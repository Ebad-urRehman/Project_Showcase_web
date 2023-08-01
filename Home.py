import streamlit as st
import pandas
st.set_page_config(layout= "wide")
col1, col2 = st.columns(2)


with col1:
    st.image("images/myimage.png", width=300)

with col2:
    st.title("Ebad-ur-Rehman")
    content = """
    Aslam u Alaikum, I am Learning python Programming
    and these are my learning projects you can use them """
    st.info(content)

st.write("Below You can found some of the Apps I have Built in python")

# col3, col4 =st.columns(2)
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

dataframe = pandas.read_csv("006 data.csv", sep = ",")

with col3:
    for index, row in dataframe[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")
        # st.write("[Source Code](https://pythonhow.com)")


with col4:
    for index, row in dataframe[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


"""      Details
line number : Description
2 : panda is used to access csv (Excel) files
4, 19 : # creating two columns
7, 10, 24, 33 : adding widgets in respective columns using with keyword 
15 : # .info method change appearance of the text (added a background layer color to show Importance of Text)
20 : adding an empty column to format the columns 3 and 5 1.5 ,0.5 and 1.5 are ratios of respective columns
this will make it easy for mobile devices to render in proper format as well
22 : # accessing data from csv importing pandas
"""
