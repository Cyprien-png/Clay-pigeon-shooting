import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation


# Define target properties
target_speed = 20 # m/s
target_delay = 0 # s
target_distance = 0 # m
target_height = 0 # m
target_angle = 60 # °


# Define shot properties
shot_speed = 20 # m/s
shot_delay = int(input("Combien de temps attendez-vous avant de tirer ? (en secondes)"))
shot_distance = int(input("A quelle distance du point de lancez tirez-vous ? (en mètres)"))
shot_height = int(input("Quelle taille faites-vous ? (en centimètres)"))
shot_angle = int(input("Quel ange de tir utilisez-vous par rapport au sol ? (en degrés)"))

gravity = 9.81 # n
time = np.linspace(0, 20, 1000)  # Time array for the animation

# Calculate x and y positions for target and shot
x_target = target_distance + target_speed * np.cos(np.radians(target_angle)) * (time - target_delay)
y_target = target_height + target_speed * np.sin(np.radians(target_angle)) * (time - target_delay) - 0.5 * gravity * (time - target_delay) ** 2

x_shot = shot_distance + shot_speed * np.cos(np.radians(shot_angle)) * (time - shot_delay)
y_shot = shot_height/100 + shot_speed * np.sin(np.radians(shot_angle)) * (time - shot_delay) 

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(0, max(target_distance, shot_distance) + 20)
ax.set_ylim(0, 20)
target, = ax.plot([], [], 'r-', linestyle='-', marker='', label='Target')  # Connect points with lines
shot, = ax.plot([], [], 'bo', linestyle='-', marker='', label='Shot')

# Update function for animation
def update(frame):
    target.set_data(x_target[:frame], y_target[:frame])
    shot.set_data(x_shot[:frame], y_shot[:frame])
    return target, shot

# Set up the animation
ani = FuncAnimation(fig, update, frames=len(time), blit=True, interval=1/10)

plt.legend()
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Motion')
plt.show()
