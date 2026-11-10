import os
import streamlit as st
from binance.client import Client

st.title("📈 Binance Spot & Bakiye Takip Botu")

# API anahtarlarını al
api_key = os.getenv("BINANCE_API_KEY") or st.secrets.get("BINANCE_API_KEY", "")
api_secret = os.getenv("BINANCE_SECRET_KEY") or st.secrets.get("BINANCE_SECRET_KEY", "")

if not api_key or not api_secret:
    st.error("Lütfen Binance API anahtarlarınızı Environment Variables kısmına ekleyin!")
else:
    try:
        client = Client(api_key, api_secret)
        st.success("Binance bağlantısı başarıyla sağlandı!")
        
        # Hesap bilgilerini ve bakiyeleri çek
        account = client.get_account()
        balances = account['balances']
        
        st.subheader("💰 Cüzdan Bakiyeleriniz")
        
        # Sadece bakiyesi 0'dan büyük olan coinleri filtreleyelim ve listeleyelim
        for asset in balances:
            free = float(asset['free'])
            locked = float(asset['locked'])
            if free > 0 or locked > 0:
                st.write(f"**{asset['asset']}**: Serbest: {free} | Kilitli: {locked}")
                
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")
