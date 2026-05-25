import pandas as pd
import requests 

def api_get_data(url="https://dummyjson.com/",dataset="",limit=0,params=None):

    try:

        # If params is None create empty dictionary
        if params is None:
            params = {}
            
        params["limit"]=limit

        response = requests.get(
            url + dataset,
            params=params
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")

        return None

raw_carts_df=api_get_data(dataset="carts")

def convert_to_pandas_df(
    raw_df,
    df_name=None,
    record_path=None,
    meta=None
):

    # Gets the first top-level key from the dictionary
    main_key = list(raw_df.keys())[0]

    # The nested list to explode into rows
    if record_path:

        pd_df = pd.json_normalize(
            raw_df[main_key],
            record_path=record_path,
            # Parent fields to keep
            meta=meta,
            # Prefix added to parent columns
            meta_prefix=df_name,
             # Ignore missing metadata fields
            errors="ignore"
        )

    else:
        
        # Simple normalization without nested extraction
        pd_df = pd.json_normalize(
            raw_df[main_key]
        )

    return pd_df