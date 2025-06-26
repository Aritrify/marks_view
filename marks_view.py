import streamlit as st
import google.generativeai as genai
import matplotlib.pyplot as plt
import pandas as pd
import os
import io



#import matplotlib.pyplot as plt

st.title("About Your Marks")
st.subheader("Aritra Kabiraj")


physics = st.number_input("Enter your physics number", 0, 100, step=1)
chemistry = st.number_input("Enter your chemistry number", 0, 100, step=1)
maths = st.number_input("Enter your Mathematics number", 0, 100, step=1)
english = st.number_input("Enter your english number", 0, 100, step=1)
bengali = st.number_input("Enter your bengali number", 0, 100, step=1)
history = st.number_input("Enter your history number", 0, 100, step=1)
geography = st.number_input("Enter your geography number", 0, 100, step=1)
biology = st.number_input("Enter your biology number", 0, 100, step=1)







# st.checkbox("Chose from this following options: "['Horizontal Bar','Vartical Bar','graphs'])
graph = st.radio("Select of the representations : ",['graphically','barview','sideplot'])
making_graph = st.button(f"Know your possible trade")
#st.badge(f"{graph}ical representation")

if making_graph:


    promt = f"""I have marks in 8 subjects: Physics = {physics}, Chemistry = {chemistry}, Mathematics = {maths}, English = {english}, Biology = {biology},
    History = {history}, Geography = {geography}, Bengali = {bengali}.

Please describe how this data would look in a graphical representation like a bar chart. Mention:
- Which subject has the highest and lowest marks
- Any interesting comparisons
- you are a master in this field that you know everything in this field of compairing 
- and give me in which stream i should go after class 10 
- and give me a graph image 
"""
    genai.configure(api_key="AIzaSyAtTWxergRwQTmwJrc3e4QofkHnNkQaQBM")
    #genai.configure(api_key=os.getenv("AIzaSyAtTWxergRwQTmwJrc3e4QofkHnNkQaQBM"))
    #promt = f""" take this all subjects{physics,chemistry,maths,english,biology} and their marks and make a graphical representation of this   """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(promt)
    # responce_image = model.


    plotting = {
        "Physics": physics,
        "Chemistry":chemistry,
        "Maths":maths,
        "English":english,
        "Biology":biology,
        "History":history,
        "Geography":geography,
        "Bengali":bengali 
    }

    df = pd.DataFrame(list(plotting.items()), columns=["Subject", "Marks"])

    plt.figure(figsize=(10,6))
    plt.bar(df['Subject'],df['Marks'],color="green")
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title('Subject VS Marks')
    plt.xticks(rotation=45)
    # plt.savefig("Subject_Marks.png")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)  # Move to the beginning of the buffer
    st.image(buf)



    st.write(response.text)
