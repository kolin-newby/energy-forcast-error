import json

import pandas as pd


def cleanEiaData(dataFile):

    with open(dataFile) as f:
        df = pd.DataFrame(json.load(f))

    # invalid -> NaN (non-numeric strings, None, empty)
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    # invalid -> NaT (non-datetime string, None, empty)
    df["period"] = pd.to_datetime(df["period"], format="%Y-%m-%d", errors="coerce")

    # zero / negative demand or forecast isn't physically meaningful -> NaN
    badVal = df["value"] <= 0
    df.loc[badVal, "value"] = pd.NA

    print(f"invalid/non-positive values: {df['value'].isna().sum()} of {len(df)}")
    print(f"invalid periods: {df['period'].isna().sum()} of {len(df)}")

    # keep code -> name lookup before dropping descriptive columns
    respondents = (
        df[["respondent", "respondent-name"]]
        .drop_duplicates()
        .set_index("respondent")["respondent-name"]
    )

    # descriptive/constant columns: names are in the lookup, type/timezone
    # descriptions duplicate their codes, units are always megawatthours
    df = df.drop(
        columns=["respondent-name", "type-name", "timezone-description", "value-units"]
    )

    return df, respondents
