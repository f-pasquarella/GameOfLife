# Fabio Pasquarella
# GNU AFFERO GENERAL PUBLIC LICENSE
# Version 3, 19 November 2007


import streamlit as st
import numpy as np
from scipy.signal import convolve2d
import time
from PIL import Image

my_expander = st.sidebar.beta_expander("Instructions")

my_expander.write("This is the game of life, classified as a universal machine. It means you can implement a Turing machine - someone has already done so. Pressing start random initializes a central area of a 70x70 matrix which is our grid. Outside the borders the values are all zero. The algorithm ends when there is no more life on grid, or when you hit stop. Beware that the system can originate states of equilibrium in which nothing seems to happen, however the algorithm is running. Enjoy!")



st.write(f"""
    # Welcome to the Game of Life! 👋
    """)
st.header('Cellular automaton devised by the British mathematician John Horton Conway')
st.markdown('2020 Fabio Pasquarella - GNU AFFERO GENERAL PUBLIC LICENSE')
st.write('____')


#il prodotto di convoluzione secondo l'opzione 'same', fa scorrere il centro del kernel su ogni numero di table e calcola la somma dei rispettivi prodotti, così abbiamo come output la matrice dei neighbors

SIZE = 70,70
kernel = np.array([[1,1,1],[1,0,1],[1,1,1]]).astype(np.uint8) # il kernel per il prodotto di convoluzione
signal=True
table =np.zeros((SIZE)).astype(np.uint8) # costruiamo la griglia di zero


if st.sidebar.button("Start",key='1'):

    rand=np.random.randint(0, 2, size=[10,10]).astype(np.uint8) # disponiamo le cellule random al centro in un quadrato 10x10
    table[29:39,29:39]=rand  # inseriamo il quadrato nella griglia

    with st.empty():

        while (signal and (not np.all(table==0))):
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
    st.image(table,width=800)
