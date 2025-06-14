import streamlit as st
import google.generativeai as genai


#import matplotlib.pyplot as plt

st.title("about your marks")
st.subheader("Aritra Kabiraj")


physics = st.number_input("Enter your physics number", 0, 100, step=1)
chemistry = st.number_input("Enter your chemistry number", 0, 100, step=1)
maths = st.number_input("Enter your Mathematics number", 0, 100, step=1)
english = st.number_input("Enter your english number", 0, 100, step=1)
biology = st.number_input("Enter your biology number", 0, 100, step=1)


# st.checkbox("Chose from this following options: "['Horizontal Bar','Vartical Bar','graphs'])
graph = st.radio("Select of the representations : ",['graphically','barview','sideplot'])
making_graph = st.button(f"Make {graph}")
st.badge(f"{graph}ical representation")

if making_graph:


    promt = f"""I have marks in 5 subjects: Physics = {physics}, Chemistry = {chemistry}, Mathematics = {maths}, English = {english}, Biology = {biology}.

Please describe how this data would look in a graphical representation like a bar chart. Mention:
- Which subject has the highest and lowest marks
- Any interesting comparisons
- and give me in which stream i should go after class 10 """
    genai.configure(api_key="AIzaSyAtTWxergRwQTmwJrc3e4QofkHnNkQaQBM")
    #promt = f""" take this all subjects{physics,chemistry,maths,english,biology} and their marks and make a graphical representation of this   """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(promt)
    st.write(response.text)

# st.divider()


# st.file_uploader("Upload your marksheet here(PDF only): ",type= ["pdf"])
# picture = st.button("Click Here to get picture")

# if picture:
#     st.image("https://velvetescape.com/wp-content/uploads/2011/11/dawid-zawila-G3rw6Y02D0-unsplash.jpg", caption="Sunrise by the mountains(Aritra Kabiraj)")

# if making_graph:




# subjects = ['Maths', 'Physics', 'Chemistry', 'biology', 'english']
# marks = [math, physics, chemistry, biology, english]

# # fig, ax = plt.subplots()
# # ax.plot(subjects, marks, marker='o', linestyle='-', color='blue')
# # ax.set_title("Simple Line Graph of Marks")
# # ax.set_xlabel("Subjects")
# # ax.set_ylabel("Marks")
# # ax.set_ylim([0, 100])
# # ax.grid(True)


# x = data["subjects"]
# y = data["marks"]
# st.write(x)
# st.write(y)
# plt.bar(subjects, marks, color = 'green')
# plt.xlabel("subjects")
# plt.ylabel("marks")
# 