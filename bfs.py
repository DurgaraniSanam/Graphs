class Vertex:
    def __init__(self, name):
        self.__name = name
        self.__visited = False
        self.__adjacent_vertex = []

    def get_name(self):
        return self.__name

    def set_visited(self):
        self.__visited = True

    def get_visited(self):
        return self.__visited

    def add_adjacent_vertex(self, vertex):
        self.__adjacent_vertex.append(vertex)

    def get_adjacent_vertex(self):
        return self.__adjacent_vertex


class BFS:
    def breadth_first_search(self, root):
        que = [root]
        root.set_visited()
        while que:
            vertex = que.pop(0)
            print(vertex.get_name(), end=' ') 
            for adj in vertex.get_adjacent_vertex():
                if not adj.get_visited():
                    adj.set_visited()
                    que.append(adj)


# Creating vertices
# a = Vertex('A')
# b = Vertex('B')
# c = Vertex('C')
# d = Vertex('D')
# e = Vertex('E')
# f = Vertex('F')
# g = Vertex('G')
# h = Vertex('H')

vertices=[]
while True:
    print('Enter Vertex name')
    vertex_name=input()
    vertex = Vertex(vertex_name)
    vertices.append(vertex)
    print('Want to create more [yes/no]:')
    choice=input()
    if choice=='no':
        break

print('Add Adjacent vertices!')
for vertex in vertices: 
    print('specify the adjacent vertices of vertex : ',vertex.get_name())
    while True:
        print('Vertex name: ',end=' ')
        v_name=input()
        for v in vertices:
            if v_name==v.get_name():
                vertex.add_adjacent_vertex(v)
        print('Any more adjacent vertices:  [yes/no]')
        option=input()
        if option=='no':
            break            
                    
# vertices=['A','B','C','D','E','F','G','H']
# graph={}

# for v in vertices:
#     graph[v.lower]=Vertex(v)


# Creating edges (undirected)
# graph[a].add_adjacent_vertex(graph[b])
# graph[a].add_adjacent_vertex(graph[f])
# graph[a].add_adjacent_vertex(graph[g])

# graph[b].add_adjacent_vertex(graph[a])
# graph['b'].add_adjacent_vertex(graph[c])
# graph['b'].add_adjacent_vertex(graph[d])


# a.add_adjacent_vertex(b)
# a.add_adjacent_vertex(f)
# a.add_adjacent_vertex(g)

# b.add_adjacent_vertex(a)
# b.add_adjacent_vertex(c)
# b.add_adjacent_vertex(d)


# c.add_adjacent_vertex(b)
# c.add_adjacent_vertex(e)

# d.add_adjacent_vertex(b)
# d.add_adjacent_vertex(e)

# e.add_adjacent_vertex(c)
# e.add_adjacent_vertex(d)
# e.add_adjacent_vertex(h)

# f.add_adjacent_vertex(a)

# g.add_adjacent_vertex(a)
# g.add_adjacent_vertex(h)

# h.add_adjacent_vertex(g)
# h.add_adjacent_vertex(e)


bfs = BFS()
bfs.breadth_first_search(vertices[0])  
