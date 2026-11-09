import streamlit as st
from binance.client import Client
import urllib.request

# Sayfa Ayarları ve Tema
st.set_page_config(page_title="CryptoProBot", page_icon="🤖")
st.title("🤖 CryptoProBot - Akıllı İşlem Botu")
st.divider()

# IP Adresini Göster
try:
    ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
    st.info(f"🌐 Bot Bulut IP Adresi: {ip}")
except:
    pass

st.write("🔄 Binance bağlantısı kuruluyor...")

# Binance'e Bağlanma ve Veri Çekme Aşaması
try:
    # 1. Şifreleri gizli kasadan (secrets) al
    api_key = st.secrets["BINANCE_API_KEY"]
    api_secret = st.secrets["BINANCE_SECRET_KEY"]

    # 2. Binance Client (Bot) oluştur
    client = Client(api_key, api_secret)

    # 3. Hesap bilgilerini çek
    account = client.get_account()
    balances = account['balances']

    st.success("✅ Binance Hesabınıza Başarıyla Bağlandı!")
    st.subheader("💼 Gerçek Cüzdan Bakiyeniz")

    # Sadece içinde para olan (0'dan büyük) coinleri yan yana kutular halinde göster
    cols = st.columns(3)
    kutu_sirasi = 0

    for b in balances:
        toplam_miktar = float(b['free']) + float(b['locked'])
        if toplam_miktar > 0:
            with cols[kutu_sirasi % 3]:
                st.metric(label=f"{b['asset']} (Coin)", value=f"{toplam_miktar:.4f}")
            kutu_sirasi += 1

    if kutu_sirasi == 0:
        st.warning("Cüzdanınızda şu an hiç coin veya bakiye görünmüyor.")

except Exception as e:
    st.error("Bağlantı kurulamadı. Gizli kasadaki şifreleri veya Binance API izinlerini kontrol edin.")
    st.write(f"Hata detayı: {e}")
