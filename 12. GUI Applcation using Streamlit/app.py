'''
use this to run >>python -m streamlit run app.py<<
import the streamlit module
'''
import streamlit as st

st.title("Welcome to DataCRUD Operations")
_namefield = st.text_input("Name")#<input type="text"/>
_emailfield = st.text_input("Email")#<input type="text"/>
_submitbutton = st.button('Submit')#<button>Submit</button>

if _submitbutton:
    st.write('successfully submitted')
    name = _namefield
    email = _emailfield
    st.write(f'Hello {name}')





# import streamlit as st
# from crud import *
# #Create a Website title 
# st.title("Welcome to DataCrud Operations:")
# 
# 
# emailTextfield= st.text_input("Email:")
# 
# submitButton = st.button("Submit")

# #How to perform event handling 
# if submitButton:
#     # con = sqlite3.connect("./database/usersDB.sqlite3") #--> check
#     #st.write("Button clicked")
#     name = nameTextfield
#     email= emailTextfield
#     #st.write(f"Hello {name} email:{email}")
#     st.success(addNewUser(name,email))
#     #Showing all Data from the Database
#     df =getAllUsers()
#     st.dataframe(df,use_container_width='width',hide_index=True) #--> check
#     #Database connection close.
#     # cursor.close()
#     # con.close()

