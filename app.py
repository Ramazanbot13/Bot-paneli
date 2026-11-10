import os
import streamlit as st
from binance.client import Client

st.title("📈 Binance Spot & Bakiye Takip Botu")

# API anahtarlarını güvenli bir şekilde alalım
api_key = os.getenv("BINANCE_API_KEY") or st.secrets.get("BINANCE_API_KEY", "")
api_secret = os.getenv("BINANCE_SECRET_KEY") or st.secrets.get("BINANCE_SECRET_KEY", "")

if not api_key or not api_secret:
    st.error("Lütfen Binance API anahtarlarınızı Environment Variables kısmına ekleyin!")
else:
    try:
        # Binance istemcisini başlatalım (Spot test için)
        client = Client(api_key, api_secret)
        
        # Hesap bilgilerini çekelim
        account_info = client.get_account()
        
        st.success("Binance bağlantısı başarıyla sağlandı ve cüzdan okundu!")
        st.subheader("💰 Cüzdan Bakiyeleriniz")
        
        # Bakiyeleri güvenli bir döngüyle ekrana yazdıralım
        balances = account_info.get('balances', [])
        found_balance = False
        
        for asset in balances:
            free = float(asset.get('free', 0))
            locked = float(asset.get('locked', 0))
            
            # Sadece sıfırdan büyük bakiyeleri gösterelim
            if free > 0 or locked > 0:
                st.write(f"🪙 **{asset['asset']}**: Serbest: {free} | Kilitli: {locked}")
                found_balance = True
                
        if not found_balance:
            st.info("Cüzdanınızda şu an sıfırdan büyük bakiye bulunmuyor.")
            
    except Exception as e:
        st.error(f"Bağlantı veya Yetki Hatası: {e}")
