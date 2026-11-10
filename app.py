import os
import streamlit as st
from binance.client import Client

# Önce Render Environment Variables'a bakar, yoksa Streamlit Secrets'ı dener
api_key = os.getenv("BINANCE_API_KEY") or st.secrets.get("BINANCE_API_KEY", "")
api_secret = os.getenv("BINANCE_SECRET_KEY") or st.secrets.get("BINANCE_SECRET_KEY", "")

# Eğer anahtarlar boşsa kullanıcıya bilgi verelim
if not api_key or not api_secret:
    st.error("Lütfen Binance API anahtarlarınızı Environment Variables veya Secrets kısmına ekleyin!")
else:
    client = Client(api_key, api_secret)
    st.success("Binance bağlantısı başarıyla sağlandı!")
    
    # Bakiye bilgileri veya bot arayüzü kodlarınız burada devam eder...
