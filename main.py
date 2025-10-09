import random
import csv
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_radar_data(num_points=10):
    data = []
    for _ in range(num_points):
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        z = random.uniform(0, 50)
        speed = random.uniform(0, 300)
        noise = lambda: random.uniform(-2, 2)
        data.append([x + noise(), y + noise(), z + noise(), speed + noise()])
    return data

def update_targets(data, dt=1):
    new_data = []
    for x, y, z, speed in data:
        angle = random.uniform(0, 2 * math.pi)
        x_new = x + speed * math.cos(angle) * dt / 10
        y_new = y + speed * math.sin(angle) * dt / 10
        new_data.append([x_new, y_new, z, speed])
    return new_data

def save_to_csv(data, filename="radar_data.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["X", "Y", "Z", "Speed"])
        writer.writerows(data)
    print(f"Data saved to {filename}")

def print_table(data):
    print(f"{'X':>8} {'Y':>8} {'Z':>6} {'Speed':>8}")
    print("-" * 34)
    for x, y, z, speed in data:
        print(f"{x:8.2f} {y:8.2f} {z:6.2f} {speed:8.2f}")

def plot_3d(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs = [d[0] for d in data]
    ys = [d[1] for d in data]
    zs = [d[2] for d in data]
    speeds = [d[3] for d in data]
    sc = ax.scatter(xs, ys, zs, c=speeds, cmap="viridis", s=50)
    plt.colorbar(sc, label="Speed")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.title("Radar 3D Simulation")
    plt.show()

def main():
    print("🚀 Radar Simulator starting...")

    data = generate_radar_data(10)
    data = update_targets(data, dt=1)
    save_to_csv(data)

    print("\n📊 Radar Data Table:")
    print_table(data)

    plot_3d(data)

if __name__ == "__main__":
    main()
