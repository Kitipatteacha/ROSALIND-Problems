import sys
sys.setrecursionlimit(6000)

def fleurys_algo(graph,edge_graph,current,path):
    path.append(current)
    found = False
    for node in graph[current]:
        edge = (current,node)
        if(edge in edge_graph):
            edge_graph.remove(edge)
            if(checkgraph(graph,edge_graph,node)):
                found = True
                fleurys_algo(graph,edge_graph,node,path)
            else:
                edge_graph.add(edge)
    if not found:
        for node in graph[current]:
            edge = (current,node)
            if(edge in edge_graph):
                edge_graph.remove(edge)
                fleurys_algo(graph,edge_graph,node,path)
    

def dfs(graph,edge_graph,visited,current):
    visited.add(current)
    for node in graph[current]:
        edge = (current,node)
        if(edge in edge_graph and node not in visited):
            dfs(graph,edge_graph,visited,node)
def checkgraph(graph,edge_graph,current):
    reachable_nodes = set()
    for edge in edge_graph:
            reachable_nodes.add(edge[0])
            reachable_nodes.add(edge[1])
    visited = set()
    dfs(graph,edge_graph,visited,current)
    return reachable_nodes == visited
    

    
g = dict()
edge_graph = set()
path = []
startnode = ''
indegree = dict()
outdegree = dict()
Ans = ''
f = open("Input.txt", "r")
for i in f:
    nodes = i.split("->")
    node = nodes[0].strip()
    nextnode = []
    for n in nodes[1].strip().split(','):
        nextnode.append(n.strip())
    g[node] = nextnode
    indegree[node] = 0
    outdegree[node] = len(g[node])
    for i in g[node]:
        if(i not in g):
            g[i] = []
        edge_graph.add((node,i))
for i in g:
    for j in g[i]:
        if(j in indegree):
            indegree[j] = indegree[j]+1
for i in g:
    if(i in indegree and i in outdegree and outdegree[i]-1 == indegree[i]):
        startnode = i
        break
fleurys_algo(g,edge_graph,startnode,path)
for i in range (len(path)):
    Ans = Ans + path[i]
    if(i != len(path)-1):
        Ans = Ans + '->'
print(Ans)
