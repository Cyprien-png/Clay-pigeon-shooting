import matplotlib.pyplot as plt
import numpy as np
import math
from tkinter import *
from tkinter import ttk
from matplotlib.animation import FuncAnimation


# Define target properties
target_speed = 20 # m/s
target_delay = 0 # s
target_distance = 0 # m
target_height = 0 # m
target_angle = 60 # °

# Define shot properties
shot_speed = 200 # m/s
shot_delay = int(input("Combien de temps attendez-vous avant de tirer ? (en secondes) : "))
shot_distance = int(input("A quelle distance du point de lancer tirez-vous ? (en mètres) : "))
shot_height = int(input("Quelle taille faites-vous ? (en centimètres) : "))
shot_angle = int(input("Quel ange de tir utilisez-vous par rapport au sol ? (en degrés) : "))

# Number of decimals considered during the check.
precision = int(input("Quelle degrès de précision voulez-vous ? : (1-5, le plus grand est le plus dur) : "))

gravity = 9.81 # n

# Convert cm to m
shot_height = shot_height/100


# Calculate the time before both function cross eachother on the axes
x_time = (shot_distance - shot_speed * np.cos(np.radians(shot_angle)) * shot_delay - target_distance + target_speed * np.cos(np.radians(target_angle)) * target_delay) / (target_speed * np.cos(np.radians(target_angle)) - shot_speed * np.cos(np.radians(shot_angle)))

# Calculate delta
A = (-0.5 * gravity)
B = (target_speed * np.sin(np.radians(target_angle)) + gravity * target_delay - shot_speed * np.sin(np.radians(shot_angle)))
C = (target_height - shot_height - (target_speed * np.sin(np.radians(target_angle)) * target_delay) - (0.5 * gravity * (target_delay ** 2)) + (shot_speed * np.sin(np.radians(shot_angle)) * shot_delay))

y_delta = B ** 2 - 4 * A * C


time = np.linspace(0, 4, 1000)  # Time array for the animation

# Calculate x and y positions for target and shot
x_target = target_distance + target_speed * np.cos(np.radians(target_angle)) * (time - target_delay)
y_target = target_height + target_speed * np.sin(np.radians(target_angle)) * (time - target_delay) - 0.5 * gravity * (time - target_delay) ** 2

x_shot = shot_distance + shot_speed * np.cos(np.radians(shot_angle)) * (time - shot_delay)
y_shot = shot_height + shot_speed * np.sin(np.radians(shot_angle)) * (time - shot_delay) 


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
        ttk.Label(frm, text="Dommage... Essayez encore!").grid(column=0, row=0)

    elif  y_delta == 0 :
        if round(x_time, precision) == round((-B + math.sqrt(y_delta)) / (2 * A), precision) : 
            ttk.Label(frm, text="Bien joué, en plein dans le mille!").grid(column=0, row=0)
        else :
            ttk.Label(frm, text="Dommage... Essayez encore!").grid(column=0, row=0)
    
    else : 
        if round(x_time, precision) == round((-B + math.sqrt(y_delta)) / (2 * A), precision) or round(x_time, precision) == round((-B - math.sqrt(y_delta)) / (2 * A), precision) :
            ttk.Label(frm, text="Bien joué, en plein dans le mille!").grid(column=0, row=0)
        else :
            ttk.Label(frm, text="Dommage... Essayez encore!").grid(column=0, row=0)
            
else :
    ttk.Label(frm, text="Dommage... Essayez encore!").grid(column=0, row=0)


# Run the simulation
plt.legend()
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Motion')
plt.show()
