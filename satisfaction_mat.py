from random import choice, randint
import matplotlib.pyplot as plt

def get_step():
    direction=choice([1,-1])
    distance=randint(0,2)
    step=direction*distance
    return step

class RandomWalk():
    """A class to generate random walks."""
    def __init__(self, num_points=1000): 
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # All walks start at (0, 0). 
        self.x_values = [0] 
        self.y_values = [0]
        self.x_end_points=[]
        self.y_end_points=[]
    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length. 
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_step = get_step()
            y_step = get_step()
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x) 
            self.y_values.append(next_y)
        #save end points
        self.x_end_points.append(self.x_values[-1])
        self.y_end_points.append(self.y_values[-1])

rw = RandomWalk(50000)
while True:
    # Make a random walk, and plot the points. 
    rw.fill_walk()
    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6),dpi=128)
    point_numbers = list(range(rw.num_points))
    end_point_numbers= list(range(len(rw.x_end_points)-1))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],c='red',edgecolors='none',s=100)
    plt.scatter(rw.x_end_points[:-1], rw.y_end_points[:-1],c=end_point_numbers,cmap=plt.cm.Purples,edgecolors='orange',s=100)
    #Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ") 
    if keep_running == 'n':
        break
    rw.num_points+=rw.num_points
