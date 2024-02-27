import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import date, datetime
import pytz

def udpate_database(name, phone, email, query):
    
    conn = st.connection("gsheets", type=GSheetsConnection)
    worksheet = "contactme"
    backup_sheet = "backup"

    existing_data = conn.read(worksheet=worksheet, usecols = list(range(6)), ttl=5)

    conn.update(worksheet=backup_sheet, data = existing_data)


    today_date = date.today().strftime("%Y-%m-%d")
    ist = pytz.timezone('Asia/Kolkata') 
    time_now = datetime.now(ist).strftime("%H:%M:%S")

    tem_df = pd.DataFrame(
        {
            "date": [today_date],
            "time": [time_now],
            "name": [name],
            "phone": [phone],
            "email": [email],
            "query": [query]
        }
    )

    tem_df.columns = existing_data.columns

    updated_data = pd.concat([tem_df,existing_data], ignore_index=True)

    conn.update(worksheet=worksheet, data=updated_data)

    return("Successfully updated")
