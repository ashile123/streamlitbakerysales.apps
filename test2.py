import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    bakery=pd.read_csv('datasets1/Bakery sales.csv')
    bakery.drop(columns=['Unnamed: 0'], inplace = True)
    bakery['unit_price2']=bakery.unit_price.str.replace(',','.')
    bakery['unit_price2']=bakery.unit_price.str.replace('€','')
    bakery['unit_price2']=bakery.unit_price2.str.replace(',','.')
    bakery['unit_price2']=bakery.unit_price2.str.strip()
    bakery.drop(columns=['unit_price'], inplace = True)
    bakery['unit_price2']=bakery.unit_price2.astype('float')
    return bakery.head(10)

bakery = load_data()


st.title('Demo app')

st.subheader('Learn the basis structure')

st.write('Bakery Sales Data')
bakery=load_data()
st.write(bakery)
    
                       