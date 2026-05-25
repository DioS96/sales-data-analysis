import sys
import os

sys.path.append(os.path.abspath("."))

import pandas as pd
import requests
from services.functions import *


def test_replace_string_values():

    df=pd.DataFrame({
        "state":["CA","NY"]
    })

    replacements={
        "CA":"California",
        "NY":"New York"
    }

    result=replace_string_values(
        df,"state",replacements
    )

    assert result["state"].iloc[0]=="California"
    assert result["state"].iloc[1]=="New York"


def test_max():

    df=pd.DataFrame({
        "values":[1,50,100]
    })

    assert find_max_value(df,"values")==100

def test_remove_duplicates():

    df=pd.DataFrame(
        {
            "names":["John","Emily","Nick","John","John"],
            "age":[18,22,18,25,18]
        }
    )
    
    df=remove_duplicates(df)

    assert len(df)==4

def test_cast_columns():

    df=pd.DataFrame(
        {
            "names":["John","Emily","Nick","John","John"],
            "age":[18,22,18,25,18]
        }
    )

    df=cast_columns(
        dataframe=df,
        columns_dict={
            "names":"str",
            "age":"str"
        }
    )

    assert df["age"].dtype=="string"

def test_incosisten_values():

    df=pd.DataFrame(
        {
            "order_id":["100","101","102","103","104"],
            "amount":[None,-10,1000,2000,300,],
            "date":["2025-01-01","2025-23-10","2026-03-03","2026-30-04","2028-01-03"]
        }
    )

    df["date"]=pd.to_datetime(df["date"],format="%Y-%d-%m")

    df=inconsistent_values(df)

    assert len(df)==2



