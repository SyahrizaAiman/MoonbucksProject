import geopy.distance
import pandas as pd
import numpy as np
from numpy import reshape, sort
from sys import maxsize
from itertools import permutations
from collections import defaultdict
import csv


# DFS Algorithm (to decide turutan)
class DFSGraph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(empty, v, visited, path):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        path.append(v)
        # print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in empty.graph[v]:
            if neighbour not in visited:
                empty.DFSUtil(neighbour, visited, path)
                

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(empty, v):
        result = []

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        empty.DFSUtil(v, visited, result)
        return result


# Kruskal Algorithm (untuk cari minimum spamming tree & decide first node)
class Graph():

    def __init__(empty, vertex):
        empty.vertex = vertex
        empty.graph = []

    def add_edge(empty, begin, destination, distance):
        empty.graph.append([begin, destination, distance])

    def search(empty, parent, i):
        if parent[i] == i:
            return i
        return empty.search(parent, parent[i])

    # Add the edge in solution and update the parent list
    def apply_union(self, parent, rank, x, y):
        xRoot = self.search(parent, x)
        yRoot = self.search(parent, y)
        if rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1

    def Kruskal(empty):
        result = []
        i, e = 0, 0
        empty.graph = sorted(empty.graph, key=lambda item: item[2])  # Sort the distance ascending order
        parent = []
        rank = []
        for node in range(empty.vertex):
            parent.append(node)
            rank.append(0)
        while e < empty.vertex - 1:
            begin, destination, distance = empty.graph[i]
            i += 1
            x = empty.search(parent, begin)
            y = empty.search(parent, destination)

            # To ensure the edges added will not form a cycle
            if x != y:
                e = e + 1
                result.append([begin, destination, distance])
                empty.apply_union(parent, rank, x, y)

        # for begin, destination, distance in result:
        #     print("Distance:", begin, destination, end=" ")
        #     print("-", distance)
        return result


def readFile(fileName):
    DataFrame = pd.read_csv(fileName, usecols=["name", "latitude", "longitude"])
    # print(DataFrame)
    return DataFrame


def calculateDistance(coordinat1, coordinat2):
    distance = int(geopy.distance.distance(coordinat1, coordinat2).km)
    return distance


def shortSpanningTree(listOfStoreLocation):
    vertex = int(listOfStoreLocation.index.stop)
    # print(row);
    graph = Graph(vertex)
    # print(type(graph));

    for begin in range(graph.vertex):
        for destination in range(graph.vertex):
            points1 = (listOfStoreLocation.iloc[begin][1], listOfStoreLocation.iloc[begin][2])
            points2 = (listOfStoreLocation.iloc[destination][1], listOfStoreLocation.iloc[destination][2])
            distance = calculateDistance(points1, points2)
            graph.add_edge(begin, destination, distance)
        
    tree = graph.Kruskal()
    # print(result)
    return tree


def OrderOfRoute(routeList):
    route = DFSGraph()
    for i in range(len(routeList)):
        route.addEdge(int(routeList[i][0]), int(routeList[i][1])) #for foward diration graph
        route.addEdge(int(routeList[i][1]), int(routeList[i][0])) # for backward direction graph

    graph = route.graph
    path = [0 for i in range(len(graph))] #to chect last vertices are the last one
    for i in range(len(routeList)):
        path[routeList[i][0]] += 1
        path[routeList[i][1]] += 1
    #print(path)
    shortestRoute = route.DFS(path.index(min(path)))
    return shortestRoute

totalDistanceList = []

def findDistributionCenter(listOfStoreLocation):
    storeName = [listOfStoreLocation.iloc[i][0] for i in range(6)] #iloc is fucntion untuk dataframe untuk bagi index kepada df
    # print(storeNameList);
    graph = shortSpanningTree(listOfStoreLocation)
    # print(graph)
    path = OrderOfRoute(graph)
    # print(path)
    distance = [graph[i][2] for i in range(len(graph))]
    distance.append(
        calculateDistance((listOfStoreLocation.iloc[path[0]][1], listOfStoreLocation.iloc[path[0]][2]), (
            listOfStoreLocation.iloc[path[len(path) - 1]][1],
            listOfStoreLocation.iloc[path[len(path) - 1]][2])))
    print(path)
    totalDistance = 0

    for i in range(len(path)):
        print(storeName[path[i]], "--->", end=" ")
        totalDistance += distance[i]
    totalDistanceList.append(totalDistance)    

    print(storeName[path[0]])
    print('Total Distance travelled is:', totalDistance, 'km')
    print('The distribution center is', storeName[path[0]], '\n')

ThailandStore = readFile("MoonbucksProject\\Location\\Thailand.csv")
IndonesiaStore = readFile("MoonbucksProject\\Location\\Indonesia.csv")
MalaysiaStore = readFile("MoonbucksProject\\Location\\Malaysia.csv")
PhilippinesStore = readFile("MoonbucksProject\\Location\\Philippines.csv")
SingaporeStore = readFile("MoonbucksProject\\Location\\Singapore.csv")

findDistributionCenter(MalaysiaStore)
findDistributionCenter(IndonesiaStore)
findDistributionCenter(ThailandStore)
findDistributionCenter(PhilippinesStore)
findDistributionCenter(SingaporeStore)

#for ranking problem 3
countryList = ["Malaysia","Indonesia","Thailand","Philippines","Singapore"]
rankingList= [['',0]  for i in range(5)]
for i in range (len(totalDistanceList)):
    rankingList[i][0] = countryList[i]
    rankingList[i][1] = totalDistanceList[i] 
newRankingList=sorted(rankingList, key=lambda x:x[1])
print(newRankingList)



