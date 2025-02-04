Import python packages

import streamlit as st
from snowflake.snowpark.functions import col
import os
import requests
import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:


st.write(
	"Has environment variables been set:",
	os.environ["db_username"] == st.secrets["db_username"])
# Write directly to the app

st.title("My parents new healthy dinner!! ")
st.write(
    """
    Choose the fruits you want in your custom Shoothie!
    """
)

#input the name modified from the documentation
name_on_order=st.text_input('Name on Smoothie')
st.write('Name on Smoothie will be:',name_on_order)

#
#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list= st.multiselect(
    'Choose up to 5 ingredients!:',
    my_dataframe ,
    max_selections=5
   
)
if ingredients_list:
 ingredients_string=''


 for x in ingredients_list:
   ingredients_string+=x+' '

 #st.write(ingredients_string)

 my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""

 st.write(my_insert_stmt)
 #st.stop()

#st.write(my_insert_stmt)
 time_to_insert=st.button('submit order')

 if time_to_insert:
    
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered! '+name_on_order, icon="✅")

smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
#st.text(smoothiefroot_response.json())
sf_df=st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)

cnx.st.connection("snowflake")
session=cnx.session()



     
