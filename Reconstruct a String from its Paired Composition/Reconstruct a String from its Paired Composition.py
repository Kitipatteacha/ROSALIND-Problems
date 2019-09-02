import sys
sys.setrecursionlimit(7000)

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

graph = dict()
edge_graph = set()
path = []
startnode = ''
indegree = dict()
outdegree = dict()
f = open("Input.txt", "r")
k = 0
d = 0
for i in f:
    pattern = i.strip('\n').split('|')
    if(len(pattern)==2):
        pattern1 = (pattern[0][:-1],pattern[1][:-1])
        pattern2 = (pattern[0][1:],pattern[1][1:])
        graph[pattern1] = [pattern2]
        indegree[pattern1] = 0
        outdegree[pattern1] = 0
        for i in graph[pattern1]:
            if(i not in graph):
                graph[i] = []
    else:
        k_d = i.strip('\n').split(' ')
        k = k_d[0]
        d = k_d[1]
for i in graph:
    for j in graph[i]:
        if(j in indegree):
            indegree[j] = indegree[j]+1
    outdegree[i] = len(graph[i])
for i in graph:
    if(i in indegree and i in outdegree and outdegree[i]-1 == indegree[i]):
        startnode = i
        break
for i in graph:
    for j in graph[i]:
        if((i,j) not in edge_graph):
            edge_graph.add((i,j))
fleurys_algo(graph,edge_graph,startnode,path)
Ans1 = path[0][0][:int(k)-2]
Ans2 = path[0][1][:int(k)-2]
count = 0;
for i in path:
    count = count + 1
    Ans1 = Ans1 + i[0][int(k)-2:]
    Ans2 = Ans2 + i[1][int(k)-2:]
print(Ans1 + Ans2[len(Ans1)-(int(d)+int(k)):])
