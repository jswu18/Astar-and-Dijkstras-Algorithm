from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
def create_graph(): 
    graph = {}
    for i in range(34):
        for j in range(34):
            graph[(i,j)] = {'visited':False, 'distance':np.inf, 'valid':True, 'parent': (0, 0)}
            if i in range(6,13) and j in range(4,11):
                if j >= 14-i:
                    graph[(i,j)]['valid'] = False
            if i in range(14,18) and j in range(11,16):
                graph[(i,j)]['valid'] = False
            if i in range(9,13) and j in range(16,21):
                graph[(i,j)]['valid'] = False
            if i in range(18,25) and j in range(16,20):
                graph[(i,j)]['valid'] = False
            if i in range(20, 29) and j in range(6,20):
                if j <= 13*i/8 - 212/8:
                 graph[(i,j)]['valid'] = False
            if (i in range(12,29) and j in range(25,29)) or (i in range(25,29) and j in range(22,26)):
                graph[(i,j)]['valid'] = False
    return graph

def astar(graph, source):
    goal = (32,32)
    graph[source]['visited'] = True
    num_nodes_visited = 1
    graph[source]['g'] = 0
    queue = [source]
    queue_distance = [calculate_distance(goal, source)+graph[source]['g']]
    while (len(queue) != 0):
        indx = queue_distance.index(min(queue_distance))
        d_min = queue_distance.pop(indx)
        current = queue.pop(indx)
        if current == goal:
            break
        for i in range(2):
            if current[0]+i <= 32:
                for j in range(2):
                    if (current[1]+j) <= 32:
                        if i != 0 or j != 0:
                            neighbour = (current[0]+i, current[1]+j)
                            if graph[neighbour]['valid'] == True:
                                if i+j == 2:
                                    dis = math.sqrt(2)
                                else:
                                    dis = 1
                                if graph[neighbour]['visited'] == False:
                                    graph[neighbour]['visited'] = True	
                                    num_nodes_visited += 1							
                                    graph[neighbour]['parent'] = current								
                                    graph[neighbour]['g'] = graph[current]['g'] + dis
                                    queue.append(neighbour)
                                    queue_distance.append(calculate_distance(goal, neighbour)+graph[neighbour]['g'])                                  	
    path = [(32, 32)]
    parent = (32, 32)
    while parent != source:
        parent = graph[path[len(path)-1]]['parent']
        path.append(parent)
    min_distance = (graph[(32,32)]['g'])	
    print("Total Number of Nodes Visited:", num_nodes_visited)  	
    return(min_distance, path)

def calculate_distance(goal, current):
    d = math.sqrt(((goal[0]-current[0])*(goal[0]-current[0]))+((goal[1]-current[1])*(goal[1]-current[1])))
    return d

if __name__ == "__main__":
    g = create_graph()
    points = [x for x in g.keys() if not (g[x]['valid'])]
    x = [i[0] for i in points]
    y = [i[1] for i in points]
    plt.scatter(x,y)   
    min_distance, path = astar(g, (2,2))
    print("Minimum Distance:", min_distance)
    x = [i[0] for i in path]
    y = [i[1] for i in path]
    plt.plot(x,y, 'r')
    plt.show()