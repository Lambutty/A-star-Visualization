import numpy as np
from termcolor import colored
import math as mother
import heapq
from functools import total_ordering
import random
from os import system, name
from time import sleep


def clear():
    if name == 'nt':  # for windows
        _ = system('cls')
    else:  # for mac and linux(here, os.name is 'posix')
        _ = system('clear')


@total_ordering
class Nodes(object):
    def __init__(self, g, h, last, xy):
        self.f = g + h
        self.g = g
        self.h = h
        self.last = last
        self.xy = xy

    def __repr__(self):
        return '{0.__class__.__name__}(f={0.f},h={0.h}, xy={0.xy},g={0.g},last={0.last})'.format(
            self)

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):

        return self.f == other.f

    def __str__(self):
        return str(self.__dict__)

    def xy(self):
        return self.xy

    def f(self):  #returns f = total distance g+h value
        return self.f

    def g(self):  #returns g = excact smallest distance to node value
        return self.g

    def h(self):  #returns h = abosulte guess till end value
        return self.h

    def last(
            self
    ):  #returns last = saves the index of the last dot before itself as tuple value
        return self.last

    def update_f(self, f):  #functions for updating set values
        self.f = f

    def update_g(self, neue):
        self.g = neue

    def update_h(self, h):
        self.h = h

    def update_last(self, last):
        if type(last) == tuple:
            self.last = last

        else:
            error(last, tuple)


def fill(a, b, g, h, last):  #fill matrix
    matrix[a][b] = Nodes(g, h, last, (a, b))


def error(error, typ):
    print(
        colored(
            f'Unable to do as you like this not takes {type(error)}! only {typ}!',  
            'red'))# a little side error but not necessary at moment


def matrixObj(n):
    matrix = np.zeros((n, n), dtype=object)  #Create an empty matrix
    return matrix


def generate(n):

    grid = np.random.randint(1, 1000, size=(n, n))  #Generate grid with numbers
    grid[0][0] = 0
    grid[n - 1][n - 1] = 0
    return grid


def backtrackingPath(matrix, last):  # backtrack the Path
    global FUN

    if last.xy == (len(matrix) - 1, len(matrix) - 1):
        FUN[last.xy] = 1
    if last.xy == (0, 0):
        FUN[last.xy] = 1
        FUN[len(Path) - 1][len(FUN) - 1] = 1
        for i in range(len(FUN)):
            for j in range(len(FUN)):
                if FUN[i][j] == 0:
                    print("[ ] ", end='')
                elif FUN[i][j] == 1:
                    print(colored("[X] ", "red"), end='')
            print()

    else:
        FUN[last.xy] = 1
        return backtrackingPath(matrix, matrix[last.last])


def main(valueGrid, objMatrix):
    global n
    global Path
    global Pathtryout
    neighbors = lambda x, y: [
        (x2, y2) for x2 in range(x - 1, x + 2)  #all neighbors
        for y2 in range(y - 1, y + 2) if (-1 < x < l and -1 < y < l and (x != x2 or y != y2) and (0 <= x2 < l) and (0 <= y2 < l))]

    l = len(objMatrix)  #starting at 0
    ClosedList = []
    heap = []
    start = (0, 0)
    end = (n - 1, n - 1)
    heapq.heappush(heap, objMatrix[start])
    printlist = []
    astar = False
    while not astar:  # the actual magic happening basically
        # always taking the node with the smallest f cost till we are at the end

        try:
            currentnode = heapq.heappop(heap)

        except IndexError:
            print("INDEXER ERRUS")
            break
        if currentnode.xy == end:
            #return backtrackingPath(ClosedList)
            print(f"Die minimalste Wegkost zum Ziel beträgt: {currentnode.g}!")
            #print(objMatrix)
            return backtrackingPath(objMatrix, ClosedList[len(ClosedList) - 1])
            break
        if currentnode not in ClosedList:
            ClosedList.append(currentnode)
            clear()
            for i in range(len(Pathtryout)):
                for j in range(len(Pathtryout)):
                    if Pathtryout[i, j] == "C":
                        print(
                            colored(f"[{Pathtryout[currentnode.xy]}]  ",
                                    "red"),
                            end='')
                    elif (i, j) != currentnode.xy:

                        print(f"[{Pathtryout[currentnode.xy]}]  ", end='')
                    else:
                        printlist.append(currentnode)

                        print(
                            colored(f"[{Pathtryout[currentnode.xy]}]  ",
                                    "green"),
                            end='')
                        #print("", end='\r')
                print()
            sleep(0.3)
        for t in printlist:
            Pathtryout[t.xy] = ("C")
        #print(currentnode)
        currentneighbors = neighbors(currentnode.xy[0], currentnode.xy[1])
        #print(currentneighbors)
        for node in currentneighbors:
            #print(node)
            #print(objMatrix[node])

            if objMatrix[node].g > currentnode.g + valueGrid[node]:
                objMatrix[node].update_g(currentnode.g + valueGrid[node])
                objMatrix[node].update_f(objMatrix[node].g + objMatrix[node].h)
                objMatrix[node].update_last(currentnode.xy)
                heapq.heappush(heap, objMatrix[node])


if __name__ == "__main__":
    n = 7  #Gridgröße
    gen = generate(
        n
    )  #generate matrix with random numbers range 1 to x(top left 0 top                                            right 0 for start and end)
    matrix = matrixObj(n)  #setting object matrix
    #test = []
    Path = np.zeros((len(matrix), len(matrix)))
    FUN = Path
    Pathtryout = np.empty([len(matrix), len(matrix)], dtype=str)
    for i in range(len(Path)):
        for j in range(len(Path)):
            Pathtryout[i][j] = "O "

    for i in range(len(matrix)):  #setting up Matrix with Objects
        for j in range(len(matrix)):
            fill(i, j, float('inf'),
                 round(mother.sqrt((n - i)**2 + (n - j)**2), 2), float('inf'))

            #fill function to fill matrix withobjects
    fill(0, 0, 0, 0, (0, 0))  #setting up left and down right as
    #start and end
    """
  for i in range(len(matrix)):
    for j in range(len(matrix)):                              
      print(f"line: {i} item: {j} is:{matrix[i][j]}")
      print(f"Waycost is: {gen[i][j]}")
  #√((x2 - x1)2 + (y2 - y1)2) distanceformel
  
  
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      heapq.heappush(test,matrix[i][j])
  while test:
    print(heapq.heappop(test))
  """

    main(gen, matrix)
    print(gen)
    #print(matrix)
