import urllib.request
import json


def get(word, count=5):
    params = urllib.parse.urlencode({
        'part': word + ' ',
        'v': 4,
        'esn': count
    })

    req = urllib.request.Request(
        url='https://suggest.yandex.ru/suggest-ya.cgi?%s' % params,
    )

    res = urllib.request.urlopen(req)

    return json.loads(res.read().decode('utf8'))[1]
