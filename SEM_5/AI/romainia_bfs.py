#bfs for romanian problem

graph = {
    'Aard':['Zerind','Timinsoa','Sibui']}

pc={
    ('Arad','Zerind'):75,('Arad','Timisoa'):140}
locs={'Arad':366,'Bucharest':0}



def BFS(g,v,goal,explored,path_so_far,m):
    """Return path from v to goal in g as a staring(Hack)"""
    explored.add(v)
    node=[]
    if v ==goal:
        return path_so_far+v
     for w in g[v]:
         if w not in explored:
             f=locs.get(w)+pc.get((v,w))
             if m>f:
                 m=f
                 print("%i%s%s"%(m,v,w))
                 node=w
    p=DFS(g,node,goal,explored,path_so_far+v+'->',m)
    if p:
        return p
    return ""

print(DFS(graph,'Star','Goal',set(),"",1000))
