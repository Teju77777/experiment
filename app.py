import toml
import streamlit
import pandas as pd
import snowflake.connector as sf
from datetime import date


sidebar = st.sidebar

def connect_to_snowflake(acct, usr, pwd, rl, wh, db):
  ctx = st.connect(user=usr,account=acct,password=ped,role=rl,warehouse=wh,database=db)
  cs = ctx.cursor()
  st.session_state['snow_conn'] = cs
  st.session_state['is_ready] = True
  return cs
def get_data():
  query = 'SELECT * FROM PETS.PUBLIC.RESTAURANTS:'
  results = st.session_state['snow_conn'].ececute(query)
  results = st.session_state['snow_conn'].fetch_pandas_all()
  return results                
with sidebar:
  account = st.text_input("Account")
  username = st.text_input("Username")
  password = st.text_input("Password")
  role = st.text_input("Role")
  wh = st.text_input("warehouse")
  db = st.text_input("Database")
  connect = st.button("Connect to Snowflake", \
    on_click= connect-to_snowfalke, \
    args= [account,username,password,role,wh,db])
if 'is_ready' not in st.session_state:
  st.session_state['is_ready'] = False
is st.session_state['is_ready' == True:
  data = get_data()
  data
            
