import matplotlib.pyplot as plt


# ---------------------------------------------
# Rota çizimi (lokasyonlar haritada sıralı çizilir)
# ---------------------------------------------
def plot_route(route, locations):
    xs = [locations[i]["lng"] for i in route] + [locations[route[0]]["lng"]]
    ys = [locations[i]["lat"] for i in route] + [locations[route[0]]["lat"]]

    plt.figure(figsize=(8, 8))
    plt.plot(xs, ys, marker="o", color="blue")

    for i in range(len(route)):
        x = locations[route[i]]["lng"]
        y = locations[route[i]]["lat"]
        plt.text(x, y, locations[route[i]]["name"], fontsize=9)

    plt.xlabel("Boylam")
    plt.ylabel("Enlem")
    plt.title("ACO - En İyi Drone Rota Çizimi")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------
# Convergence grafiği
# ---------------------------------------------
def plot_convergence(progress):
    plt.figure(figsize=(7, 4))
    plt.plot(progress, marker="o")
    plt.xlabel("Iterasyon")
    plt.ylabel("En İyi Mesafe")
    plt.title("ACO Convergence Grafiği")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
