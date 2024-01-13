
import numpy as np
from queue import Queue
from collections import deque


# def BFS(adjacency_list):
#     #all nodes start as not visited so value is zero
#     #this is to keep track of whether or not a node has been visited
#     visited_nodes= np.zeros(len(adjacency_list))
#     #when visited, change value of queue[vertex-1] to '1'

#     myqueue= Queue() #queue with vertices that i'll work with

#     output= Queue() #the output of visited nodes in order

#     output.put(adjacency_list[])



def BFS(adjacency_list):
    #all nodes start as not visited so value is zero
    #this is to keep track of whether or not a node has been visited
    visited_nodes= np.zeros(len(adjacency_list))
    #when visited, change value of queue[vertex-1] to '1'

    #here we initialise parent of each node to be -1
    parent_nodes = [-1] * len(adjacency_list) 

    myqueue=[] #queue with vertices that i'll work with
    # myqueue= deque(1)
    # print("my queue")
    # print(myqueue)

    output= [] #the output of visited nodes in order

    myqueue.append(1)


    while(len(myqueue)>0): #while i still have nodes to traverse
        current_vertex=myqueue.pop(0) #dequeue first element
        if (visited_nodes[current_vertex-1]==0):
            visited_nodes[current_vertex-1]=1 #set it to visited
            output.append(current_vertex)
            #then queue its edges
            #this sorts them before enqueuing so that i visit smaller value nodes first
            adjacent_nodes=sorted(adjacency_list[current_vertex-1])
            for element in adjacent_nodes:
                # myqueue.append(element)
                if visited_nodes[element-1] == 0:
                     if (not (element in myqueue)):
                         parent_nodes[element-1] = current_vertex
                     myqueue.append(element)
                     if(current_vertex==3):
                        print(parent_nodes[element-1])           
                     if(current_vertex==3):
                        print(parent_nodes[element-1])
                    

               

    return output, parent_nodes



def DFS(adjacency_list):
        #all nodes start as not visited so value is zero
    #this is to keep track of whether or not a node has been visited
    visited_nodes = np.zeros(len(adjacency_list))
    #when visited, change value of queue[vertex-1] to '1'

    #here we initialise parent of each node to be -1
    parent_nodes = [-1] * len(adjacency_list) 

    mystack = []  # Stack with vertices that I'll work with
    output = [] #the output of visited nodes in order

    mystack.append(1)

    while len(mystack) > 0: #while i still have nodes to traverse
        current_vertex = mystack.pop()  # pop the last element 
        if visited_nodes[current_vertex-1] == 0:
            visited_nodes[current_vertex-1] = 1
            output.append(current_vertex)

            #sorting nodes before appending them so that i visit them in order of
            #smallest number node first
            adjacent_nodes = sorted(adjacency_list[current_vertex-1], reverse=True)
            for element in adjacent_nodes:
                if visited_nodes[element-1] == 0:
                    # if (not (element in mystack)):
                    parent_nodes[element-1] = current_vertex
                  #  parent_nodes[element-1] = current_vertex
                    mystack.append(element)

    return output, parent_nodes


def finding_cycles(adjacency_list):
    num_vertices = len(adjacency_list)
    visited = [False] * num_vertices
    cycles = []

    def dfs(node, current_cycle):
        nonlocal visited, cycles

        visited[node] = True
        current_cycle.append(node+1)

        for neighbor in adjacency_list[node]:
            if not visited[neighbor-1]:
                if dfs(neighbor-1, current_cycle):
                    return True
            elif neighbor in current_cycle:
                # If the neighbor is in the current cycle, then there is a cycle
                # if (neighbor==1):
                index = current_cycle.index(neighbor)
                cycle1=current_cycle[index:]
                if (len(cycle1)>1):
                    cycle = current_cycle[index:] + [current_cycle[index]]
                    cycles.append(cycle)

               

        current_cycle.pop()  # Remove the node from the current cycle
        # visited[node] = False  # Mark the node as unvisited
        return False

    for vertex in range(num_vertices):
        if not visited[vertex]:
            dfs(vertex, [])

    return cycles



def isBipartite(adjacency_list):
    #this function takes an adjacency list of a graph, finds its cycles and 
    #finds if it contains any odd-length cycles
    cycles= finding_cycles(adjacency_list)
    for i in range(len(cycles)):
        if ((len(cycles[i])-1 %2)==1):
            return False
    
    return True


def print_BFSTree(parent_nodes):
    for index, element in enumerate(parent_nodes):
        print("Node: ")
        print(index+1)
        print("has parent: ")
        print(element)

def print_DFSTree(parent_nodes):
    for index, element in enumerate(parent_nodes):
        print("Node: ")
        print(index+1)
        print("has parent: ")
        print(element)

#input list
adjacency_list = [
    [3, 4], #edges of vertex 1
    [2, 3], #edges of vertex 2
    [4],    #edges of vertex 3
    [1, 2]  #edges of vertex 4
]



# print(adjacency_list[0])


# Dequeue and print each element

# output= BFS(adjacency_list)
# while not output.empty():
#     print(output.get())

# output, parents= BFS(adjacency_list)
# print("outputs")
# print(output)
# print("parent nodes")
# print(parents)
# print_BFSTree(parents)

# output2, parents2= DFS(adjacency_list)
# print("outputs")
# print(output2)
# print("parent nodes")
# print(parents2)
# print_BFSTree(parents2)
# print(finding_cycles(adjacency_list))
# BFS(adjacency_list)
# print(isBipartite(adjacency_list))