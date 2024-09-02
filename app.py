import streamlit as st
from PIL import Image
import datetime

st.title('Hello....')
st.write('I am Streamlit website created by Soumita!!!!')

st.header('It is header')
st.subheader('It is sub-header')

st.info("This is a info")

st.success('Yes you get success')
st.warning('Sorry you may face problem.. It is a warning message')
st.error('Try again.There is some errors')

q=ZeroDivisionError("Try to divide by 0")
st.exception(q)

st.write(range(10))

img=Image.open('st.png')
st.image(img,width=300)

#Checkbox --> Select multiple options or single option
if st.checkbox("Show/Hide"):
    st.text("Showing the wizard...")
    
#Radio button
r=st.radio("Select Gender",('Male','Female'))
if r=='Male':
    st.success('You are a male')
else:
    st.success('You are a female')
    
#Selectbox
hobby=st.selectbox("Hobbies",['Reading','Gardening','Watching Movie','Travelling'])
st.write('Your hobby is ',hobby)

hobby=st.multiselect("Hobbies",['Reading','Gardening','Watching Movie','Travelling'])
st.write('Your hobby is ',len(hobby),'hobby')

#button
st.button('Click Me')

if st.button('About'):
    st.text('Welcome to streamlit....')
    
#Take input
n=st.text_input("Enter name:")
st.write('Your name is ',n.title()) #title() function in python make the first letter of any text in capital and next followed letters are in small letters


#create Calculator
t1=st.number_input("Enter the first number : ")
t2=st.number_input("Enter the second number: ")
sum=t1+t2
st.write('Sum is ',sum)

#Slider
st.slider("Select level",1,50)

age=st.slider("Enter age",min_value=0,max_value=100,value=10)
st.write("Your age is ",age)

#Calender
date=st.date_input("Whats your birthday?",datetime.date(2024,1,1),datetime.date(1990,1,1),datetime.datetime.now())
st.write("Your birthday is ",date)


#Columns
c1,c2=st.columns(2)
with c1:
    st.write("Column 1 content here")
with c2:
    st.write("Column 2 content here")

#To hide something
with st.expander('See Details'):
    st.write("i am hidden...")
    
#Sidebar
option=st.sidebar.selectbox('Choose Option',['a','b','c'])
st.write(f'you selected {option}') #Formate string


#Comment
st.markdown(
    '''
    <style>
    .hello{
        font-size:20px;
    }
    </style>
    ''',unsafe_allow_html=True)

st.markdown("<p class='hello'>I am Soumita</p>",unsafe_allow_html=True)

#Count
if 'count' not in st.session_state:
    st.session_state['count']=0
if st.button('Click me'):
    st.session_state['count']+=1
st.write('Count is ',st.session_state['count'])