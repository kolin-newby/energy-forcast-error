# src/fetch_eia.py
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

RAW_DIR = Path("data/raw/eia")
URL = "https://api.eia.gov/v2/electricity/rto/daily-region-data/data/"
PAGE_SIZE = 5000


def fetchEiaData(start="2019-07-01", end="2019-07-07"):

    records = []
    offset = 0

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    outPath = RAW_DIR / f"daily_region_{start}_{end}.json"
    if outPath.exists():
        return outPath

    load_dotenv()
    key = os.environ["EIA_API_KEY"]

    while True:
        params = {
            "frequency": "daily",
            "data": ["value"],
            "facets": {"type": ["D", "DF"]},
            "start": start,
            "end": end,
            "sort": [{"column": "period", "direction": "asc"}],
            "offset": offset,
            "length": PAGE_SIZE,
        }
        res = requests.get(
            URL,
            params={"api_key": key},
            headers={"X-Params": json.dumps(params)},
            timeout=60,
        )
        res.raise_for_status()

        page = res.json()["response"]["data"]
        records.extend(page)
        print(f"EIA: fetched {len(records)} rows - ✅")
        if len(page) < PAGE_SIZE:
            break
        offset += PAGE_SIZE

    outPath.write_text(json.dumps(records))
    return outPath
