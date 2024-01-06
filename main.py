import matplotlib.pyplot as plt
import numpy as np
import math
from tkinter import *
from tkinter import ttk
from matplotlib.animation import FuncAnimation


class Projectile :
    def __init__(self, speed, delay, distance, height, angle):
        self.speed = speed # m/s
        self.delay = delay # s
        self.distance = distance # m
        self.height = height # m
        self.angle = angle # °


# Define target properties
target = Projectile(20, 0, 0, 0, 60)

# Define shot properties
shot_delay = int(input("How long do you wait before shooting? (in seconds) : "))
shot_distance = int(input("At what distance from the throwing point do you shoot? (in meters) : "))
shot_height = int(input("What size are you? (in centimeters) : "))
shot_angle = int(input("What shooting angle do you use in relation to the ground? (in degrees) : "))

shot = Projectile(200, shot_delay, shot_distance, shot_height, shot_angle)

# Number of decimals considered during the check.
precision = int(input("What degree of precision do you want? (1-5, where the highest is the hardest) : "))

gravity = 9.81 # n

# Convert cm to m
shot.height = shot.height/100


# Calculate the time before both function cross eachother on the axes
x_time = (shot.distance - shot.speed * np.cos(np.radians(shot.angle)) * shot.delay - target.distance + target.speed * np.cos(np.radians(target.angle)) * target.delay) / (target.speed * np.cos(np.radians(target.angle)) - shot.speed * np.cos(np.radians(shot.angle)))

# Calculate delta
A = (-0.5 * gravity)
B = (target.speed * np.sin(np.radians(target.angle)) + gravity * target.delay - shot.speed * np.sin(np.radians(shot.angle)))
C = (target.height - shot.height - (target.speed * np.sin(np.radians(target.angle)) * target.delay) - (0.5 * gravity * (target.delay ** 2)) + (shot.speed * np.sin(np.radians(shot.angle)) * shot.delay))

y_delta = B ** 2 - 4 * A * C


time = np.linspace(0, 4, 1000)  # Time array for the animation

# Calculate x and y positions for target and shot
x_target = target.distance + target.speed * np.cos(np.radians(target.angle)) * (time - target.delay)
y_target = target.height + target.speed * np.sin(np.radians(target.angle)) * (time - target.delay) - 0.5 * gravity * (time - target.delay) ** 2

x_shot = shot.distance + shot.speed * np.cos(np.radians(shot.angle)) * (time - shot.delay)
y_shot = shot.height + shot.speed * np.sin(np.radians(shot.angle)) * (time - shot.delay) 


# Initialize the plot on the simu
fig, ax = plt.subplots()
ax.set_xlim(0, 40)
ax.set_ylim(0, 20)
target, = ax.plot([], [], linestyle='-', marker='', label='Target')  # Connect points with lines
shot, = ax.plot([], [], linestyle='-', marker='', label='Shot')

# Update function for animation
def update(frame):
    target.set_data(x_target[:frame], y_target[:frame])
    shot.set_data(x_shot[:frame], y_shot[:frame])

    return target, shot

# Set up the animation
ani = FuncAnimation(fig, update, frames=len(time), blit=True, interval=1/10)


# Congrat the player
root = Tk()
root.title('Projectile Motion')
frm = ttk.Frame(root, padding=20)
frm.grid()

# Calculate if the shot hit the target
if x_time >= 0 : # they hit eachother on x axis
    if y_delta < 0 :
        ttk.Label(frm, text="Too bad... Try again!").grid(column=0, row=0)

    elif  y_delta == 0 :
        if round(x_time, precision) == round((-B + math.sqrt(y_delta)) / (2 * A), precision) : 
            ttk.Label(frm, text="Nicely done, right on target!").grid(column=0, row=0)
        else :
            ttk.Label(frm, text="Too bad... Try again!").grid(column=0, row=0)
    
    else : 
        if round(x_time, precision) == round((-B + math.sqrt(y_delta)) / (2 * A), precision) or round(x_time, precision) == round((-B - math.sqrt(y_delta)) / (2 * A), precision) :
            ttk.Label(frm, text="Nicely done, right on target!").grid(column=0, row=0)
        else :
            ttk.Label(frm, text="Too bad... Try again!").grid(column=0, row=0)

else :
    ttk.Label(frm, text="Too bad... Try again!").grid(column=0, row=0)


# Run the simulation
plt.legend()
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Motion')
plt.show()
