# ---------------------------------LiBRARIES--------------------------------------
import streamlit as st
import matplotlib as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests

# ---------------------------------PAGE SETUP--------------------------------------

st.set_page_config(page_title='Madrid Airbnb', layout='wide')

# ---------------------------------MADRID DATA--------------------------------------

madrid = pd.read_csv('data/madrid_clean.csv')

#----------------------SIDEBAR------------------------------------

#Lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_url_airbnb = "https://assets2.lottiefiles.com/packages/lf20_2hYese.json"
lottie_airbnb = load_lottieurl(lottie_url_airbnb)

st.set_option('deprecation.showPyplotGlobalUse', False)
with st.sidebar:
    st_lottie(lottie_airbnb,width=200, height=200)
st.sidebar.write('---')
st.sidebar.title('Menu')
index= st.sidebar.selectbox(
            'Choose the option',
            ('Main Page','Data Visualization', 'Maps','Word Cloud'))
st.sidebar.write('---')


# ---------------------------------MAIN PAGE--------------------------------------

if index == 'Main Page':

    st.image('https://viajes.nationalgeographic.com.es/medio/2019/03/20/puerta-del-sol-madrid_acdeeb0f_1280x720.jpg')

    st.text('Imagen National Geografhic viajes')

    st.title('AIRBNB: MADRID ')

    col1, col2 = st.columns(2)
    col2.subheader("A Streamlit web app by Ignacio Torralba Ruiz")

#Introduction
    st.markdown(
        "The starting point is the consideration that there is a big problem with AirBnb rental housing and tourism in cities. We are going to work with a `dataset` to analyze this problem."
    )
    st.markdown(
        "It is known that many private owners find it more profitable and lucrative to rent flats to tourists than to locals (especially in city centers), and many real estate agencies buy properties and convert them into tourist accommodation as well. All of this has the effect of reducing supply, increasing prices, and pushing local businesses to other neighborhoods, leaving only tourists in the center."
    )
    st.markdown(
        "With this in mind, and knowing that Airbnb is one of the most popular online marketplaces for accommodation today, we will dig into the data for:"
    )
    st.markdown(
        "- On the one hand, to evaluate the impact that Airbnb has on housing (in this case, the city of Madrid is analyzed)."
    )
    st.markdown(
        "- On the other hand, inquire about who, when and how is rented and possibly make considerations about tourist flows."
    )

#Table Airbnb / Madrid
    tabs = st.tabs(["AIRBNB", "MADRID"])

    #Table Airbnb
    tab_plots = tabs[0]
    with tab_plots:
        #Control space and rows (format)
        row1_1, row1_2 = st.columns((1,1))
    
    #Row control 1
        with row1_1:
            st.image('https://1000marcas.net/wp-content/uploads/2020/01/Airbnb-simbolo.jpg', width=300)
            st.markdown('Imagen [1000marcas](https://1000marcas.net/)')
        
        with row1_2:
            st.markdown(
            "Airbnb is a online marketplace and hospitality service that allows people to lease or rent short-term lodging, including vacation rentals, apartment rentals, homestays, hostel beds, or hotel rooms. The company was founded in 2008 by Brian Chesky, Joe Gebbia and Nathan Blecharczyk. It is headquartered in San Francisco, California. The platform enables hosts to list their properties for rent and guests to book accommodations. The platform is now available in over 220 countries and territories worldwide."
            )

    #Table Madrid
    tab_plots = tabs[1]
    with tab_plots:
        #Control space and rows (format)
        row2_1, row2_2 = st.columns((1,1))
    
    #Row control 2
        with row2_1:
            st.markdown(
            "Madrid is the capital and largest city of Spain. It is located in the center of the country and has a population of approximately 3.3 million people. Madrid is known for its rich cultural heritage, with famous museums such as the Prado and the Reina Sofia, as well as many historic landmarks and monuments. The city is also known for its vibrant nightlife and delicious cuisine."
            )
        
        with row2_2:
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Bandera_de_la_ciudad_de_Madrid.svg/800px-Bandera_de_la_ciudad_de_Madrid.svg.png', width=400)
            st.markdown('Imagen [wikipedia](https://es.wikipedia.org/wiki/Madrid)')

    # More information option   
    if st.button('You can click here to see the dataframe'):
        st.dataframe(madrid)

elif index == 'Data Visualization':
    # Data Visualization 
    st.title('Data Visualization')
    #Table Airbnb / Madrid
    tabs2 = st.tabs(["CORRELATION", "NEIGHBOURHOOD GROUP","NEIGHBOURHOOD","ROOM TYPE", "NEIGHBOURGROUP AND AVAILABILITY"])

    #Table Correlation
    tab_plots2 = tabs2[0]
    with tab_plots2:
        
        st.image('imagen/correlation.png', width=1000)

    #Table neighbourhood_group
    tab_plots2 = tabs2[1]
    with tab_plots2:
        
        st.image('imagen/neighbourhood_group.png', width=1000)

    #Table neighbourhood
    tab_plots2 = tabs2[2]
    with tab_plots2:
        
        st.image('imagen/neighbourhood.png', width=1500)

    #Table room type
    tab_plots2 = tabs2[3]
    with tab_plots2:
        
        st.image('imagen/room_type.png', width=1000)

    #Table NEIGHBOURGROUP AND AVAILABILITY
    tab_plots2 = tabs2[4]
    with tab_plots2:
        
        st.image('imagen/neigh_avail.png')

elif index == 'Maps':
    # MAPS
    st.title('Maps Visualization')
    #Table maps
    tabs3 = st.tabs(["NEIGHBOURHOOD GROUP","NEIGHBOURHOOD","ROOM TYPE", "AVAILABILITY"])       
    
    #Table NEIGHBOURHOOD GROUP
    tab_plots3 = tabs3[0]
    with tab_plots3:
        
        st.image('imagen/map_neighgroup.png', width=1000)
    
    #Table NEIGHBOURHOOD GROUP
    tab_plots3 = tabs3[1]
    with tab_plots3:
        
        st.image('imagen/map_neighbourhood.png', width=1000)

    #Table ROOM TYPE
    tab_plots3 = tabs3[2]
    with tab_plots3:
        
        st.image('imagen/map_roomtype.png', width=1000)

    #Table AVAILABILITY
    tab_plots3 = tabs3[3]
    with tab_plots3:
        
        st.image('imagen/map_avail.png', width=1000)

else:
    # Word Cloud
    st.title('Word Cloud')
    st.image('imagen/WordCloud.png', width=1000)



#SIDEBAR 2 part
more_info = st.sidebar.expander("More information? 👉")
with more_info:
    st.markdown(
            "If you want more information abaut Airbnb, press [Airbnb](https://www.airbnb.es/).")
    st.markdown(
            "If you want more information abaut Madrid, press [Madrid](https://www.esmadrid.com/).")
    
if(st.sidebar.button("Curiosity")):
    st.sidebar.write('Casa Botín, founded in 1725, is the oldest restaurant in the world according to the Guinness Book of Records and one of the benchmarks for the best traditional cuisine in Madrid.')
    st.sidebar.image('https://estaticos.esmadrid.com/cdn/farfuture/jKC_8Rj15xCjs1VUaoLtzGIFFybPVfu8GXOWUg9s1Nw/mtime:1643971179/sites/default/files/recursosturisticos/restaurantes/casa_botin-baja-05.jpg', 
        width=300,caption='esmadrid.com')
