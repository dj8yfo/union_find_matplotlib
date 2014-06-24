import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Selection import Selection
from Insertion import Insertion
from Shell_Sort import Shell_Sort
import random
from UpdateBars import BarUpdate
import math

sorting_algorithm = Selection
n_elements  = 1000
array = [i**2*math.fabs(math.sin(i))*random.uniform(0.0, 1.0) for i in range(n_elements)]
fig = plt.figure(figsize=(16,9), dpi=200)
ax = fig.add_subplot(1, 1, 1)

sort =  sorting_algorithm(array)
sort.sort()


graphic = BarUpdate(ax, sort.representations_of_states, 15)

anim = FuncAnimation(fig, graphic, len(sort.representations_of_states), init_func=graphic.init,
        interval=1, blit=True)

plt.show()
