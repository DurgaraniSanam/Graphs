class Graph:
    def __init__(self,vertices):
        self._adjacency_matrix=[[0] * vertices for _ in range(vertices)]
       
    def add_edge(self,v1,v2):
        self._adjacency_matrix[v1][v2]=1
        self._adjacency_matrix[v2][v1]=1
 
       
    def del_edge(self,v1,v2):
        self._adjacency_matrix[v1][v2]=0
        self._adjacency_matrix[v2][v1]=0
 
    def print_matrix(self):
        for row in self._adjacency_matrix:
           for cell in row:
              print(cell,end=' ')
           print()
     
g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)
print("The Adjacency Matrix.......")
g.print_matrix()

print("After Deleting")
g.del_edge(2,3)
g.print_matrix()
