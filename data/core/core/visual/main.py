import streamlit as st
from data.coordinates import locations
from core.matrix_utils import build_distance_matrix
from core.ant_algorithm import run_aco
from visual.plotting import plot_route, plot_convergence
import matplotlib.pyplot as plt


# ----------------------------------------------------
# Streamlit Başlık
# ----------------------------------------------------
st.title("🛰️ ACO ile Isparta Acil Durum Drone Rota Optimizasyonu")
st.write("Genetik Algoritmalar ve Yapay Zeka Sistemleri Projesi - Rabia Çolak")


# ----------------------------------------------------
# Kullanıcıdan Parametre Alma
# ----------------------------------------------------
st.sidebar.header("ACO Parametreleri")

num_ants = st.sidebar.slider("Karınca Sayısı", 5, 50, 20)
num_iterations = st.sidebar.slider("Iterasyon Sayısı", 10, 200, 50)
alpha = st.sidebar.slider("Alpha (feromon etkisi)", 0.1, 5.0, 1.0)
beta = st.sidebar.slider("Beta (mesafe etkisi)", 0.1, 5.0, 2.0)
evaporation = st.sidebar.slider("Buharlaşma Oranı", 0.1, 1.0, 0.5)


# ----------------------------------------------------
# Şehir Listesini Göster
# ----------------------------------------------------
st.subheader("📍 Isparta Acil Toplanma Alanları")
for loc in locations:
    st.write(f"- {loc['name']} (Lat: {loc['lat']}, Lng: {loc['lng']})")


# ----------------------------------------------------
# ACO Hesaplama
# ----------------------------------------------------
if st.button("🚀 En İyi Rotayı Hesapla"):
    st.write("Hesaplanıyor... Lütfen bekleyin.")

    distance_matrix = build_distance_matrix()
    
    best_route, best_distance, progress = run_aco(
        distance_matrix,
        num_ants=num_ants,
        num_iterations=num_iterations,
        alpha=alpha,
        beta=beta,
        evaporation=evaporation
    )

    st.success(f"✨ En iyi rota toplam mesafe: **{best_distance:.3f} km**")
    st.write("📌 En iyi rota:", best_route)


    # ----------------------------------------------------
    # Rota Grafiği
    # ----------------------------------------------------
    st.subheader("📌 En İyi Rota Görselleştirme")

    fig1 = plt.figure(figsize=(6, 6))
    plot_route(best_route, locations)
    st.pyplot(fig1)

    
    # ----------------------------------------------------
    # Convergence Grafiği
    # ----------------------------------------------------
    st.subheader("📈 Convergence Grafiği")

    fig2 = plt.figure(figsize=(6, 4))
    plot_convergence(progress)
    st.pyplot(fig2)
