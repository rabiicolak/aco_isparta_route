import random
from data.coordinates import n_cities
from core.matrix_utils import build_distance_matrix


# -----------------------------------------
# Rastgele başlangıç şehri + tüm şehirleri dolaşan rota
# -----------------------------------------
def generate_route(pheromone, heuristic):
    start = random.randint(0, n_cities - 1)
    route = [start]
    visited = {start}

    while len(route) < n_cities:
        current = route[-1]
        probabilities = []

        for next_city in range(n_cities):
            if next_city in visited:
                probabilities.append(0)
            else:
                tau = pheromone[current][next_city]       # feromon
                eta = heuristic[current][next_city]       # bilgi sezgisi
                probabilities.append(tau * (eta ** 2))     # α=1, β=2 varsayımı

        total = sum(probabilities)

        if total == 0:
            # Tüm ihtimaller 0 olursa rastgele seçim
            unvisited = list(set(range(n_cities)) - visited)
            next_city = random.choice(unvisited)
        else:
            probabilities = [p / total for p in probabilities]
            next_city = random.choices(range(n_cities), weights=probabilities)[0]

        route.append(next_city)
        visited.add(next_city)

    return route


# -----------------------------------------
# Rota uzunluğu
# -----------------------------------------
def route_distance(route, distance_matrix):
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i + 1]]

    # tura kapat
    total += distance_matrix[route[-1]][route[0]]
    return total


# -----------------------------------------
# Feromon güncelleme
# -----------------------------------------
def update_pheromones(pheromone, routes, distances, evaporation_rate=0.5):
    # Buharlaşma
    for i in range(n_cities):
        for j in range(n_cities):
            pheromone[i][j] *= (1 - evaporation_rate)

    # Her karınca feromon bırakıyor
    for route, dist in zip(routes, distances):
        deposit = 1 / dist
        for k in range(len(route) - 1):
            a = route[k]
            b = route[k + 1]
            pheromone[a][b] += deposit
            pheromone[b][a] += deposit

        # rotayı kapat
        pheromone[route[-1]][route[0]] += deposit

    return pheromone


# -----------------------------------------
# ANA ACO ALGORİTMASI
# -----------------------------------------
def run_aco(api_key=None, num_ants=10, num_iterations=50):
    distance_matrix = build_distance_matrix(api_key)

    # feromon başlangıç matrisi
    pheromone = [[1 for _ in range(n_cities)] for _ in range(n_cities)]

    # heuristic = 1 / mesafe
    heuristic = [
        [
            (1 / distance_matrix[i][j]) if distance_matrix[i][j] != 0 else 0
            for j in range(n_cities)
        ]
        for i in range(n_cities)
    ]

    best_route = None
    best_distance = float("inf")
    distance_progress = []

    for iteration in range(num_iterations):
        routes = []
        distances = []

        for _ in range(num_ants):
            route = generate_route(pheromone, heuristic)
            d = route_distance(route, distance_matrix)

            routes.append(route)
            distances.append(d)

        # en iyi rota
        min_d = min(distances)
        min_r = routes[distances.index(min_d)]

        if min_d < best_distance:
            best_distance = min_d
            best_route = min_r

        distance_progress.append(best_distance)

        pheromone = update_pheromones(pheromone, routes, distances)

    return best_route, best_distance, distance_progress, distance_matrix
