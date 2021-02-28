# File: env.py
# Description: Building the environment-1 for the Mobile Robot to explore
# Agent - Mobile Robot
# Obstacles - 'road closed', 'trees', 'traffic lights', 'buildings'
# Importing libraries
import numpy as np  # To deal with data in form of matrices
import tkinter as tk  # To build GUI
from PIL import Image, ImageTk  # For adding images into the canvas widget
# Setting the sizes for the environment
pixels = 50  # pixels
env_height = 16 # grid height
env_width = 16 # grid width
# Global variable for dictionary with coordinates for the final route
a = {}
# Creating class for the environment
class Environment(tk.Tk, object):
    def __init__(self):
        super(Environment, self).__init__()
        self.action_space = ['up', 'down', 'left', 'right']
        self.n_actions = len(self.action_space)
        self.title('Major project')
        self.geometry('{0}x{1}'.format(env_height * pixels, env_height * pixels))
        self.build_environment()
        # Dictionaries to draw the final route
        self.d = {}
        self.f = {}
        # Key for the dictionaries
        self.i = 0
        # Writing the final dictionary first time
        self.c = True
        # Showing the steps for longest found route
        self.longest = 0
        # Showing the steps for the shortest route
        self.shortest = 0
    # Function to build the environment
    def build_environment(self):
        self.canvas_widget = tk.Canvas(self,  bg='white',
                                       height=env_height * pixels,
                                       width=env_width * pixels)
        for column in range(0, env_width * pixels, pixels):
            x0, y0, x1, y1 = column, 0, column, env_height * pixels
            self.canvas_widget.create_line(x0, y0, x1, y1, fill='grey')
        for row in range(0, env_height * pixels, pixels):
            x0, y0, x1, y1 = 0, row, env_height * pixels, row
            self.canvas_widget.create_line(x0, y0, x1, y1, fill='grey')
        img_obstacle1 = Image.open("images/road_closed1.png")
        self.obstacle1_object = ImageTk.PhotoImage(img_obstacle1)
        img_obstacle2 = Image.open("images/tree1.png")
        self.obstacle2_object = ImageTk.PhotoImage(img_obstacle2)
        img_obstacle3 = Image.open("images/tree2.png")
        self.obstacle3_object = ImageTk.PhotoImage(img_obstacle3)
        img_obstacle4 = Image.open("images/building1.png")
        self.obstacle4_object = ImageTk.PhotoImage(img_obstacle4)
        img_obstacle5 = Image.open("images/building2.png")
        self.obstacle5_object = ImageTk.PhotoImage(img_obstacle5)
        img_obstacle6 = Image.open("images/road_closed2.png")
        self.obstacle6_object = ImageTk.PhotoImage(img_obstacle6)
        img_obstacle7 = Image.open("images/road_closed3.png")
        self.obstacle7_object = ImageTk.PhotoImage(img_obstacle7)
        img_obstacle8 = Image.open("images/traffic_lights.png")
        self.obstacle8_object = ImageTk.PhotoImage(img_obstacle8)
        img_obstacle9 = Image.open("images/pedestrian.png")
        self.obstacle9_object = ImageTk.PhotoImage(img_obstacle9)
        img_obstacle10 = Image.open("images/shop.png")
        self.obstacle10_object = ImageTk.PhotoImage(img_obstacle10)
        img_obstacle11 = Image.open("images/bank1.png")
        self.obstacle11_object = ImageTk.PhotoImage(img_obstacle11)
        img_obstacle12 = Image.open("images/bank2.png")
        self.obstacle12_object = ImageTk.PhotoImage(img_obstacle12)
        img_obstacle13 = Image.open("images/library.jpg")
        self.obstacle13_object = ImageTk.PhotoImage(img_obstacle13)
        img_obstacle14 = Image.open("images/mdc.jpg")
        self.obstacle14_object = ImageTk.PhotoImage(img_obstacle14)
        img_obstacle15 = Image.open("images/energy.jpg")
        self.obstacle15_object = ImageTk.PhotoImage(img_obstacle15)
        img_obstacle16 = Image.open("images/slippery.png")
        self.obstacle16_object = ImageTk.PhotoImage(img_obstacle16)
        img_obstacle17 = Image.open("images/noentry.png")
        self.obstacle17_object = ImageTk.PhotoImage(img_obstacle17)
        img_obstacle18 = Image.open("images/private_road.jpg")
        self.obstacle18_object = ImageTk.PhotoImage(img_obstacle18)
        img_obstacle19 = Image.open("images/road_closed4.jpg")
        self.obstacle19_object = ImageTk.PhotoImage(img_obstacle19)
        img_obstacle20 = Image.open("images/traffic.cars.jpeg")
        self.obstacle20_object = ImageTk.PhotoImage(img_obstacle20)
        img_obstacle21 = Image.open("images/10th.jpg")
        self.obstacle21_object = ImageTk.PhotoImage(img_obstacle21)
        img_obstacle22 = Image.open("images/cafe.jpg")
        self.obstacle22_object = ImageTk.PhotoImage(img_obstacle22)
        img_obstacle23 = Image.open("images/mig.jpg")
        self.obstacle23_object = ImageTk.PhotoImage(img_obstacle23)
        img_obstacle24 = Image.open("images/food.jpg")
        self.obstacle24_object = ImageTk.PhotoImage(img_obstacle24)
        # Creating obstacles themselves
        self.obstacle1 = self.canvas_widget.create_image(pixels * 6, pixels * 15, anchor='nw', image=self.obstacle2_object)
        self.obstacle2 = self.canvas_widget.create_image(0, pixels * 2, anchor='nw', image=self.obstacle6_object)
        self.obstacle3 = self.canvas_widget.create_image(pixels, 0, anchor='nw', image=self.obstacle5_object)
        self.obstacle4 = self.canvas_widget.create_image(pixels * 9, pixels * 13, anchor='nw', image=self.obstacle2_object)
        self.obstacle5 = self.canvas_widget.create_image(pixels * 4, 0, anchor='nw', image=self.obstacle12_object)
        self.obstacle6 = self.canvas_widget.create_image(pixels * 5, pixels * 3, anchor='nw', image=self.obstacle7_object)
        self.obstacle7 = self.canvas_widget.create_image(pixels * 7, pixels * 3, anchor='nw', image=self.obstacle9_object)
        self.obstacle8 = self.canvas_widget.create_image(pixels * 6, pixels, anchor='nw', image=self.obstacle10_object)
        self.obstacle9 = self.canvas_widget.create_image(pixels * 11, pixels * 7, anchor='nw', image=self.obstacle4_object)
        self.obstacle10 = self.canvas_widget.create_image(pixels * 15, pixels * 9, anchor='nw', image=self.obstacle4_object)
        self.obstacle11 = self.canvas_widget.create_image(pixels * 3, pixels * 12, anchor='nw', image=self.obstacle4_object)
        self.obstacle12 = self.canvas_widget.create_image(pixels * 5, pixels * 11, anchor='nw', image=self.obstacle4_object)
        self.obstacle13 = self.canvas_widget.create_image(0, pixels * 8, anchor='nw', image=self.obstacle3_object)
        self.obstacle14 = self.canvas_widget.create_image(pixels * 3, pixels * 7, anchor='nw', image=self.obstacle8_object)
        self.obstacle15 = self.canvas_widget.create_image(0, pixels * 4, anchor='nw', image=self.obstacle1_object)
        self.obstacle16 = self.canvas_widget.create_image(pixels * 8, 0, anchor='nw', image=self.obstacle3_object)
        self.obstacle17 = self.canvas_widget.create_image(pixels * 16, pixels * 5, anchor='nw', image=self.obstacle4_object)
        self.obstacle18 = self.canvas_widget.create_image(pixels*14, pixels * 14, anchor='nw', image=self.obstacle11_object)
        self.obstacle19 = self.canvas_widget.create_image(pixels * 10, pixels * 4, anchor='nw', image=self.obstacle8_object)
        self.obstacle20 = self.canvas_widget.create_image(pixels * 7, pixels * 6, anchor='nw', image=self.obstacle4_object)
        self.obstacle21 = self.canvas_widget.create_image(pixels * 13, pixels , anchor='nw', image=self.obstacle4_object)
        self.obstacle22 = self.canvas_widget.create_image(pixels * 2, pixels * 3, anchor='nw', image=self.obstacle2_object)
        self.obstacle23 = self.canvas_widget.create_image(pixels * 14,pixels * 6, anchor='nw', image=self.obstacle13_object)
        self.obstacle24 = self.canvas_widget.create_image(pixels * 4,pixels * 6, anchor='nw', image=self.obstacle14_object)
        self.obstacle25 = self.canvas_widget.create_image(pixels * 2,pixels * 4, anchor='nw', image=self.obstacle15_object)
        self.obstacle26 = self.canvas_widget.create_image(pixels * 10,pixels * 8, anchor='nw', image=self.obstacle16_object)
        self.obstacle27 = self.canvas_widget.create_image(pixels * 12,pixels * 10, anchor='nw', image=self.obstacle17_object)
        self.obstacle28 = self.canvas_widget.create_image(pixels * 14,pixels * 12, anchor='nw', image=self.obstacle18_object)
        self.obstacle29 = self.canvas_widget.create_image(pixels * 11,pixels * 1, anchor='nw', image=self.obstacle19_object)
        self.obstacle30 = self.canvas_widget.create_image(pixels * 7,pixels * 13, anchor='nw', image=self.obstacle20_object)
        self.obstacle31 = self.canvas_widget.create_image(pixels * 15,pixels * 3, anchor='nw', image=self.obstacle21_object)
        self.obstacle32 = self.canvas_widget.create_image(pixels * 4,pixels * 15, anchor='nw', image=self.obstacle22_object)
        self.obstacle33 = self.canvas_widget.create_image(pixels * 2,pixels * 14, anchor='nw', image=self.obstacle23_object)
        self.obstacle34 = self.canvas_widget.create_image(pixels * 8,pixels * 5, anchor='nw', image=self.obstacle24_object)
        print("1: Libary")
        print("2: Food Court")
        print("3: MDC")
        print("4: Energy House")
        print("5: Cafeteria")
        print("6: MIG")
        print("7: 10th Block")
        inp = int(input("Enter the number of destination where you want to go: "))
        if inp == 1:
            img_flag = Image.open("images/library.jpg")
            self.flag_object = ImageTk.PhotoImage(img_flag)
            self.flag = self.canvas_widget.create_image(pixels * 14, pixels * 6, anchor='nw', image=self.flag_object)
        elif inp == 2:
            img_flag = Image.open("images/food.jpg")
            self.flag_object = ImageTk.PhotoImage(img_flag)
            self.flag = self.canvas_widget.create_image(pixels * 8, pixels * 5, anchor='nw', image=self.flag_object)
        elif inp == 3:
            img_flag = Image.open("images/mdc.jpg")
            self.flag_object = ImageTk.PhotoImage(img_flag)
            self.flag = self.canvas_widget.create_image(pixels * 4, pixels * 6, anchor='nw', image=self.flag_object)
        elif inp == 4:
            img_flag = Image.open("images/energy.jpg")
            self.flag_object = ImageTk.PhotoImage(img_flag)
            self.flag = self.canvas_widget.create_image(pixels * 2, pixels * 4, anchor='nw', image=self.flag_object)
        elif inp == 5:
            img_flag = Image.open("images/cafe.jpg")
            self.flag_object = ImageTk.PhotoImage(img_flag)
            self.flag = self.canvas_widget.create_image(pixels * 4, pixels * 15, anchor='nw', image=self.flag_object)
        elif inp == 6:
            img_flag = Image.open("images/mig.jpg")
            self.flag_object = ImageTk.PhotoImage(img_flag)
            self.flag = self.canvas_widget.create_image(pixels * 2, pixels * 14, anchor='nw', image=self.flag_object)
        elif inp == 7:
            img_flag = Image.open("images/10th.jpg")
            self.flag_object = ImageTk.PhotoImage(img_flag)
            self.flag = self.canvas_widget.create_image(pixels * 15, pixels * 3, anchor='nw', image=self.flag_object)
        else:
            print("Invalid input!")
        # Uploading the image of Mobile Robot
        img_robot = Image.open("images/agent1.png")
        self.robot = ImageTk.PhotoImage(img_robot)
        # Creating an agent with photo of Mobile Robot
        self.agent = self.canvas_widget.create_image(0, 0, anchor='nw', image=self.robot)
        # Packing everything
        self.canvas_widget.pack()
    # Function to reset the environment and start new Episode
    def reset(self):
        self.update()
        # Updating agent
        self.canvas_widget.delete(self.agent)
        self.agent = self.canvas_widget.create_image(0, 0, anchor='nw', image=self.robot)
        # # Clearing the dictionary and the i
        self.d = {}
        self.i = 0
        # Return observation
        return self.canvas_widget.coords(self.agent)
    # Function to get the next observation and reward by doing next step
    def step(self, action):
        # Current state of the agent
        state = self.canvas_widget.coords(self.agent)
        base_action = np.array([0, 0])
        # Updating next state according to the action
        if action == 0:
            if state[1] >= pixels:
                base_action[1] -= pixels
        # Action 'down'
        elif action == 1:
            if state[1] < (env_height - 1) * pixels:
                base_action[1] += pixels
        # Action right
        elif action == 2:
            if state[0] < (env_width - 1) * pixels:
                base_action[0] += pixels
        # Action left
        elif action == 3:
            if state[0] >= pixels:
                base_action[0] -= pixels
        # Moving the agent according to the action
        self.canvas_widget.move(self.agent, base_action[0], base_action[1])
        # Writing in the dictionary coordinates of found route
        self.d[self.i] = self.canvas_widget.coords(self.agent)
        # Updating next state
        next_state = self.d[self.i]
        # Updating key for the dictionary
        self.i += 1
        # Calculating the reward for the agent
        if next_state == self.canvas_widget.coords(self.flag):
            reward = 1
            done = True
            next_state = 'goal'
            # Filling the dictionary first time
            if self.c == True:
                for j in range(len(self.d)):
                    self.f[j] = self.d[j]
                self.c = False
                self.longest = len(self.d)
                self.shortest = len(self.d)
            # Checking if the currently found route is shorter
            if len(self.d) < len(self.f):
                # Saving the number of steps for the shortest route
                self.shortest = len(self.d)
                # Clearing the dictionary for the final route
                self.f = {}
                # Reassigning the dictionary
                for j in range(len(self.d)):
                    self.f[j] = self.d[j]
            # Saving the number of steps for the longest route
            if len(self.d) > self.longest:
                self.longest = len(self.d)
        elif next_state in [self.canvas_widget.coords(self.obstacle1),
                            self.canvas_widget.coords(self.obstacle2),
                            self.canvas_widget.coords(self.obstacle3),
                            self.canvas_widget.coords(self.obstacle4),
                            self.canvas_widget.coords(self.obstacle5),
                            self.canvas_widget.coords(self.obstacle6),
                            self.canvas_widget.coords(self.obstacle7),
                            self.canvas_widget.coords(self.obstacle8),
                            self.canvas_widget.coords(self.obstacle9),
                            self.canvas_widget.coords(self.obstacle10),
                            self.canvas_widget.coords(self.obstacle11),
                            self.canvas_widget.coords(self.obstacle12),
                            self.canvas_widget.coords(self.obstacle13),
                            self.canvas_widget.coords(self.obstacle14),
                            self.canvas_widget.coords(self.obstacle15),
                            self.canvas_widget.coords(self.obstacle16),
                            self.canvas_widget.coords(self.obstacle17),
                            self.canvas_widget.coords(self.obstacle18),
                            self.canvas_widget.coords(self.obstacle19),
                            self.canvas_widget.coords(self.obstacle20),
                            self.canvas_widget.coords(self.obstacle21),
                            self.canvas_widget.coords(self.obstacle22),
                            self.canvas_widget.coords(self.obstacle23),
                            self.canvas_widget.coords(self.obstacle24),
                            self.canvas_widget.coords(self.obstacle25),
                            self.canvas_widget.coords(self.obstacle26),
                            self.canvas_widget.coords(self.obstacle27),
                            self.canvas_widget.coords(self.obstacle28),
                            self.canvas_widget.coords(self.obstacle29),
                            self.canvas_widget.coords(self.obstacle30),
                            self.canvas_widget.coords(self.obstacle31),
                            self.canvas_widget.coords(self.obstacle32),
                            self.canvas_widget.coords(self.obstacle33),
                            self.canvas_widget.coords(self.obstacle34),]:
            reward = -1
            done = True
            next_state = 'obstacle'
            # Clearing the dictionary and the i
            self.d = {}
            self.i = 0
        else:
            reward = 0
            done = False
        return next_state, reward, done
    # Function to refresh the environment
    def render(self):
        #time.sleep(0.03)
        self.update()
    # Function to show the found route
    def final(self):
        # Deleting the agent at the end
        self.canvas_widget.delete(self.agent)
        # Showing the number of steps
        print('The shortest route:', self.shortest)
        print('The longest route:', self.longest)
        # Creating initial point
        origin = np.array([20, 20])
        self.initial_point = self.canvas_widget.create_oval(
            origin[0] - 5, origin[1] - 5,
            origin[0] + 5, origin[1] + 5,
            fill='blue', outline='blue')
        # Filling the route
        for j in range(len(self.f)):
            # Showing the coordinates of the final route
            print(self.f[j])
            self.track = self.canvas_widget.create_oval(
                self.f[j][0] + origin[0] - 5, self.f[j][1] + origin[0] - 5,
                self.f[j][0] + origin[0] + 5, self.f[j][1] + origin[0] + 5,
                fill='blue', outline='blue')
            # Writing the final route in the global variable a
            a[j] = self.f[j]
# Returning the final dictionary with route coordinates
# Then it will be used in agent_brain.py
def final_states():
    return a
if __name__ == '__main__':
    env = Environment()
    env.mainloop()