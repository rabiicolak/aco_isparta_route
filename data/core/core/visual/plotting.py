import matplotlib.pyplot as plt

# ---------------------------------------------
# Rota çizimi (lokasyonlar haritada sıralı çizilir)
# ---------------------------------------------
def plot_route(route, locations):
    xs = [locations[i]["lng"] for i in route] + [locations[route[0]]["lng"]]
    ys = [locations[i]["lat"] for i in route] + [locations[route[0]]["lat"]]

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot(xs, ys, marker="o", color="blue")

    for i in range(len(route)):
        x = locations[route[i]]["lng"]
        y = locations[route[i]]["lat"]
        ax.text(x, y, locations[route[i]]["name"], fontsize=9)

    ax.set_xlabel("Boylam")
    ax.set_ylabel("Enlem")
    ax.set_title("ACO - En İyi Drone Rota Çizimi")
    ax.grid(True)
    fig.tight_layout()

    return fig


# ---------------------------------------------
# Convergence grafiği
# ---------------------------------------------
def plot_convergence(progress):
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(progress, marker="o")
    ax.set_xlabel("Iterasyon")
    ax.set_ylabel("En İyi Mesafe")
    ax.set_title("ACO Convergence Grafiği")
    ax.grid(True)
    fig.tight_layout()

    return fig
