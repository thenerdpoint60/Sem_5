g={'A':{'B','C'},
   'B':{'A','D','E'},
   'C':{'A','C'},
   'D':{'B','G'}}



def bfs(g,s,goal):
    explored=[]
    queue=[s]
    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            neis=g[node]
            for nei in neis:
                queue.append(nei)
            if goal==node:
                break
    return explored

print (bfs(g,'A','C'))
