import json

import requests


# In config later
cookies = {
    'perf_dv6Tr4n': '1',
    'intercom-id-t3kzf11w': 'dc654a40-c0ea-4727-841d-a8f52fbf765e',
    'intercom-device-id-t3kzf11w': 'ee1ee19f-23b2-49a6-a542-8693021220c9',
    'connect.sid': 's%3A7che7jOHHSFV5UJxIhuefctIHHrHgxnk.lfJZdwU5JyzCCG7dfCjT5vlSUmr6AtxRnWhLZEkRwHs',
    'XSRF-TOKEN': 'YhY6AX5c-S0aKGkW26ZJOWHzTvvo1G0eHW8E',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7',
    'appguid': 'a010a05a-728c-4f35-bdcf-e644b00472c5',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'if-modified-since': '0',
    'priority': 'u=1, i',
    'referer': 'https://app.gastromatic.de/app/',
    'sec-ch-ua': '"Chromium";v="133", "Not(A:Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-timezone': 'Europe/Berlin',
    'x-xsrf-token': 'YhY6AX5c-S0aKGkW26ZJOWHzTvvo1G0eHW8E',
    # 'cookie': 'perf_dv6Tr4n=1; intercom-id-t3kzf11w=dc654a40-c0ea-4727-841d-a8f52fbf765e; intercom-device-id-t3kzf11w=ee1ee19f-23b2-49a6-a542-8693021220c9; connect.sid=s%3A7che7jOHHSFV5UJxIhuefctIHHrHgxnk.lfJZdwU5JyzCCG7dfCjT5vlSUmr6AtxRnWhLZEkRwHs; XSRF-TOKEN=YhY6AX5c-S0aKGkW26ZJOWHzTvvo1G0eHW8E',
}

response = requests.get(
    'https://app.gastromatic.de/breeze/PunchTimes?$filter=(employeeId%20eq%20%2763fe1fb52b5ad760aef95796%27)%20and%20(date%20ge%20datetime%272024-12-31T23%3A00%3A00.000Z%27)&',
    cookies=cookies,
    headers=headers,
)


with open('worktime.json', 'w', newline='') as f:
    json.dump(response.json(), f)
