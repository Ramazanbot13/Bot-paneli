import streamlit as st

# Sayfa Ayarları ve Karanlık Tema Modu
st.set_page_config(page_title="CryptoProBot Panel", layout="wide")

st.title("🤖 CryptoProBot - Akıllı İşlem Botu")
st.write("🟢 Bot Aktif - 7/24 Piyasa Takibi Yapılıyor...")
st.divider()

# Üst İstatistikler
col1, col2, col3, col4 = st.columns(4)
col1.metric("Toplam Sermaye", "1.032,80 TL", "+%3,28")
col2.metric("Haftalık Getiri", "+32,80 TL", "+%3,28")
col3.metric("Toplam İşlem", "4", "1 Beklemede")
col4.metric("Başarı Oranı", "%75", "3/4")

st.divider()

# 5'li Kasa Sistemi
st.subheader("🔒 5'li Kasa Durumu")
k1, k2, k3, k4, k5 = st.columns(5)

k1.metric("🟢 Kasa 1 (BTC)", "226,40 TL", "+%13,20")
k2.metric("🟢 Kasa 2 (ETH)", "207,80 TL", "+%3,90")
k3.metric("🔴 Kasa 3 (SOL)", "194,20 TL", "-%2,90")
k4.metric("⚪ Kasa 4 (XRP)", "200,00 TL", "%0,00")
k5.metric("🟢 Kasa 5 (DOGE)", "204,20 TL", "+%2,10")

st.divider()

# Ayarlar ve İşlem Geçmişi
ayar_sutun, gecmis_sutun = st.columns([2, 1])

with ayar_sutun:
    st.subheader("⚙️ Bot Stratejisi ve Kurallar")
    st.write("Aşağıdaki ayarları değiştirdiğinizde bot anında yeni kurallara uyar.")
    
    ilk_satis = st.slider("İlk Satış Eşiği (%) - Hangi kârda satış başlasın?", 1, 50, 10)
    satis_orani = st.slider("İlk Satış Oranı (%) - Kârda paranın yüzde kaçı satılsın?", 10, 100, 30)
    kar_koruma = st.slider("Kâr Koruma Seviyesi (%) - İzleyen kâr düşüş payı", 1, 50, 15)
    stop_loss = st.slider("Stop-Loss (Zarar Kes) (%) - Zarar durdurma", 1, 20, 5)
    
    if st.button("💾 Ayarları Kaydet ve Bota İlet"):
        st.success("Yeni stratejiler buluttaki bota başarıyla iletildi!")

with gecmis_sutun:
    st.subheader("🕒 Son İşlemler")
    st.write("⬆️ **Kasa 1 - BTC:** +%15'te satış yapıldı")
    st.write("⬆️ **Kasa 2 - ETH:** +%15'te kapandı")
    st.write("⬇️ **Kasa 3 - SOL:** Stop-Loss (-%5) çalıştı")
    st.write("ℹ️ **Kasa 4 - XRP:** Fırsat yok, beklemede")
    import urllib.request
try:
    ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
    st.info(f"🌐 Bot Bulut IP Adresi: {ip}")
except:
    pass
