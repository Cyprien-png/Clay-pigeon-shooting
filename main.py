import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation


class Projectile :
    def __init__(self, speed, delay, distance, height, angle):
        self.speed = speed # m/s
        self.delay = delay # s
        self.distance = distance # m
        self.height = height/100 # convert cm to m
        self.angle = angle # °


# Define target properties
target_option = input("Would you like to custom the target throw (yes/no)? (default : no) : ")
if target_option.lower() == "yes" or target_option.lower() == "y" :
    target_angle = float(input("\t What throwing angle do you use in relation to the ground? (in degrees) : "))
    target = Projectile(20, 0, 0, 0, target_angle)
else :
    target = Projectile(20, 0, 0, 0, 60)


# Define shot properties
print("\nWhat about the shot : ")
shot_delay = float(input("\t How long do you wait before shooting? (in seconds) : "))
shot_distance = float(input("\t At what distance from the throwing point do you shoot? (in meters) : "))
shot_height = float(input("\t What size are you? (in centimeters) : "))
shot_angle = float(input("\t What shooting angle do you use in relation to the ground? (in degrees) : "))

shot = Projectile(200, shot_delay, shot_distance, shot_height, shot_angle)

# Number of decimals considered during the check.
precision = int(input("\t What level of precision do you want (1-5)? (where the highest is the hardest) : "))

slow_motion = input("\nWould you like to see the simulation in slow motion (yes/no)? (default : no) : ")

gravity = 9.81 # n

# Calculate the time before both function cross eachother on the axes
x_time = (shot.distance - shot.speed * np.cos(np.radians(shot.angle)) * shot.delay - target.distance + target.speed * np.cos(np.radians(target.angle)) * target.delay) / (target.speed * np.cos(np.radians(target.angle)) - shot.speed * np.cos(np.radians(shot.angle)))

# Calculate delta
A = (-0.5 * gravity)
B = (target.speed * np.sin(np.radians(target.angle)) + gravity * target.delay - shot.speed * np.sin(np.radians(shot.angle)))
C = (target.height - shot.height - (target.speed * np.sin(np.radians(target.angle)) * target.delay) - (0.5 * gravity * (target.delay ** 2)) + (shot.speed * np.sin(np.radians(shot.angle)) * shot.delay))

y_delta = B ** 2 - 4 * A * C

# Time array for the animation
if slow_motion.lower() == "yes" or slow_motion.lower() == "y" :
    time = np.linspace(0, 4, 6000)
else :
    time = np.linspace(0, 4, 1000)

# Calculate x and y positions for target and shot
x_target = target.distance + target.speed * np.cos(np.radians(target.angle)) * (time - target.delay)
y_target = target.height + target.speed * np.sin(np.radians(target.angle)) * (time - target.delay) - 0.5 * gravity * (time - target.delay) ** 2

x_shot = shot.distance + shot.speed * np.cos(np.radians(shot.angle)) * (time - shot.delay)
y_shot = shot.height + shot.speed * np.sin(np.radians(shot.angle)) * (time - shot.delay) 




def calculer_y_target(x_target, target, gravity):
    t = (x_target - target.distance) / (target.speed * np.cos(np.radians(target.angle))) + target.delay
    
    y_target = (
        target.height
        + target.speed * np.sin(np.radians(target.angle)) * (t - target.delay)
        - 0.5 * gravity * (t - target.delay) ** 2
    )
    
    return y_target


(target.speed * np.cos(np.radians(target.angle)) + target.distance)

def test(target, gravity):
    # Coefficients for the quadratic equation
    A = -0.5 * gravity
    B = target.speed * np.sin(np.radians(target.angle))
    C = target.height

    # Calculate the discriminant
    Ddelta = B**2 - 4 * A * C

    if Ddelta < 0:
        print("The target never hits the ground.")
    else:
        # Calculate the time when the target hits the ground
        t1 = (-B + math.sqrt(Ddelta)) / (2 * A)
        t2 = (-B - math.sqrt(Ddelta)) / (2 * A)

        # Choose the positive solution
        t = max(t1, t2)

        # Calculate the x position when the target hits the ground
        return target.distance + target.speed * np.cos(np.radians(target.angle)) * max(t1, t2)
    

def getMaxHeigth(target, gravity):
    return ((target.speed * np.sin(np.radians(target.angle))) ** 2)/(2 * gravity)



# Initialize the plot on the simu
fig, ax = plt.subplots()
ax.set_xlim(0, test(target, gravity))
ax.set_ylim(0, getMaxHeigth(target, gravity) + getMaxHeigth(target, gravity)/20)
target, = ax.plot([], [], linestyle='-', marker='', label='Target')  # Connect points with lines
shot, = ax.plot([], [], linestyle='-', marker='', label='Shot')

fig.canvas.manager.set_window_title('Clay pigeon shooting')



# Update function for animation
def update(frame):
    target.set_data(x_target[:frame], y_target[:frame])
    shot.set_data(x_shot[:frame], y_shot[:frame])

    return target, shot

# Set up the animation
ani = FuncAnimation(fig, update, frames=len(time), blit=True, interval=1/10)

result_message = "Too bad... Try again!"

# Calculate if the shot hit the target
if x_time >= 0 : # they hit eachother on x axis
    if  y_delta == 0 :
        if round(x_time, precision) == round((-B + math.sqrt(y_delta)) / (2 * A), precision) : 
            result_message = "Nicely done, right on target!"
      
    elif  y_delta > 0 : 

        print("\n\n\n", x_time)
        print("-------------------")
        print((-B + math.sqrt(y_delta)) / (2 * A))
        print((-B - math.sqrt(y_delta)) / (2 * A))

        if round(x_time, precision) == round((-B + math.sqrt(y_delta)) / (2 * A), precision) or round(x_time, precision) == round((-B - math.sqrt(y_delta)) / (2 * A), precision) :
            result_message = "Nicely done, right on target!"

# Run the simulation
plt.legend()
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title(result_message)
plt.show()
