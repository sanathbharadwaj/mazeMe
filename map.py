# Self Driving Car

# Importing the libraries
import numpy as np
from random import random, randint
#import matplotlib.pyplot as plt
import time


# Importing the Kivy packages
# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.button import Button
# from kivy.graphics import Color, Ellipse, Line
# from kivy.config import Config
# from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
# from kivy.vector import Vector
#from kivy.clock import Clock

# Importing the Dqn object from our AI in ai.py
from ai import Dqn

# Adding this line if we don't want the right click to put a red point
# Introducing last_x and last_y, used to keep the last point in memory when we draw the sand on the map
last_x = 0
last_y = 0
n_points = 0
length = 0

# Getting our AI, which we call "brain", and that contains our neural network that represents our Q-function
brain = Dqn(5,3,0.9)
action2rotation = [0,20,-20]
last_reward = 0
scores = []

# Initializing the map
first_update = True
def init():
    global sand
    ###global goal_x
    ###global goal_y
    ###global first_update
    #sand = np.zeros((longueur,largeur))
    ###goal_x = 20
    ###goal_y = largeur - 20
    first_update = False

# Initializing the last distance
###last_distance = 0

# Creating the car class

class Car(Widget):
    
    angle = 0
    rotation = 0
    velocity_x = 0
    velocity_y = 0
    velocity = 0#
    sensor1_x = 0
    sensor1_y = 0
    sensor1 = 0
    sensor2_x = 0
    sensor2_y = 0
    sensor2 = 0
    sensor3_x = 0
    sensor3_y = 0
    sensor3 = 0
    signal1 = 0
    signal2 = 0
    signal3 = 0

    def __init__(self):
        self.signal1 = 0
        self.signal2 = 0
        self.signal3 = 0

    def move(self, action):
        #self.pos = Vector(*self.velocity) + self.pos
        #self.rotation = rotation
        #self.angle = self.angle + self.rotation
        #self.sensor1 = Vector(30, 0).rotate(self.angle) + self.pos
        #self.sensor2 = Vector(30, 0).rotate((self.angle+30)%360) + self.pos
        #self.sensor3 = Vector(30, 0).rotate((self.angle-30)%360) + self.pos
        #self.signal1 = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.
        #self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        #self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400.
        # if self.sensor1_x>longueur-10 or self.sensor1_x<10 or self.sensor1_y>largeur-10 or self.sensor1_y<10:
        #     self.signal1 = 1.
        # if self.sensor2_x>longueur-10 or self.sensor2_x<10 or self.sensor2_y>largeur-10 or self.sensor2_y<10:
        #     self.signal2 = 1.
        # if self.sensor3_x>longueur-10 or self.sensor3_x<10 or self.sensor3_y>largeur-10 or self.sensor3_y<10:
        #     self.signal3 = 1.
        if action==0:
            moveForward()
        if action == 1:
            turn(1)
        if action == 2:
            turn(2) 



# Creating the game class

