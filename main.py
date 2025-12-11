import streamlit as st
import numpy as np
from data.coordinates import locations, n_cities
from core.matrix_utils import build_distance_matrix
from core.ant_algorithm import run_aco
from core.visual.plotting import plot_route, plot_convergence


# ----------- Streamlit Sayfa Ayarları -----------
st.set_page_config(page_title="Isparta Drone ACO Optimizasyonu", layout="wide")

st.title("🚁 Isparta Acil Durum Drone Rota Optimizasyonu (ACO)")
st.write("Karınca Kolonisi Algoritması kullanılarak en kısa rota hesaplanır.")


# ----------- Kullanıcı Parametreleri -----------
st.sidebar.header("ACO Parametreleri")

num_ants = st.sidebar.slider("Karınca Sayısı", min_value=5, max_value=50, value=20)
iterations = st.sidebar.slider("İterasyon Sayısı", min_value=10, max_value=200, value=50)


# ----------- Optimizasyonu Başlat -----------
if st.button("🚀 Optimizasyonu Başlat"):

    best_route, best_distance, distance_progress, distance_matrix = run_aco(
        api_key=None,
        num_ants=num_ants,
        num_iterations=iterations
    )

    st.success(f"**En İyi Mesafe:** {best_distance:.3f} km")
    st.write("**En iyi rota (şehir indeksleri):**", best_route)


    # ----------- Convergence Grafiği -----------
    st.subheader("📉 ACO Convergence Grafiği")
    fig1 = plot_convergence(distance_progress)
    st.pyplot(fig1)


    # ----------- Rota Haritası -----------
    st.subheader("🗺️ En İyi Rota Harita Çizimi")
    fig2 = plot_route(best_route, locations)
    st.pyplot(fig2)


else:
    st.info("Sol taraftan parametreleri ayarlayıp 'Optimizasyonu Başlat' butonuna tıklayın.")
