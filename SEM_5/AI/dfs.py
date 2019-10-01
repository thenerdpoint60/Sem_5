g={'A':{'B','C'},
   'B':{'A','D','E'},
   'C':{'A','C'},
   'D':{'B','G'}}

def dfs(g,s,goal):
    explored=[]
    queue=[s]
    while queue:
        node=queue.pop(len(queue)-1)
        if node not in explored:
            explored.append(node)
            neis=g[node]
            for nei in neis:
                queue.append(nei)
            if goal==node:
                break
    return explored

print(dfs(g,'A','D'))
