import csv
import sys
import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from simulation import simulate


def main():
    args = get_args()
    if args.velocity < 0 or args.angle < 0 or args.angle > 90 or args.mass <= 0:
        sys.exit("Error: Invalid physical parameters.")
    history = simulate(args.velocity,args.angle,args.mass,args.drag,args.area,dt=0.01)
    x_coords = [point.x for point in history]
    y_coords = [point.y for point in history]
    write_csv(x_coords,y_coords)
    plot_graph(x_coords,y_coords)
    animate(history,args.velocity,args.angle,args.mass,args.drag,filename="trajectory.gif")
    print(f"Max Height: {get_max_height(history):.2f} m")
    print(f"Landing Position: {get_landing_position(history):.2f} m")
    print("Generated: trajectory.png, trajectory.gif, coordinates.csv")

def get_args():
    parser = argparse.ArgumentParser(prog='Ballistic Trajectory Simulator',
                                     description='Simulates and plots the 2D trajectory of a projectile accounting for gravity and aerodynamic drag')
    parser.add_argument("--velocity", type=float, required=True)
    parser.add_argument("--angle", type=float, required=True)
    parser.add_argument("--mass", type=float, required=True)
    parser.add_argument("--drag", type=float, required=True)
    parser.add_argument("--area", type=float, required=True) 
    return parser.parse_args()

def plot_graph(x_coords,y_coords):
    """
    Generates a png image of the Trajectory of the object, Distance(m) against Height(m)
    """

    plt.plot(x_coords,y_coords)
    plt.title("Trajectory",
            fontsize=20,
            family="Arial",
            fontweight="bold",
            )
    plt.xlabel("Distance (m)",
            fontsize=10,
            family="Arial",
            )
    plt.ylabel("Height (m)",
            fontsize=10,
            family="Arial",
            ) 
    
    plt.savefig("trajectory.png")
    plt.close()

def write_csv(x_coords,y_coords):
    """
    Writes the x & y coordinates to a csv file
    """
    with open("coordinates.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["x", "y"]) 
        for x, y in zip(x_coords, y_coords):
            csvwriter.writerow([round(x, 2), round(y, 2)])

def get_max_height(history):
    return max(p.y for p in history)

def get_landing_position(history):
    return history[-1].x

def animate(history,velocity,angle,mass,drag,filename="trajectory.gif"):
    """
    Generates a gif of the Trajectory of the object
    """
    x = [p.x for p in history]
    y = [p.y for p in history]

    fig, ax = plt.subplots()
    ax.set_xlim(0, max(x) * 1.1)
    ax.set_ylim(0, max(y) * 1.1)
    ax.set_title(f"Launch speed: {velocity}m/s | Angle: {angle}° | Mass: {mass}kg | Cd: {drag}")
    ax.set_xlabel("Distance (m)", fontsize=10, family="Arial")
    ax.set_ylabel("Height (m)", fontsize=10, family="Arial")
    line, = ax.plot([], [])

    def update(i):
        line.set_data(x[:i], y[:i])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=len(x), interval=40)
    ani.save(filename, writer="pillow")
    plt.close()


if __name__ == "__main__":
    main()