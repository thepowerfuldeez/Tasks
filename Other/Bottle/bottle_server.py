import requests
import logging
from bottle import route, run, template, request, redirect

film_infos = []

logging.basicConfig(filename="logfile.txt")
stderrLogger = logging.StreamHandler()
stderrLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logging.getLogger().addHandler(stderrLogger)


def get_info_from_film_name(film_name):
    real_name = "%20".join(film_name.split())
    page = requests.get("http://api.kinopoisk.cf/searchFilms?keyword={film_name}".format(film_name=real_name))
    try:
        content = eval(page.content)
        content = content["searchFilms"]
    except: content = []
    result = []

    for film in content:
        try: name = film["nameRU"]
        except: name = ""

        try: description = film["description"]
        except: description = ""

        try: year = film["year"]
        except: year = ""

        try: rating = film["rating"].split()[0]
        except: rating = ""

        try: kp_id = int(film["id"])
        except: kp_id = 0

        try: result.append([name, description, rating, year, kp_id])
        except: pass

        print([name, description, rating, year, kp_id])

    return result


@route('/')
def index():
    return '''
        <a href="/"><img src="http://i.imgur.com/Q1b0vo3.png"></a>
        <form action="/" method="post">
            Название фильма: <input name="film" type="text" />
            <input value="Смотреть" type="submit" />
        </form>
    '''


@route('/', method='POST')
def do_appear():
    global film_infos
    film_name = request.forms.film
    print(film_name)
    film_infos = get_info_from_film_name(film_name)
    try: kp_id = film_infos[0][4]
    except: kp_id = 0

    redirect("/{kp_id}".format(kp_id=kp_id))


@route('/<kp>')
def get_video(kp):
    try:
        global film_infos

        try: others = film_infos[1:]
        except: others = []

        try: name = film_infos[0][0]
        except: name = ""

        try:
            text = '<p>Возможно вы имели в виду:</p>' + '\n'.join(['<br><a href="/{kp}">{name}</a>'
                                                                  .format(name=film[0], kp=film[4]) for film in others])
        except: text = ''
        film_infos = []

        return template(
            '''
            <a href="/"><img src="http://i.imgur.com/Q1b0vo3.png"></a>
            <form action="/" method="post">
                Название фильма: <input name="film" type="text" />
                <input value="Смотреть" type="submit" />
            </form>
            <br>
            <h2>{{name}}</h2>
            <iframe src="http://v1.domkino.kz/player/player.php?kp={{kp}}" width="800" height="450" scrolling="no" border=0 allowfullscreen="true"></iframe>
            ''' + text, name=name, kp=kp)
    except Exception as e:
        print(e.__traceback__)


if __name__ == "__main__":
    run(host='0.0.0.0', port=81)
