import streamlit as st
import pandas as pd
import numpy as np


@st.cache_resource
def init_connection():
    return snowflake.connector.connect(
        **st.secrests["snowflake"], client_session_keep_alive=True
    )
conn = init_connection()

@st.cache_data
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetch_pandas_all()

