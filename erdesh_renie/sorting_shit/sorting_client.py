import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Selection import Selection
from Insertion import Insertion
from Shell_Sort import Shell_Sort
import random
from UpdateBars import BarUpdate

sorting_algorithm = Selection
n_elements  = 200
array = [random.uniform(0.0, 1.0) for i in range(n_elements)]
fig = plt.figure(figsize=(16,9), dpi=200)
ax = fig.add_subplot(1, 1, 1)

sort =  sorting_algorithm(array)
sort.sort()


graphic = BarUpdate(ax, sort.representations_of_states)

anim = FuncAnimation(fig, graphic, len(sort.representations_of_states), init_func=graphic.init,
        interval=10, blit=True)

plt.show()
