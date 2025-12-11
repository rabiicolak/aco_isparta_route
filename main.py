import streamlit as st
from data.coordinates import locations
from core.matrix_utils import build_distance_matrix
from core.ant_algorithm import run_aco
from core.visual.plotting import plot_route, plot_convergence

# ----------- Streamlit Ayarları -----------
st.set_page_config(page_title="Isparta Drone ACO Optimizasyonu", layout="wide")

st.title("🚁 Isparta Acil Durum Drone Rota Optimizasyonu (ACO)")
st.write("Google Maps API ile alınan gerçek yol mesafeleri kullanılarak en kısa rota hesaplanır.")

# ----------- API KEY -----------
api_key = st.secrets["GOOGLE_MAPS_API_KEY"]

# ----------- Parametreler -----------
st.sidebar.header("ACO Parametreleri")
num_ants = st.sidebar.slider("Karınca Sayısı", 5, 50, 20)
iterations = st.sidebar.slider("İterasyon Sayısı", 10, 200, 50)

# ----------- Optimizasyonu Başlat -----------
if st.button("🚀 Optimizasyonu Başlat"):

    with st.spinner("🌍 Google Maps API ile mesafe matrisi oluşturuluyor..."):
        distance_matrix = build_distance_matrix(api_key)

    best_route, best_distance, distance_progress = run_aco(
        distance_matrix,
        num_ants=num_ants,
        num_iterations=iterations
    )

    st.success(f"**En İyi Mesafe:** {best_distance:.3f} km")
    st.write("**En iyi rota (şehir indeksleri):**", best_route)

    # ---------- Convergence ----------
    st.subheader("📉 ACO Convergence Grafiği")
    st.pyplot(plot_convergence(distance_progress))

    # ---------- Route Visualization ----------
    st.subheader("🗺️ En İyi Rota Harita Çizimi")
    st.pyplot(plot_route(best_route, locations))

else:
    st.info("Sol taraftan parametreleri ayarlayıp 'Optimizasyonu Başlat' butonuna tıklayın.")
