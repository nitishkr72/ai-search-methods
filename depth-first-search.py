#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:38:47 2020

@author: Nitish Kumar

moveGen(Node N) & goalTest(Node N) is a user given function
dfs function will find the possible path from start Node to goal node7

(this may not be the shortest possible path) ...
"""

#to test algorithm uncomment one of the movegen,
#strtNode, GoalNode and commentout user-input--
#moveGen = {'S':['A','B','C'],'A':['S','B','D'],'B':['S','A','D'],'C':['S','G'],'D':['A','B','E'],'E':['D','G'],'G':['C','E']}
#moveGen = {'S': ['A','B','D'],'A':['C','B','S'],'B':['S','A','C'],'C':['B','A'],'D':['S','G'],'G':['D']}
#startNode = 'S'
#goalNode = 'G'



##user-input--
def userInput():
    ls = {}
    print('Enter the number of node: ', end='')
    nodes = int(input())
    while nodes!=0:
        print('Enter Node: ', end='')
        Node = input()
        print('Enter the edges from Node: ', end='')
        ls[Node] = list(map(str, input().split()))
        nodes = nodes - 1
    return ls

moveGen = userInput()
print('Enter the starting Node: ', end='')
startNode = input()
print('Set Goal to Node: ', end='')
goalNode = input()
##end-of-user-input--


#user-provided-data--
def goalTest(N):
    return True if N == goalNode else False

#end-of-user-provided-function--

##dfs-search-algorithm--

def ReconstructPath(node, OPEN, parent):
    OPEN = OPEN + [[node, parent, 1]]
    return OPEN

def RemoveSeen(CHILD, OPEN):
    ls = []
    ls_OPEN = []
    for nodePair in OPEN:
        ls_OPEN = OPEN[0]
        
    for i in CHILD:
        if i not in ls_OPEN:
            ls.append(i)
    return ls

def makePairs(newNodes, node, status):
    ls = []
    for i in range(len(newNodes)):
        ls.append([newNodes[i], node, status])
    return ls


#depth first search algorithm..
def dfs():
    count = 0
    OPEN = [[startNode, '', 0]]        # open contain nodeTuple =
                                       # [node, itsParent, status]
    while len(OPEN) != 0:
        [node, parent, nodeStatus] = OPEN.pop()
        
        if goalTest(node):
            return ReconstructPath(node, OPEN, parent)
        elif nodeStatus == 1:
            OPEN = OPEN[: len(OPEN)-1]
        else:
            OPEN = OPEN[: len(OPEN)-1]
            OPEN = OPEN + [[node, parent, 1]]
            CHILD = moveGen[node]
            newNodes = RemoveSeen(CHILD, OPEN)
            newPairs = makePairs(newNodes, node, 0)
            OPEN = OPEN + newPairs
            count = count + len(newPairs)
    return OPEN

print(dfs())