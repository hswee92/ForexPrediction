# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import requests
from github import Github

import time
import warnings

# warnings.simplefilter('ignore')

initial_state = 0
st.title('Forex Pair Graphs')

st.sidebar.title("Forex Pair")
radio_forex = st.sidebar.radio("Pick the interested forex pair.", ["EURUSD", "GBPUSD**", "USDJPY**"], key='forex')
st.sidebar.write("** Prediction not available.")

st.write("Hello! Welcome to Forex Prediction page!")

if radio_forex == "EURUSD":
         st.write("this is EURUSD")
         hist_file = radio_forex[0:6] + "_historical.txt"
         plotcolor = 'royalblue'
         
         # path = "https://raw.githubusercontent.com/hswee92/ForexPrediction/main/" + hist_file
         # st.write(path)
         # response = requests.get(path)
         # df = pd.read_csv(path, delimiter=',', index_col=False)
         # st.table(df)


elif radio_forex == "GBPUSD**":
         st.write("this is GBPUSD")
         # hist_file = radio_forex[0:6] + "_historical.txt"
         plotcolor = 'salmon'
         
elif radio_forex == "USDJPY**":
         st.write("this is USDJPY")
         # hist_file = radio_forex[0:6] + "_historical.txt"
         plotcolor = 'forest'

hist_file = radio_forex[0:6] + "_historical.txt"
path = "./" + hist_file
df = pd.read_csv(hist_file, delimiter=',', index_col=False)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(24,10))

# Plot
ax.plot(df['Date'],df['Close'],label="silhouette score",,color=plotcolor) # marker='x' marker='.'
ax.set(xlabel='Time')  
ax.set(ylabel='Exchange Rate') 
plottitle = radio_forex[0:6] + 'Latest Exchange Rate'
ax.set_title(plottitle)


st.table(df)



rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)




now = datetime.now()
current_time = now.strftime("%H:%M:%S")
cur_time = "Current Time = " + current_time
st.write(cur_time)


st.write("**:red[Disclaimer: Trading involves risk. \n"
         "As a general rule, you should only trade in financial products that "
         "you are familiar with and understand the risk associated with them. \n"
         "Trade at your own risk.]**")

st.write("st.session_state")
st.session_state

time.sleep(5)
st.rerun()





