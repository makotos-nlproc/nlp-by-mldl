import json
import requests
from chp03.conf import *


def fetch_data(**params):
    return requests.get(URL, params=params).json


def save_as_json(save_file, record):
    with open(save_file, mode='a') as f:
        f.write(json.dumps(record) + '\n')


def extract_data(response):
    for key in response['response'].keys():
        if not key.isdigit():
            continue
        d = response['response'][key]['photo']
        if d.get('comment') and d.get('total_score'):
            data = {
                'comment': d['comment'],
                'score': d['total_score']
            }
            yield data


def main():
    res = fetch_data(
        keyid=API_KEY,
        area='新宿',
        hit_per_page=50,
        offset_page=1
    )
    save_as_json(RAW_DATA, res)

    records = extract_data(res)
    for record in records:
        save_as_json(SAVE_FILE, record)


if __name__ == '__main__':
    main()