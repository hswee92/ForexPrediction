# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from github import Github
import pytz

import time
import warnings

# warnings.simplefilter('ignore')

# define functions

@st.cache_data
def plot_graph(df,df_pred=pd.DataFrame()):
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10,5))
    ax.plot(df['Date_timestamp'],df['Close'],label="Historical",color=plotcolor) # marker='x' marker='.'

    if radio_forex == "EURUSD":
        df_pred = pd.concat([df.iloc[-2:], df_pred]).reset_index(drop=True)
        ax.plot(df_pred['Date_timestamp'],df_pred['Close'],label="Prediction",color='red',linewidth=2.5)

    ax.set(xlabel='EET Time')  
    ax.set(ylabel='Exchange Rate') 
    plottitle = radio_forex[0:6] + ' Latest Exchange Rate'
    ax.set_title(plottitle)
    ax.set_xlim(df['Date_timestamp'].iloc[0], df_datetime['Date'].iloc[-1]) 
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax.legend()
    st.pyplot(fig)


@st.cache_data
def prediction_table(df):
    df2 = df
    df2['Date'] = df2['Date'].str.slice(11,19)
    df2['Close'] = df2['Close'].round(5)
    df2_set1 = df2[['Date','Close']][0:10]
    df2_set2 = df2[['Date','Close']][10:20]
    df2_set3 = df2[['Date','Close']][20:30]
    st.write(df2_set1.T, key='table1')
    st.write(df2_set2.T, key='table2')
    st.write(df2_set3.T, key='table3')


         
@st.cache_data
def datetime_list(str_date):
    df = pd.DataFrame()
    df['Date'] = pd.date_range(str_date, periods=1440, freq="T")
    return df

st.title('Forex Pair Graphs')

st.sidebar.title("Forex Pair")
radio_forex = st.sidebar.radio("Pick the interested forex pair.", ["EURUSD", "GBPUSD**", "USDJPY**"], key='forex')
st.sidebar.write("** Prediction not available.")

st.write("Hello! Welcome to Forex Prediction page!")

if radio_forex == "EURUSD":
    st.write("this is EURUSD")
    hist_file = radio_forex[0:6] + "_historical.txt"
    plotcolor = 'royalblue'

    pred_file = radio_forex[0:6] + "_prediction.txt"
    df_pred = pd.read_csv(pred_file, delimiter=',', index_col=False)
    df_pred['Date_timestamp'] = pd.to_datetime(df_pred['Date'])

elif radio_forex == "GBPUSD**":
    st.write("this is GBPUSD")
    # hist_file = radio_forex[0:6] + "_historical.txt"
    plotcolor = 'salmon'
         
elif radio_forex == "USDJPY**":
    st.write("this is USDJPY")
    # hist_file = radio_forex[0:6] + "_historical.txt"
    plotcolor = 'forestgreen'

hist_file = radio_forex[0:6] + "_historical.txt"
df = pd.read_csv(hist_file, delimiter=',', index_col=False)
df['Date_timestamp'] = pd.to_datetime(df['Date'])

# Prepare for plot
str_datetime = df['Date'].iloc[0]
str_date = str_datetime[0:10]

df_datetime = datetime_list(str_date)
if radio_forex == "EURUSD":
    plot_graph(df,df_pred)
    prediction_table(df_pred)
else:
    plot_graph(df)
    del st.session_state['table1']
    del st.session_state['table2']
    del st.session_state['table3']
    


# container for information below
container = st.container(border=True)
MT4_timezone = pytz.timezone('EET') 
MT4_now = datetime.now(MT4_timezone)
str_MT4 = MT4_now.strftime("%d-%m-%Y %H:%M:%S")
container.write("**Server time:** " + str_MT4)

local_timezone = pytz.timezone('Asia/Kuala_Lumpur') 
local_now = datetime.now(local_timezone)
str_local = local_now.strftime("%d-%m-%Y %H:%M:%S")
container.write("**Malaysia time:** "+  str_local)

container.write("**:red[Disclaimer: Trading involves risk. \n"
                "As a general rule, you should only trade in financial products that "
                "you are familiar with and understand the risk associated with them. \n"
                "Trade at your own risk.]**", key='disclaimer')

# st.write("st.session_state")
# st.session_state

time.sleep(5)
st.rerun()




