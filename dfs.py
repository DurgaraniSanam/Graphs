class Vertex:
    def __init__(self,name):
        self.__name=name
        self.__visited=False
        self.__adjacent_vertex=[]
    
    def get_name(self):
        return self.__name
    
    def set_visited(self):
        self.__visited=True
    
    def get_visited(self):
        return self.__visited
    
    def add_adjacent_vertex(self,vertex):
        self.__adjacent_vertex.append(vertex)
        
    def get_adjacent_vertices(self):
        return self.__adjacent_vertex
    
    
class DFS:
    def depth_first_search(self,root):
        stack=[root]
        root.set_visited()
        while stack:
            vertex=stack.pop()
            print(vertex.get_name(),end=' ')
            for adj in vertex.get_adjacent_vertices():
                if not adj.get_visited():
                    adj.set_visited()
                    stack.append(adj)
            

# Creating vertices
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')
f = Vertex('F')
g = Vertex('G')
h = Vertex('H')



a.add_adjacent_vertex(b)
a.add_adjacent_vertex(f)
a.add_adjacent_vertex(g)

b.add_adjacent_vertex(a)
b.add_adjacent_vertex(c)
b.add_adjacent_vertex(d)


c.add_adjacent_vertex(b)
c.add_adjacent_vertex(e)

d.add_adjacent_vertex(b)
d.add_adjacent_vertex(e)

e.add_adjacent_vertex(c)
e.add_adjacent_vertex(d)
e.add_adjacent_vertex(h)

f.add_adjacent_vertex(a)

g.add_adjacent_vertex(a)
g.add_adjacent_vertex(h)

h.add_adjacent_vertex(g)
h.add_adjacent_vertex(e)


dfs = DFS()
dfs.depth_first_search(a)  

        