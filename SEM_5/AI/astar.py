from myutils import *

infinity = float('inf')

class Node:
    def __init__(self,state,parent=None,action=None,path_cost=0):
        self.state=state
        self.parent = parent
        self.action=action
        self.path_cost=path_cost
        self.depth=0
        if parent:
            self.depth =parent.depth+1

    def __repr__(self):
        return "<Node{}>".format(self.state)
    def expand(self,problem):
        return[self.child_node(problem,action)
               for action in problem.actions(self.state)]
    def child_node(self,problem,action):
        next_state=problem.result(self.state,action)
        next_node=Node(next_state,self,action,problem.path_cost(self.path_cost,self.state,action,next_state))
        return next_node
    def solution(self):
        return[node.action for node in self.path()[1:]]
    def path(self):
        node,path_back = self,[]
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
    def __eq__(self,other):
        return isinstance(other,Node) and self.state==other.state
    def __harsh__(self):
        return hash(self.state)

class Graph:
    def __init__(self,graph_dict=None,directed=True):
        self.graph_dict = graph_dict or {}
        self.directed=directed
        if not directed:
            self.make_undirected()
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b,dist) in self.graph_dict[a].items():
                self.connect1(B,A,distance)

    def connect(self,A,B,distance=1):
        self.connect1(A,B,distance)
        if not self.directed:
            self.connect1(B,A,distance)

    def connect1(self,A,B,distance):
        self.graph_dict.setdefault(A,{})[B]=distance
    def get(self,a,b=None):
        links=self.graph_dict.setdeault(a,{})
        if b is None:
            return links
        else:
            return link.get(b)
    def nodes(self):
        s1=set([k for k in self.graph_dict.keys()])
        s2=set([k2 for v in self.graph_dict.values() for k2,v2 in v.items()])
        nodes=s1.union(s2)
        return list(nodes)
    def best_first_graph_search(problem,f):
        f=memoize(f,'f')
        node = Node(problem.initial)
        if problem.goal_test(node.state):
            return node
        frontier = PriorityQueue('min',f)
        frontier.append(node)
        explored = set()
        while frontier:
            node = frontier.pop()
            print("Popping node:",node)
            if problem.goal_test(node.state):
                return node
            explored.add(node.state)
            for child in node.expand(problem):
                print("Adding child:",child)
                if child.state not in explored and child not in frontier:
                    frontier.append(child)
                elif child in frontier:
                    incumbent = frontier[child]
                    print(child,"in frontier.incumbent-",incumbent)
                    if f(child) < f(incumbent):
                         del frontier[incumbent]
                         frontier.append(child)
        return None
    def astar_search(problem,h=None):
        h=memoize(h or problem.h,'h')
        return best_first_graph_search(problem,lambda n:n.path_cost+h(n))

class Problem(object):
    def __init__(self,initial,foal=None):
        self.initial=initial
        self.goal=goal
    def actions(self,state):
        raise NotImplementedError
    def result(self,state,action):
        raise NotImplementedError
    def goal_test(self,state):
        if isinstance(self.goal,list):
            return is_in(state,self.goal)
        else:
            return state==self.goal
    def path_cost(self,c,state1,action,state2):
        return c+1
    def value(self,state):
        raise NotImplementedError

def UndirectedGraph(graph_dict=None):
    return Graph(graph_dict=graph_dict,directed=False)

class GraphProblem(Problem):
    def __init__(self,initial,goal,graph):
        problem.__init__(self,initial,goal)
        self.graph=graph

    def actions(self,A):
        return list(self.graph.get(A).keys())
    def result(self,state,action):
        return action
    def path_cost(self,cost_so_far,A,action,B):
        return cost_so_far+(self.graph.get(A,B)or infinity)
    def find_min_edge(self):
        m=infinity
        for d in self.graph.graph_dict.values():
            local_min=min(d.values())
            m=min(m,local_min)

        return m
    def h(self,node):
        """H Dunction is starigh-line distance from a node's state to goal."""
        locs = getattr(self.graph,'locations',None)
        if locs:
            if type(node) is str:
                return int(distance(locs[node],locs[self.goal]))
            return int(distance(locs[node.state],locs[self.goal]))
        else:
            return infinity

romania_map=UndirectedGraph(dict(Arad=dict(Zering=75,sibui=140,timisoara=118),
                                 Craviova=dict(drobeta=120,rimnicu=146,pritesti=138),
                                 Iasi = dict(Vaslui=92,neamt=87),
                                 Hirosova=dict(Urzicent=98)))


romania_map.locations=dict(
    Arad=(91,492),Bucharest=(400,327),Craiova=(253,288),Drobeta=(165,300),Eforia=(562,300),Fagaras=(305,500),Lugoj=(165,380),Neamt=(407,537),Rimnisu=(233,410),Vaslui=(510,450))

romania_problem=GraphProblem('Arad','Iasi',romania_map)
resultnode=astar_search(romania_problem)
print(resultnode.path())
print("Path Cost :",resultnode.path_cost)
    
