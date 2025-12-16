import streamlit as st
import pandas as pd

from data.coordinates import locations
from core.matrix_utils import build_distance_matrix
from core.ant_algorithm import run_aco
from core.visual.plotting import plot_convergence
from core.visual.map_plotting import plot_route_on_map
from streamlit_folium import st_folium


# ----------------------------------------
# Streamlit Sayfa Ayarları
# ----------------------------------------
st.set_page_config(
    page_title="Isparta Drone ACO Optimizasyonu",
    layout="wide"
)

st.title("🚁 Isparta Acil Durum Drone Rota Optimizasyonu (ACO)")
st.write(
    "Google Maps API ile alınan gerçek yol mesafeleri kullanılarak "
    "Karınca Kolonisi Algoritması (ACO) ile en kısa rota hesaplanır."
)

# ----------------------------------------
# API KEY
# ----------------------------------------
api_key = st.secrets["GOOGLE_MAPS_API_KEY"]

# ----------------------------------------
# Session State (sonuçları saklamak için)
# ----------------------------------------
if "result" not in st.session_state:
    st.session_state.result = None
if "distance_matrix" not in st.session_state:
    st.session_state.distance_matrix = None

# ----------------------------------------
# Sidebar – ACO Parametreleri
# ----------------------------------------
st.sidebar.header("ACO Parametreleri")


num_ants = st.sidebar.slider(
    "Karınca Sayısı",
    min_value=5,
    max_value=50,
    value=20
)

num_iterations = st.sidebar.slider(
    "İterasyon Sayısı",
    min_value=10,
    max_value=200,
    value=50
)

alpha = st.sidebar.slider(
    "Alpha (Feromon Etkisi)",
    min_value=0.1,
    max_value=5.0,
    value=1.0,
    step=0.1
)

beta = st.sidebar.slider(
    "Beta (Mesafe Etkisi)",
    min_value=0.1,
    max_value=5.0,
    value=2.0,
    step=0.1
)

evaporation = st.sidebar.slider(
    "Buharlaşma Oranı (ρ)",
    min_value=0.1,
    max_value=1.0,
    value=0.5,
    step=0.05
)

# ----------------------------------------
# Optimizasyonu Başlat
# ----------------------------------------
if st.button("🚀 Optimizasyonu Başlat"):

    with st.spinner("🌍 Google Maps API ile mesafe matrisi oluşturuluyor..."):
        distance_matrix = build_distance_matrix(api_key)

    best_route, best_distance, distance_progress = run_aco(
    distance_matrix,
    num_ants=num_ants,
    num_iterations=num_iterations,
    alpha=alpha,
    beta=beta,
    evaporation=evaporation
)


    st.session_state.distance_matrix = distance_matrix
    st.session_state.result = {
        "best_route": best_route,
        "best_distance": best_distance,
        "progress": distance_progress
    }

# ----------------------------------------
# Sonuçları Göster
# ----------------------------------------
if st.session_state.result is not None:

    best_route = st.session_state.result["best_route"]
    best_distance = st.session_state.result["best_distance"]
    progress = st.session_state.result["progress"]
    distance_matrix = st.session_state.distance_matrix

    # ---- İyileşme Oranı ----
    initial_distance = progress[0]
    improvement_rate = (
        (initial_distance - best_distance) / initial_distance
    ) * 100

    # ----------------------------------------
    # Özet Bilgiler (Kart Mantığı)
    # ----------------------------------------
    colA, colB, colC = st.columns(3)

    with colA:
        st.success(f"🧭 En İyi Mesafe\n\n**{best_distance:.3f} km**")

    with colB:
        st.info(f"📉 İyileşme Oranı\n\n**%{improvement_rate:.2f}**")

    with colC:
        st.warning(f"📍 Durak Sayısı\n\n**{len(best_route)}**")

    # ----------------------------------------
    # Rota Metni (İsimlerle)
    # ----------------------------------------
    route_names = [locations[i]["name"] for i in best_route]
    route_names.append(route_names[0])

    st.markdown(
        "**🧭 En İyi Rota:**  \n" + " → ".join(route_names)
    )

    # ----------------------------------------
    # Harita & Yakınsama Grafiği (Yan Yana)
    # ----------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🗺️ En İyi Drone Rotası (Kuş Uçuşu)")
        route_map = plot_route_on_map(best_route, locations)
        st_folium(route_map, width=600, height=450)

    with col2:
        st.subheader("📈 ACO Yakınsama Grafiği")
        st.pyplot(plot_convergence(progress))

    # ----------------------------------------
    # Detaylı Rota Tablosu
    # ----------------------------------------
    st.subheader("📋 Detaylı Rota Tablosu")

    table_data = []

    for i in range(len(best_route)):
        current_idx = best_route[i]
        next_idx = best_route[(i + 1) % len(best_route)]

        table_data.append({
            "Sıra": i + 1,
            "Mevcut Durak": locations[current_idx]["name"],
            "Sonraki Durak": locations[next_idx]["name"],
            "Mesafe (km)": round(
                distance_matrix[current_idx][next_idx], 4
            )
        })

    df = pd.DataFrame(table_data)
    st.dataframe(df, use_container_width=True)

else:
    st.info("Sol taraftan parametreleri ayarlayıp **Optimizasyonu Başlat** butonuna tıklayın.")