class Game():

    ###car = ObjectProperty(None)
   # ball1 = ObjectProperty(None)
    #ball2 = ObjectProperty(None)
    #ball3 = ObjectProperty(None)

    def __init__(self):
        self.car = Car()

    #def serve_car(self):
        #self.car.center = self.center
        #self.car.velocity = Vector(6, 0)

    def update(self, dt):

        global brain
        global last_reward
        global scores
        ###global last_distance
        global goal_x
        global goal_y
        global longueur
        global largeur

        # longueur = self.width
        # largeur = self.height
        if first_update:
            init()

        #xx = goal_x - self.car.x
        #yy = goal_y - self.car.y
        orientation = getRotation()
        self.car.signal1 = getSensor(1)
        self.car.signal2 = getSensor(2)
        self.car.signal3 = getSensor(3)

        last_signal = [self.car.signal1, self.car.signal2, self.car.signal3, orientation, -orientation]
        action = brain.update(last_reward, last_signal)
        ###scores.append(brain.score())
        #rotation = action2rotation[action]
        self.car.move(action)
        #distance = np.sqrt((self.car.x - goal_x)**2 + (self.car.y - goal_y)**2)
        ###self.ball1.pos = self.car.sensor1
        #self.ball2.pos = self.car.sensor2
        #self.ball3.pos = self.car.sensor3
        
        md = 5
        if getSensor(1) < md or getSensor(2) < md or getSensor(3) < md:
            #self.car.velocity = Vector(1, 0).rotate(self.car.angle)
            last_reward = -1
        else: # otherwise
            #self.car.velocity = Vector(6, 0).rotate(self.car.angle)
            last_reward = -0.1
            #if distance < last_distance:
                #last_reward = 0.1

        # if self.car.x < 10:
        #     self.car.x = 10
        #     last_reward = -1
        # if self.car.x > self.width - 10:
        #     self.car.x = self.width - 10
        #     last_reward = -1
        # if self.car.y < 10:
        #     self.car.y = 10
        #     last_reward = -1
        # if self.car.y > self.height - 10:
        #     self.car.y = self.height - 10
        #     last_reward = -1
            
        if orientation > 0.3 or orientation < -0.3:
            last_reward -= 0.1
            
        if last_reward < -1:
            last_reward = -1;

        # if distance < 100:
        #     goal_x = self.width-goal_x
        #     goal_y = self.height-goal_y
        # last_distance = distance

# Adding the painting tools

# class MyPaintWidget(Widget):

#     def on_touch_down(self, touch):
#         global length, n_points, last_x, last_y
#         with self.canvas:
#             Color(0.8,0.7,0)
#             d = 10.
#             touch.ud['line'] = Line(points = (touch.x, touch.y), width = 10)
#             last_x = int(touch.x)
#             last_y = int(touch.y)
#             n_points = 0
#             length = 0
#             sand[int(touch.x),int(touch.y)] = 1

#     def on_touch_move(self, touch):
#         global length, n_points, last_x, last_y
#         if touch.button == 'left':
#             touch.ud['line'].points += [touch.x, touch.y]
#             x = int(touch.x)
#             y = int(touch.y)
#             length += np.sqrt(max((x - last_x)**2 + (y - last_y)**2, 2))
#             n_points += 1.
#             density = n_points/(length)
#             touch.ud['line'].width = int(20 * density + 1)
#             sand[int(touch.x) - 10 : int(touch.x) + 10, int(touch.y) - 10 : int(touch.y) + 10] = 1
#             last_x = x
#             last_y = y

# Adding the API Buttons (clear, save and load)

class CarApp():

    def __init__(self):
        parent = Game()
        parent.serve_car()
        Clock.schedule_interval(parent.update, 1.0/60.0)
        #self.painter = MyPaintWidget()
        # clearbtn = Button(text = 'clear')
        # savebtn = Button(text = 'save', pos = (parent.width, 0))
        # loadbtn = Button(text = 'load', pos = (2 * parent.width, 0))
        # clearbtn.bind(on_release = self.clear_canvas)
        # savebtn.bind(on_release = self.save)
        # loadbtn.bind(on_release = self.load)
        # parent.add_widget(self.painter)
        # parent.add_widget(clearbtn)
        # parent.add_widget(savebtn)
        # parent.add_widget(loadbtn)
        #return parent

    # def clear_canvas(self, obj):
    #     global sand
    #     self.painter.canvas.clear()
    #     sand = np.zeros((longueur,largeur))

    # def save(self, obj):
    #     print("saving brain...")
    #     brain.save()
    #     plt.plot(scores)
    #     plt.show()

    # def load(self, obj):
    #     print("loading last saved brain...")
    #     brain.load()

# Running the whole thing
if __name__ == '__main__':
    #myCar = CarApp()
    #parent = Game()
    #Clock.schedule_interval(parent.update, 1.0/60.0)
    dd = HardwareInterface()
    dd.moveForward(1)
