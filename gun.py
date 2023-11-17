import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
m = 0.01  # mass of the bullet in kg
k = 0.01  # air resistance constant in kg/s
g = 9.81  # acceleration due to gravity in m/s^2
v0 = 100  # initial velocity in m/s
h = 1     # initial height in m
dt = 0.01 # time step in s

# Angle of shooting
angles = [ math.radians(90), -math.pi, math.pi, math.radians(120), math.radians(40)]  # angles in radians

plots = []
for theta in angles:
    # Initialize variables
    x = 0     # horizontal position
    y = h     # vertical position
    vx = v0 * math.cos(theta)  # horizontal component of velocity
    vy = v0 * math.sin(theta)  # vertical component of velocity

    # Lists to store trajectory data
    xs = [x]
    ys = [y]

    # Euler method
    while y > 0:
        vx = vx - (k/m)*vx*dt
        vy = vy - (k/m)*vy*dt - g*dt
        x = x + vx*dt
        y = y + vy*dt/2
        xs.append(x)
        ys.append(y)

    plots.append({"x": xs, "y": ys, "theta": theta})

# Plotting the trajectory
plt.figure(figsize=(10,50))
for plot in plots:
    xs = plot["x"]
    ys = plot["y"]
    theta = plot["theta"]
    plt.plot(xs, ys, label=("theta " + str(theta)))
    plt.legend()
plt.title('Trajectory of a Bullet')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.show()
