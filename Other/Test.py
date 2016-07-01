import requests
from bottle import route, run, template, request, redirect


def get_info_from_film_name(film_name):
    real_name = "%20".join(film_name.split())
    page = requests.get("http://api.kinopoisk.cf/searchFilms?keyword={film_name}".format(film_name=real_name))
    content = eval(page.content)
    content = content["searchFilms"][0]

    name = content["nameRU"]
    description = content["description"]
    year = content["year"]
    rating = content["rating"].split()[0]
    kp_id = int(content["id"])
    print([name, description, rating, year, kp_id])
    return [name, description, rating, year, kp_id]


@route('/')
def index():
    return '''
        <form action="/" method="post">
            Название фильма: <input name="film" type="text" />
            <input value="name_of_film" type="submit" />
        </form>
    '''


@route('/', method='POST')
def do_appear():
    film_name = request.forms.film
    print(film_name)
    kp_id = get_info_from_film_name(film_name)[4]
    redirect("/{kp_id}".format(kp_id=kp_id))


@route('/<kp>')
def get_video(kp):
    return template(
        '<iframe src="http://v1.domkino.kz/player/player.php?kp={{kp}}" width="800" height="450" scrolling="no" border=0 allowfullscreen="true"></iframe>', kp=kp)


run(host='0.0.0.0', port=80)
