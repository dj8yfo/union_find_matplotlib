import math
from Grid import Grid
from random import randint
from RandomConnectionBag import RandomConnectionBag
from datetime import datetime
from QuickUnionUF import QuickUnionUF
from QuickFindUF import QuickFindUF
from WeightedQuickUnionUF import WeightedQuickUnionUF
from RankedQuickUnionUF import RankedQuickUnionUF
import math
from graphic_sample import GraphicGrid
import matplotlib.animation as animation

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def add_random_connection(union_find):
    length =  len(union_find.get_managed_array())
    p  = randint(0, length - 1)
    q = p
    while q == p:
        q  = randint(0, length - 1)

    if not union_find.connected(p, q):
        union_find.union(p, q)


def new_experiment_sequence(new_grid, union_find, show_progress):
    resulting_representations = []
    connections = RandomConnectionBag(len(new_grid), union_find)
    iterations = 0
    max_num_of_random_connections =  len(new_grid)*3
    period = 5
    delay = False
    effective_iterations = 0
    while iterations < max_num_of_random_connections:
        x,y = connections.get_next_spiraled()
        if union_find.count ==  1:
            break
        if effective_iterations%period == 0 and show_progress and not delay:
            next_representation = new_grid.State_info(new_grid, union_find)
            resulting_representations.append(next_representation.get_represantation())
            # print next_representation
            # print union_find
            # print 'iterations consumed:', iterations
            # print 'connections left', len(connections)

        if union_find.connected(x,y):
            delay = False
        else:
            delay = False
            effective_iterations +=1
        union_find.union(x, y)
            # delay = False
        iterations += 1
    print union_find
    last_representation = new_grid.State_info(new_grid, union_find)
    resulting_representations.append(next_representation.get_represantation(True))
    print 'iterations consumed:', iterations
    print len(resulting_representations)
    return resulting_representations


def new_experiment(new_grid, union_find, show_progress):
    connections = RandomConnectionBag(len(new_grid), union_find)
    iterations = 0
    max_num_of_random_connections =  len(new_grid)
    period = new_grid.size()*10
    start = datetime.now()
    while iterations < max_num_of_random_connections:
        x,y = connections.get_next_spiraled()
        if union_find.count ==  1:
            break
        if iterations%period == 0 and show_progress:
            print union_find
            print 'iterations consumed:', iterations
            print 'connections left', len(connections)

        union_find.union(x, y)
            # delay = False

        iterations += 1
    end = datetime.now()
    print 'iterations consumed:', iterations
    print union_find
    return iterations, (end -start).total_seconds()


# types_of_experiments = [WeightedQuickUnionUF, QuickUnionUF, QuickFindUF]
types_of_experiments = [RankedQuickUnionUF]
# for dimension in [5]:
dimensions = [10]
# dimensions = [5]
times_execution = {}
for type in types_of_experiments:
    times_execution[type] = {}
    times_execution[type]['time_elapsed'] = []
    times_execution[type]['time per iter'] = []


def show_last_state():
    for mytype in types_of_experiments:

        print 'experiment type' , mytype
        print '-'*70
        for index in range(0, len(dimensions)):

            dimension = dimensions[index]
            new_grid = Grid(dimension)

            show_progress = False
            # if dimension == 80:
            #     show_progress = True
            # else:
            #     show_progress = False
                        # print i
            union_find = mytype(new_grid)
            # print union_find
            new_experiment(new_grid, union_find, show_progress)

            graphic = GraphicGrid(new_grid,union_find)
            graphic.drawGrid_alt()

        print '-'*70
    print times_execution


def animate():
    for mytype in [RankedQuickUnionUF]:

        print 'experiment type' , mytype
        print '-'*70
        dimension = 25
        new_grid = Grid(dimension)

        union_find = mytype(new_grid, False)
        # print union_find
        sequence = new_experiment_sequence(new_grid, union_find, True)
        print 'len sequence', len(sequence)
        print sequence[len(sequence) -1]

    fig = plt.figure(figsize=(16,9), dpi=200)
    ax = plt.axes(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Test')

    z_lim = float(sequence[len(sequence) -1].max_display_rank)
    print 'zlim 3d', z_lim
    ax.set_zlim3d([0.0, z_lim])
    patches = ax.scatter(0, 0, 0)
    lines = [ax.plot([0, 1], [0, 1], [0, 1], linewidth=0.2)]
    redundant_lines = [ax.plot([0, 1], [0, 1], [0, 1], linewidth=0.2)]

    graphic = GraphicGrid(new_grid, representations=sequence,zlim=z_lim)


    line_ani = animation.FuncAnimation(fig, graphic.update_frame, len(sequence), fargs=(patches, lines, redundant_lines, ax),
                                  interval=1, blit=False)

    plt.show()

    print times_execution
animate()
# show_last_state()



