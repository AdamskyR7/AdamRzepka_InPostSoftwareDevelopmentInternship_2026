import requests
import pandas as pd
import json
import time


def getData(fetchFromAPI: bool) -> pd.DataFrame:
    if not fetchFromAPI:
        try:
            with open('paczkomatData.json', 'r') as f:
                print("File found")
                return pd.json_normalize(json.load(f))
        except FileNotFoundError:
            print("File not found. Downloading data from API. It will take a while.")

    return getAPIdata()


def getAPIdata() -> pd.DataFrame:
    base_url = "https://api-global-points.easypack24.net/v1/points/"
    all_paczkomats = []

    current_page = 1
    total_pages = 1

    print("Starting data fetch")
    while current_page <= total_pages:
        try:
            response = requests.get(base_url, params={'page': current_page})
        except requests.exceptions.RequestException as e:
            print(f"There was an error: {e}, on page {current_page}")
            break


        data = response.json()

        if current_page == 1:
            total_pages = data.get('total_pages')

        paczkomats_onPage = data.get('items')

        all_paczkomats.extend(paczkomats_onPage)

        print(f"{current_page} of {total_pages}")
        current_page += 1

        time.sleep(0.2)

    print("Finished data fetch")

    if all_paczkomats:
        with open('paczkomatData.json', 'w', encoding='utf-8') as f:
            json.dump(all_paczkomats, f, indent=4)

    return pd.json_normalize(all_paczkomats)