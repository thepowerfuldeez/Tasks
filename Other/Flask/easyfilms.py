import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def get_kp_id_from_film_name(film_name):
    try:
        return int(eval(requests.get(
            "http://api.kinopoisk.cf/searchFilms?keyword={}".format("%20".join(film_name.split()))).content)["searchFilms"][0].get("id", "0"))
    except Exception as e:
        print(e.args)
        print("at get_kp_id")
        return 0


def get_film_from_kp_id(kp_id):
    try:
        return eval(requests.get("http://api.kinopoisk.cf/getFilm?filmID={}".format(kp_id)).content)
    except Exception as e:
        print(e.args)
        print("at get_film_name")
        return ""


def get_info(film, kp_id=0):
    kp_id = int(film.get("id", kp_id))
    name = film.get("nameRU", "")
    name_en = film.get("nameEN", "")
    description = film.get("description", "")
    poster_url = "http://st.kp.yandex.net/images/film_big/{}.jpg".format(kp_id)
    film_length = film.get("filmLength", "")
    year = film.get("year", "")
    country = film.get("country", "")
    genre = film.get("genre", "")
    rating = film.get("rating", "")
    return {"kp_id": kp_id, "name": name, "name_en": name_en, "description": description, "poster_url": poster_url,
            "film_length": film_length, "year": year, "country": country, "genre": genre, "rating": rating}


def get_search_results(film_name):
    try:
        content = eval(requests.get(
            "http://api.kinopoisk.cf/searchFilms?keyword={}".format("%20".join(film_name.split()))).content)[
            "searchFilms"]
    except Exception as e:
        print(e.args)
        print("at get_info start")
        content = []
    return content[1:6]


def get_similar_films(kp_id):
    try:
        return eval(requests.get("http://api.kinopoisk.cf/getSimilar?filmID={}".format(kp_id)).content)["items"][0][:5]
    except Exception as e:
        print(e.args)
        print("at get_similar")
        return []


@app.route("/", methods=['POST', 'GET'])
@app.route("/<kp_id>")
def index(kp_id=None, name='Пусто'):
    if not kp_id:
        if request.method == 'POST':
            input_name = request.form["film"]
            if not input_name:
                return render_template("error.html")
            else:
                print(input_name)
                kp_id = get_kp_id_from_film_name(input_name)
                return redirect("/{}".format(kp_id))
        else:
            return render_template("film.html")
    else:
        if name == 'Пусто':
            try:
                result_film = get_info(eval(requests.get("http://api.kinopoisk.cf/getFilm?filmID={}".format(kp_id)).content), kp_id)
            except Exception:
                return render_template("error.html")
            other = [get_info(film) for film in get_search_results(result_film.get("name", ""))]
            similar = [get_info(film) for film in get_similar_films(kp_id)]

            return render_template("film.html", kp_id=kp_id, result_film=result_film, other=other, similar=similar)
        else:
            return render_template("error.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
