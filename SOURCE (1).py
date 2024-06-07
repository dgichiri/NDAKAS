# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random

st.write("""
 
# Welcome to A Night In Paris
        
         """)

msgs = ['We thought you should know, that just like an Olympian, you can inspire greatness in everything you do, and in everyone around you. Keep reaching for your dreams!',
        'Our thoughts to you; may your journey be as rewarding as winning gold. Believe in yourself and conquer every challenge!',
        'We thought to remind you that in the game of life, you're a true champion. Keep shining brightly like an Olympic torch!',
        'YThis is us, sending you an Olympic-sized heart-felt encouragement to chase your dreams and reach new heights.',
        'Please receive this, our wish to you; just like an Olympian, you're fuelled by passion and driven by dedication. Keep pushing forward and making your family, friends, and colleagues proud!',
        'Your tech insights are like guiding stars in the digital universe, illuminating paths to innovation and progress. Keep shining bright and leading the way',
        'Your determination in the face of technical challenges is like a force of nature. Your resilience and tenacity propel us forward, overcoming obstacles and achieving greatness.',
        'Just dropping here to whisper this encouragement; may your journey be filled with the same spirit of unity and sportsmanship found in the Olympic Games. Go for gold!',
        
        ]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name +" Welcome to B&M Mission Cascade. "+msg)
