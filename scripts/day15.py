import sys


def printL(L):
    print('-------------Start of array-------------')
    for item in L:
        print((item))
    print('-------------End of array-------------')


def check_risk(risk_level, x, y):
    right_risk = risk_level[y][x+1]+risk_level[y][x+2]+risk_level[y+1][x+2]
    bottom_risk = risk_level[y+1][x]+risk_level[y+2][x+1]+risk_level[y+2][x]
    if right_risk > bottom_risk:
        return [x, y+1, risk_level[y][x]]
    else:
        return [x+1, y, risk_level[y][x]]


def move(risk_level, current_x, current_y):
    if current_x < len(risk_level[0])-2 and current_y < len(risk_level)-2:
        return check_risk(risk_level, current_x, current_y)
    elif current_x < len(risk_level[0])-1 and current_y < len(risk_level)-1:
        if risk_level[current_y+1][current_x] > risk_level[current_y][current_x+1]:
            return [current_x+1, current_y, risk_level[current_x][current_y]]
        else:
            return [current_x, current_y+1, risk_level[current_x][current_y]]
    elif current_x < len(risk_level[0])-1:
        return [current_x+1, current_y, risk_level[current_y][current_x]]
    elif current_y < len(risk_level)-1:
        return [current_x, current_y+1, risk_level[current_y][current_x]]
    else:
        print(current_x, current_y)
        print("pb")


def update_cost(risk_level, risk_cost, x, y):
    if x < len(risk_level[0])-1:
        if risk_cost[y][x+1] == "inf":
            risk_cost[y][x+1] = risk_level[y][x]+risk_cost[y][x]
        else:
            risk_cost[y][x+1] = min(risk_level[y][x] +
                                    risk_cost[y][x], risk_cost[y][x+1])
    if y < len(risk_level)-1:
        if risk_cost[y+1][x] == "inf":
            risk_cost[y+1][x] = risk_level[y][x]+risk_cost[y][x]
        else:
            risk_cost[y+1][x] = min(risk_level[y][x] +
                                    risk_cost[y][x], risk_cost[y+1][x])
    if x > 0:
        if risk_cost[y][x-1] == "inf":
            risk_cost[y][x-1] = risk_level[y][x]+risk_cost[y][x]
        else:
            risk_cost[y][x-1] = min(risk_level[y][x] +
                                    risk_cost[y][x], risk_cost[y][x-1])
    if y > 0:
        if risk_cost[y-1][x] == "inf":
            risk_cost[y-1][x] = risk_level[y][x]+risk_cost[y][x]
        else:
            risk_cost[y-1][x] = min(risk_level[y][x] +
                                    risk_cost[y][x], risk_cost[y-1][x])


# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)

# This code is contributed by Divyanshu Mehta

with open('./inputs/input_day15.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    lines = f.readlines()

    risk_level = []
    risk_cost = []

    for i in range(0, len(lines)):
        tmp = []
        tmp_2 = []
        for j in range(len(lines[i].split("\n")[0])):
            tmp.append(int(lines[i][j]))
            tmp_2.append("inf")
        risk_level.append(tmp)
        risk_cost.append(tmp_2)

    risk_cost[0][0] = 0
    # printL(risk_level)

    # y = len(risk_level)
    # x = len(risk_level[0])

    # risk = 0

    # current_x = 0
    # current_y = 0
    # while current_x < x-1 or current_y < y-1:
    # data = move(risk_level, current_x, current_y)
    # current_x = data[0]
    # current_y = data[1]
    # risk += data[2]
    for k in range(len(risk_level)+1):
        for y in range(len(risk_level)):
            for x in range(len(risk_level[y])):
                update_cost(risk_level, risk_cost, x, y)

    printL(risk_cost)
    print(risk_cost[len(risk_cost)-1][len(risk_cost[0])-1])
    f.close()
