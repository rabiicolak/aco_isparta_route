import googlemaps
import numpy as np
from data.coordinates import locations

def build_distance_matrix(api_key):
    gmaps = googlemaps.Client(key=api_key)

    n = len(locations)
    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            origin = (locations[i]["lat"], locations[i]["lng"])
            destination = (locations[j]["lat"], locations[j]["lng"])

            try:
                result = gmaps.distance_matrix(
                    origins=[origin],
                    destinations=[destination],
                    mode="driving"
                )

                element = result["rows"][0]["elements"][0]

                if element["status"] == "OK":
                    distance_m = element["distance"]["value"] / 1000  # metre → km
                else:
                    distance_m = 0  # API sonucu yoksa 0 döner, algoritma yine çalışır.

                matrix[i][j] = distance_m

            except Exception as e:
                print("Google API Hatası:", e)
                matrix[i][j] = 0  # Hata olsa bile algoritmayı durdurmaz.

    return matrix
