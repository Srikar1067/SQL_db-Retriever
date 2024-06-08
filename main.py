from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configuring my Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## This is the function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

##This is the  fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name food and has the following tables inside it
    named "Users", "Restaurant", "Orders", "OrderItems","DeliveryDriver","Delivery" 
    with their respected columns
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present in Orders?, 
    the SQL command will be something like this SELECT COUNT(*) FROM Orders ;
    \nExample 2 -Names of customers who have placed orders at restaurants that
    serveItalian cuisine ,  the SQL command will be something like this SELECT Name 
    FROM Users
    WHERE UserID IN (
    SELECT DISTINCT UserID 
    FROM Orders
    WHERE RestaurantID IN (
        SELECT RestaurantID 
        FROM Restaurant
        WHERE CuisineType = 'Italian'
    )
);
    like this you need to obtain sql queries for some of the nested,Corelated nested,groupby,having and joins type of Queries also
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

#This is the UI part which was done using Streamlit

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("SQL Database Data Retriever")
st.markdown("""
    <style>
    body {
        color: black;
        background-color: white;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)
question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit button is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"food.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)









