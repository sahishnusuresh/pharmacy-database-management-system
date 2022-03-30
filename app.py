# streamlit_app.py
import pandas as pd
import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.cache to only run once.


@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])


conn = init_connection()
cur = conn.cursor()
conn.autocommit = True
# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.


pageMenu = ["pharmacy", "doctor", "hospital", "patient", "supplier"]
choice = st.sidebar.selectbox("menu", pageMenu)
if st.sidebar.button("generate bill"):
    amount = st.text_input("amount", 0)
    bill_id = st.text_input("bill_id", 0)
    medicine_id = st.text_input("medicine_id", 0)
    patient_id = st.text_input("patient_id", 0)
    pharmacy_id = st.text_input("pharmacy_id", 0)
    quantity = st.text_input("quantity", 0)
    if st.button("generate"):
        pass

elif(choice == pageMenu[0]):
    cur.execute('Select * from pharmacy;')
    rows = list(cur.fetchall())
    # Print results.
    df = pd.DataFrame(rows, columns=["name", "id", "city"])
    st.table(df)
elif(choice == pageMenu[1]):
    cur.execute('Select * from doctor;')
    rows = list(cur.fetchall())
    # Print results.
    df = pd.DataFrame(rows)
    st.table(df)
elif(choice == pageMenu[2]):
    cur.execute('Select * from hospital;')
    rows = list(cur.fetchall())
    # Print results.
    df = pd.DataFrame(rows)
    st.table(df)
elif(choice == pageMenu[3]):
    with st.expander("records"):
        cur.execute('Select * from patient;')
        rows = list(cur.fetchall())
        # Print results.
        df = pd.DataFrame(rows)
        st.table(df)
elif(choice == pageMenu[4]):
    cur.execute('Select * from supplier;')
    rows = list(cur.fetchall())
    # Print results.
    df = pd.DataFrame(rows)
    st.table(df)
