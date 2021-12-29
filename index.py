import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'streamlit'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'streamlit_echarts'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PIL'])

import streamlit as st  

import pandas as pd
import numpy as np

from streamlit_echarts import st_echarts
from PIL import Image

import datastream as ds
import vizopt as vo
import styling

sonic_df = pd.DataFrame(ds.data_stream())                                           

st.set_page_config(layout="wide")    

st.markdown(styling.setStyle(), unsafe_allow_html=True)     
                          
logoList = ['sonic2.png','sonic.png','sonic-rush.png','sonic-heroes.png','sonic-secret-rings.png']

st.markdown('<h1 style="font-size: 72px;"><b style="color: #1f41a3;">Sonic</b> video games sales through the years</h1>', unsafe_allow_html=True)

with st.container():
    x_col1, x_col2 = st.columns([2,4])
    
    with x_col1:
        st.image(Image.open('media/sonic-full.png'))
        
    with x_col2:
        st.markdown('<p style="font-size: 14px;">Sonic the hedgehog has been a SEGA icon since the early 90s, as well as a pop culture icon like Mario Bros for Nintendo. In its development, Sonic is not only exclusively played on the SEGA game console, but also penetrates various other popular game consoles.</p>', unsafe_allow_html=True)                
        st.markdown('<p style="font-size: 14px;">And among so many Sonic game titles spread across various gaming platforms, below are the 5 titles with the highest sales. Is your favorite Sonic game any of them?</p>', unsafe_allow_html=True)
        
        with st.expander('Sonic the Hedgehog is a Japanese video game series and media franchise created and owned by Sega. The franchise follows Sonic, an anthropomorphic blue hedgehog who battles the evil Doctor Eggman, a mad scientist. The main Sonic the Hedgehog games are platformers mostly developed by Sonic Team; other games, developed by various studios, include spin-offs in the racing, fighting, party and sports genres. The franchise also incorporates printed media, animations, feature films, and merchandise.'):  
            st.markdown('<p style="font-size: 14px;">Sega developed the first Sonic game, released in 1991 for the Sega Genesis, to compete with Nintendo\'s mascot Mario. Its success helped Sega become one of the leading video game companies during the fourth generation of video game consoles in the early 1990s. Sega Technical Institute developed the next three Sonic games, plus the spin-off Sonic Spinball (1993). After a hiatus during the unsuccessful Saturn era, the first major 3D Sonic game, Sonic Adventure, was released in 1998 for the Dreamcast. Sega exited the console market and shifted to third-party development in 2001, continuing the series on Nintendo, Xbox, and PlayStation systems.</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-size: 14px;">While Sonic games often have unique game mechanics and stories, they feature recurring elements such as the ring-based health system, level locales, and fast-paced gameplay. Games typically feature Sonic setting out to stop Eggman\'s schemes for world domination, and the player navigates levels that include springs, slopes, bottomless pits, and vertical loops. While Sonic and Eggman were the only characters introduced in the first game, the series would go on to have a large cast of characters; some, such as Miles "Tails" Prower, Knuckles the Echidna, and Shadow the Hedgehog, have starred in spin-offs. The franchise has crossed over with other video game franchises in games such as Mario & Sonic, Sega All-Stars, and Super Smash Bros.</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-size: 14px;">Sonic the Hedgehog is Sega\'s flagship franchise and one of the bestselling video game franchises, selling over 140 million units by 2016 and grossing over $6 billion as of 2020. Series sales and free-to-play mobile game downloads totaled 1.14 billion units as of 2020. The Genesis Sonic games have been described as representative of the culture of the 1990s and listed among the greatest of all time. Although later games, notably the 2006 series reboot, have been criticized for a perceived decline in quality, Sonic is influential in the video game industry and is frequently referenced in popular culture. The franchise is also known for its fandom that produces unofficial media, such as fan art and fangames. </p>', unsafe_allow_html=True)
            st.markdown('<a href="https://en.wikipedia.org/wiki/Sonic_the_Hedgehog" target="_blank" style="font-size: 14px; float: right;">read more...</a>', unsafe_allow_html=True)

options = vo.set_chart_option(sonic_df)

with st.container():
    x_col1, x_col2 = st.columns([1,3])
    
    with x_col1:
        st.markdown('<div style="height: 60px;"></div>', unsafe_allow_html=True)
        st.image(Image.open('media/'+logoList[0]))
        st.image(Image.open('media/'+logoList[1]))
        st.image(Image.open('media/'+logoList[2]))
        st.image(Image.open('media/'+logoList[3]))
        st.image(Image.open('media/'+logoList[4]))
        
    with x_col2:
        st_echarts(options=options, height="650px") 
        
with st.container():
    footer_col1, footer_col2 = st.columns(2)
    
    with footer_col1:
        st.markdown('<div style="text-align: left;">Design by: <a href="https://www.linkedin.com/in/rahman-firmansyah-79283512b" target="_blank">Rahman Firmansyah</a></div>', unsafe_allow_html=True)
        
    with footer_col2:
        st.markdown('<div style="text-align: right;">Data source: <a href="https://www.kaggle.com/gregorut/videogamesales">Video Game Sales</a></div>', unsafe_allow_html=True)

with st.expander('Credits (image)'):  
    st.markdown('<p style="font-size: 12px;">Sonic The Hedgehog (character) : <a href="https://sega.fandom.com/wiki/Sonic_the_Hedgehog" target="_blank">https://sega.fandom.com/wiki/Sonic_the_Hedgehog</a></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 12px;">Sonic 2 :<a href="https://logos.fandom.com/wiki/Sonic_the_Hedgehog_2" target="_blank">https://logos.fandom.com/wiki/Sonic_the_Hedgehog_2</a></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 12px;">Sonic : <a href="https://logos.fandom.com/wiki/Sonic_the_Hedgehog" target="_blank">https://logos.fandom.com/wiki/Sonic_the_Hedgehog</a></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 12px;">Sonic Rush : <a href="https://sonic.fandom.com/wiki/Sonic_Rush" target="_blank">https://sonic.fandom.com/wiki/Sonic_Rush</a></p>', unsafe_allow_html=True)                
    st.markdown('<p style="font-size: 12px;">Sonic Heroes : <a href="https://www.pngitem.com/middle/hwTmxmR_logopedia-sonic-heroes-logo-png-transparent-png/" target="_blank">https://www.pngitem.com/middle/hwTmxmR_logopedia-sonic-heroes-logo-png-transparent-png/</a></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 12px;">Sonic and The Secret Rings : <a href="https://sonic.fandom.com/wiki/Sonic_and_the_Secret_Rings" target="_blank">https://sonic.fandom.com/wiki/Sonic_and_the_Secret_Rings</a></p>', unsafe_allow_html=True)