# Import python packages

import streamlit as st
#from snowflake.snowpark.functions import col


# Write directly to the app
st.title("Customize Your Smoothie!! ")
st.write(
    """
    Choose the fruits you want in your custom Shoothie!
    """
)

#input the name modified from the documentation
name_on_order=st.text_input('Name on Smoothie')
st.write('Name on Smoothie will be:',name_on_order)


session = get_active_session()
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


cnx.st.connection('snowflake')
session=cnx.session()



     
