# https://www.eia.gov/opendata/documentation.php
# Documentation for this data source

import requests


def fetchEiaData():
    apiEndpoint = "api.eia.gov/v2/electricity/rto/daily-region-data/data/"
    queryParamList = [
        "frequency=daily",
        "data[0]=value",
        "start=2019-01-01",
        "end=2026-10-01",
        "sort[0][column]=period",
        "sort[0][direction]=desc",
        "offset=0",
        "length=5000",
    ]

    queryParamString = "&".join(queryParamList)

    headers = {}

    res = requests.get("https://" + apiEndpoint + "?" + queryParamString)

    print(res)


fetchEiaData()
