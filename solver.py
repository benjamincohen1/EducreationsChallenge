def initialize(graph, source):
    dest = {} # Stands for destinations
    pred = {} # Stands for predecessors
    for node in graph:
        dest[node] = float('Inf') # start by assuming all nodes are infinity away
        pred[node] = None  #each node has no predicesor
    dest[source] =0
    return dest, pred
 
def relax(node, neighbour, graph, dest, pred):
    """ Checks if the distance from a node to it's neighbour is lower than our current one"""
    if dest[neighbour] > dest[node] + graph[node][neighbour]:
        pred[neighbour] = node
        dest[neighbour]  = dest[node] + graph[node][neighbour]
 
def bellman_ford(graph, source):
    """This is the main part of the algorithm"""
    """ It initializes, then for each thing in the graph, relaxes it"""
    """ Meaning that it finds the shortest neighbour away """
    dest, pred = initialize(graph, source)  
    for x in range(len(graph)-1): 
        for y in graph:
            for z in graph[y]: 
                relax(y, z, graph, dest, pred) 

    return dest, pred

def solvePuzzle(graph):
    """graph -> Integer"""
    """Populates the neighbors.  Neighbors are stored as a dict of {neighbors: weight}"""
    """The First row's neighbors are the ones directly below it to ensure they start on the """
    """correct node, all other nodes' neighbors are the ones below,diagonal below from them, provided they exist"""
    nodes={} #makes empty list of nodes
    for x in range(len(graph)+1):  #makes n+1*m nodes where n is the height of the matrix and m is the length of the matrix
        for y in range(len(graph[0])):
            nodes[(x,y)]={}
    
    for x in range(len(graph[0])):
        for y in range(len(graph)):
            if(y==len(graph)-1):
                if (y+1,x) in nodes:
                    nodes[y,x][(y+1),x]=graph[y][x]          
            else:
                if (y+1,x) in nodes:
                    nodes[y,x][(y+1),x]=graph[y][x]
                if (y+1,x+1) in nodes:
                    nodes[y,x][(y+1),x+1]=graph[y][x]

                if (y+1,x-1) in nodes:
                    nodes[y,x][(y+1),x-1]=graph[y][x]

    #ADJACENCY LIST DONE


    starts=[(0,x) for x in range(len(graph[0]))]  #Get list of all starting nodes
    ends=[(len(graph),x) for x in range(len(graph[0]))] #Get list of all ending nodes
    #Initialize all of the things we need to track as empty
    distances=[]
    paths={}
    minDistance=1000
    bestEnd=x
    bestD=""
    bestP=""
    bestStart=""
    for start in starts:
        d,p=bellman_ford(nodes,start)
        for x in ends:
            #for each start and end, we want to check if the path length is our best yet, and replace our mins if it is
            if(d[x]<minDistance):
                bestStart=start
                bestEnd=x
                bestP=p
                minDistance=d[x]
                bestD=d

    curNode=bestEnd
    path=[bestEnd]
    #Goes from end to start building a path
    while(bestP[curNode]!=None):
        path.append(bestP[curNode])
        curNode=bestP[curNode]
    lastPath=[]
    #Equates each element in path with one in the initial graph
    for x in path[1:]:
        XVAL=x[0]
        YVAL=x[1]
        lastPath.append(graph[XVAL][YVAL])
    lastPath.reverse()  #reverses the path so it's in the right order

    return minDistance,lastPath  #All done, returns!
