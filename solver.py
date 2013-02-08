class node(object):
    """Node Object.  Stores each node's name and neighboring nodes"""
    __slots__=['value','neighbors']
    def __init__(self,value):
        self.value=value
        self.neighbors={}

def solvePuzzle(graph):
    """graph -> Integer"""
    nodes={} #makes empty list of nodes
    for x in range(len(graph)+1):  #makes n+1*m nodes where n is the height of the matrix and m is the length of the matrix
        for y in range(len(graph[0])):
            nodes[(x,y)]=node((x,y))

    """Populates the neighbors.  Neighbors are stored as a dict of {neighbors: weight}"""
    """The First row's neighbors are the ones directly below it to ensure they start on the """
    """correct node, all other nodes' neighbors are the ones below,diagonal below from them, provided they exist"""
    for x in range(len(graph[0])):
        for y in range(len(graph)):
            if(y==len(graph)-1):
                if (y+1,x) in nodes:
                    nodes[y,x].neighbors[(y+1),x]=graph[y][x]          
            else:
                if (y+1,x) in nodes:
                    nodes[y,x].neighbors[(y+1),x]=graph[y][x]
                if (y+1,x+1) in nodes:
                    nodes[y,x].neighbors[(y+1),x+1]=graph[y][x]

                if (y+1,x-1) in nodes:
                    nodes[y,x].neighbors[(y+1),x-1]=graph[y][x]

    #ADJACENCY LIST DONE


    starts=[(0,x) for x in range(len(graph[0]))]  #Get list of all starting nodes
    ends=[(len(graph),x) for x in range(len(graph[0]))] #Get list of all ending nodes

    #Here we begin to convert the adjacency list to a matrix so we can do Warshall's
    l=nodes.keys()
    matrix=[] 

    #iterate through matrix, populating 0s on the diagonals 
    #and 1000 elsewhere.  1000 represents max weight 
    for x in range(len(nodes)):
        row=[]
        for y in range(len(nodes)):
            if x==y:
                row.append(0)
            else:
                row.append(1000)
        matrix.append(row)
    
    l=sorted(l)

    #goes through the matrix again, changing the weights of neighbors to represent their weights
    for i in range(len(l)-1):
        curNode=nodes[l[i]]
        n=curNode.neighbors
        for x in n:
            matrix[i][l.index(x)]=curNode.neighbors[x]
            #matrix[l.index(x)][i]=curNode.neighbors[x]
    #uncomment below to view matrix pre-warshall

    """
    for x in matrix:
        print x
    """    
    matrix=(fw(matrix))

    #uncomment below to view matrix post-warshall

    """
    for x in matrix:
        print x
    """   
    pathValues=[]  #a list which will contain all the possible values from top of the matrix to bot

    for x in starts:
        for y in ends:
            pathValues.append(matrix[l.index(x)][l.index(y)])  #appending all paths from starts to ends

    minimum=min(pathValues)
    return minimum 

def fw(matrix):
    """Performs the Floyd-Warshall algoritm to find the shortest paths in the matrix"""
    """Runtime is O(number of verticies ^ 3) as we have 3 loops through the verticies"""
    """I chose to implement this as our graphs have tons of connections, so I wanted an algoritm"""
    """that only depended on the number of verticies, not edges"""


    """ matrix -> matrix"""
    listLength=len(matrix)
    for i in range(listLength):
        for j in range(listLength):
            for k in range(listLength):
                matrix[i][k] = min(matrix[i][k],matrix[i][j]+matrix[j][k])  #the key step in the algoritm.  replaces a value with the mimimum possible value it can take on.

    return matrix
