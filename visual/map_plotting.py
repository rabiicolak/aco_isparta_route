import folium

def plot_route_on_map(route, locations):

    # Harita başlangıç noktası (ilk durak)
    start = locations[route[0]]

    # Haritayı oluştur
    m = folium.Map(
        location=[start["lat"], start["lng"]],
        zoom_start=14
    )

    # Noktaları işaretle
    for i in route:
        loc = locations[i]
        folium.Marker(
            location=[loc["lat"], loc["lng"]],
            popup=loc["name"],
            tooltip=loc["name"]
        ).add_to(m)

    # Drone rotası (kuş uçuşu çizgi)
    path = []
    for i in route:
        path.append((locations[i]["lat"], locations[i]["lng"]))

    # Başlangıca geri dön
    path.append((start["lat"], start["lng"]))

    folium.PolyLine(
        path,
        color="red",
        weight=4
    ).add_to(m)

    return m
