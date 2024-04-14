import os
import requests


__all__ = ['rq', 'fetch']


endpoint = 'https://www.strava.com/api/v3'
api_key = os.environ['STRAVA_API_KEY']


def rq(path, method='GET', **kwargs):
    url = f'{endpoint}{path}'
    headers = { 'Authorization': f'Bearer {api_key}' }

    return requests.request(method, url, headers=headers, **kwargs)


def fetch(path, method='GET', **kwargs):
    res = rq(path, method, **kwargs)

    try:
        return res.json()
    except:
        print('Error:', res.status_code, res.content.decode())
        raise

