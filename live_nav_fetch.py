import requests
import pandas as pd

scheme_codes = [119551, 120503, 118632, 119092, 120841]

all_data = []

for code in scheme_codes:

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    fund_name = data["meta"]["scheme_name"]

    latest_nav = data["data"][0]["nav"]

    nav_date = data["data"][0]["date"]

    print(fund_name)
    print("NAV:", latest_nav)
    print()

    all_data.append({
        "scheme_code": code,
        "fund_name": fund_name,
        "nav": latest_nav,
        "date": nav_date
    })

df = pd.DataFrame(all_data)

df.to_csv("data/raw/live_nav_5_funds.csv", index=False)

print("CSV Saved Successfully")