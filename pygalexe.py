from random import randint
import pygal

ROLLS=10000000

class Die():
    """A class representing a single die."""
    def __init__(self, num_sides=6): 
        """Assume a six-sided die."""
        self.num_sides = num_sides
    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

die_1=Die()
die_2=Die(10)

results=[]

for roll_num in range(ROLLS):
    result=die_1.roll()+die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result=die_1.num_sides+die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)/ROLLS*100
    frequencies.append(frequency)

#Visualize the results
hist=pygal.Pie(half_pie=True)

hist.title="Results of rolling two D6 1000 times."
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist._titles="Result"
hist.y_title="Frequency of Result"

j=2
for i in frequencies:
    hist.add(f'{j}',i)
    j+=1

hist.render_to_file('die_visual.svg')