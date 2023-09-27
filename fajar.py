
import requests
import streamlit as st
from streamlit_lottie import st_lottie



def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets10.lottiefiles.com/packages/lf20_l13zwx3i.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,speed=1,
    reverse=False,
    loop=True,
    key="hello")  

