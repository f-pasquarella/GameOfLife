import streamlit as st
import numpy as np
from scipy.signal import convolve2d
import time
from PIL import Image

st.write(f"""
    # Welcome to the Game of Life! 👋
    """)
st.header('Cellular automaton devised by the British mathematician John Horton Conway')
st.markdown('2020 Copyright  ©Fabio Pasquarella')
st.write('____')


#il prodotto di convoluzione secondo l'opzione 'same', fa scorrere il centro del kernel su ogni numero di table e calcola la somma dei rispettivi prodotti, così abbiamo come output la matrice dei neighbors

SIZE = 40,40
kernel = np.array([[1,1,1],[1,0,1],[1,1,1]]).astype(np.uint8) # il kernel per il prodotto di convoluzione
signal=True


if st.sidebar.button("Start",key='1'):

    table = np.random.randint(0, 2, size=SIZE).astype(np.uint8) # disponiamo le cellule random

    with st.empty():

        while signal:
            next_table = table.copy()
            neighbors = convolve2d(table, kernel, 'same')
            next_table[neighbors < 2] = 0 # morte (se è 2 rimane invariato)
            next_table[neighbors > 3] = 0 # morte
            next_table[(neighbors == 3) & (table == 0)] = 1 # nascita (se è 3 rimane invariato)
            table = next_table


            table_im=np.repeat(table, 20, axis=1)
            table_im=np.repeat(table_im, 20, axis=0)
            im = Image.fromarray(table_im * 255)
            st.image(im,width=800)

            time.sleep(.30)

if st.sidebar.button("Stop",key='2'):
    signal=False
