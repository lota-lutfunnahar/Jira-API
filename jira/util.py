import math
from typing import Mapping, Any

import requests as rest

import jira


def get_all(endpoint: str, what: str, params: Mapping[str, Any] = None) -> Mapping[str, Any]:
    if params is None:
        params = {}

    url = jira.API_URL + endpoint

    print("usl is ", url)

    print("Auth ", jira.AUTH)

    # data = []

    # data = rest.get(url, auth=jira.AUTH, params=params)
    data = rest.get(url, auth=jira.AUTH).json()
    print('response: 👉️', data)
    # print('response.status_code: 👉️', data.status_code)
    # print('response.headers: 👉️', data.headers)

    print('OK GET', endpoint)

    if data['total'] > data['maxResults']:
        for page in range(1, math.ceil(data['total'] / data['maxResults'])):
            temp = rest.get(url, auth=jira.AUTH, params={
                **params,
                'startAt': page * jira.PAGE_SIZE  # specify the offset
            }).json()
            print('OK GET', endpoint)
            # data[what] += temp[what]

    return data
