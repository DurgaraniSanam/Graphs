from collections import defaultdict

class Vertex():
    def __init__(self,name):
         self.__name=name
    def get_name(self):
        return self.__name
    
class Graph():
    def __init__(self):
        #Creates a dictionary which stores the values in the form of a list
        self.__adjacency_list=defaultdict(list)
        
    def add_adjacent_vertex(self,source_vertex,dest_vertex):
        self.__adjacency_list[source_vertex].append(dest_vertex)
        self.__adjacency_list[dest_vertex].append(source_vertex)
    
    
    def print_adjacency_list(self):
        print("The Adjacency List")
        for key,value in self.__adjacency_list.items():
            print(key.get_name() ,":",end=' ')
            for v in value:
                print(v.get_name(),end=' ')
            print()


a=Vertex('A')
b=Vertex('B')
c=Vertex('C')
d=Vertex('D')
e=Vertex('E')


g=Graph()
g.add_adjacent_vertex(a,b)
g.add_adjacent_vertex(a,c)
g.add_adjacent_vertex(a,d)
g.add_adjacent_vertex(b,c)
g.add_adjacent_vertex(b,d)
g.add_adjacent_vertex(c,d)
g.add_adjacent_vertex(d,e)



print("The Adjacency List....")
g.print_adjacency_list()
