import streamlit as st
import numpy as np
from data.coordinates import locations, n_cities
from core.matrix_utils import build_distance_matrix
from core.ant_algorithm import ACO
from visual.plotting import plot_route_image

st.set_page_config(page_title="Isparta Drone ACO Optimizasyonu", layout="wide")

st.title("🚁 Isparta Acil Durum Drone Rota Optimizasyonu (ACO)")
st.write("Karınca Kolonisi Algoritması kullanılarak en kısa rota hesaplanır.")

# --- Kullanıcıdan parametreler ---
st.sidebar.header("ACO Parametreleri")

num_ants = st.sidebar.slider("Karınca Sayısı", min_value=5, max_value=50, value=20)
iterations = st.sidebar.slider("İterasyon Sayısı", min_value=10, max_value=200, value=50)
alpha = st.sidebar.slider("α (Feromon Etkisi)", min_value=0.5, max_value=5.0, value=1.0)
beta = st.sidebar.slider("β (Mesafe Etkisi)", min_value=0.5, max_value=5.0, value=2.0)
rho = st.sidebar.slider("Buharlaşma Oranı (ρ)", min_value=0.1, max_value=1.0, value=0.5)

# --- Mesafe matrisi ---
distance_matrix = build_distance_matrix()

# --- ACO Başlat ---
aco = ACO(
    distance_matrix=distance_matrix,
    num_ants=num_ants,
    num_iterations=iterations,
    alpha=alpha,
    beta=beta,
    evaporation_rate=rho
)

# --- Çalıştır Butonu ---
if st.button("🚀 Optimizasyonu Başlat"):
    best_route, best_distance, distance_progress = aco.run()

    st.success(f"**En İyi Mesafe:** {best_distance:.3f} km")
    st.write("**En iyi rota:**", best_route)

    # Grafik göster
    st.line_chart(distance_progress)

    # Harita görüntüsü üret
    fig = plot_route_image(best_route, locations)
    st.pyplot(fig)

else:
    st.info("Sol taraftan parametreleri ayarlayın ve 'Optimizasyonu Başlat' butonuna tıklayın.")
