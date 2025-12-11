import googlemaps
from math import radians, sin, cos, sqrt, atan2

from data.coordinates import locations, n_cities


# -----------------------------
# Google Distance Matrix API
# -----------------------------
def get_driving_distance(api_key, lat1, lng1, lat2, lng2):
    gmaps = googlemaps.Client(key=api_key)

    result = gmaps.distance_matrix(
        origins=[(lat1, lng1)],
        destinations=[(lat2, lng2)],
        mode="driving",
        units="metric"
    )

    try:
        distance_meters = result["rows"][0]["elements"][0]["distance"]["value"]
        return distance_meters / 1000  # km
    except:
        return None


# -----------------------------
# Haversine (yol alternatifi)
# -----------------------------
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Dünya yarıçapı (km)

    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    a = sin(d_lat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return R * c


# -----------------------------
# Mesafe Matrisini Oluşturma
# -----------------------------
def build_distance_matrix(api_key=None):
    matrix = [[0]*n_cities for _ in range(n_cities)]

    for i in range(n_cities):
        for j in range(n_cities):
            if i == j:
                matrix[i][j] = 0
                continue

            lat1, lng1 = locations[i]["lat"], locations[i]["lng"]
            lat2, lng2 = locations[j]["lat"], locations[j]["lng"]

            # Google API varsa kullan
            if api_key:
                d = get_driving_distance(api_key, lat1, lng1, lat2, lng2)
                if d:
                    matrix[i][j] = d
                    continue

            # API çalışmazsa: Haversine
            matrix[i][j] = haversine(lat1, lng1, lat2, lng2)

    return matrix
