import requests
from bs4 import BeautifulSoup
from vk_core import Vk


def get_audio(link, page):
    soup = BeautifulSoup(requests.get(link, params={'page': page}).content, "lxml")
    return [td.text.replace("\n", "") for td in soup.findAll('td', {'class': "chartlist-name"})]

tracks = []
for i in range(1, 4):
    tracks.extend(get_audio("http://www.last.fm/ru/user/redheadgenious/loved", i))

vk = Vk()

for track in tracks:
    try:
        vk_track = vk.method("audio.search", {
            "q": track,
            "auto_complete": 1,
            "sort": 2
        }).get('items')[0:0]
        track_id = vk_track.get('id')
        owner_id = vk_track.get('owner_id')
        vk.method("audio.add", {
            "audio_id": track_id,
            "owner_id": owner_id
        })
    except: continue