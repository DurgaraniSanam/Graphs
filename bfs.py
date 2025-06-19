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
        if vertex not in self.__adjacent_vertex:
            self.__adjacent_vertex.append(vertex)

    def get_adjacent_vertex(self):
        return self.__adjacent_vertex


class BFS:
    def breadth_first_search(self, root):
        queue = [root]
        root.set_visited()
        while queue:
            vertex = queue.pop(0)
            print(vertex.get_name(), end=' ')
            for adj in vertex.get_adjacent_vertex():
                if not adj.get_visited():
                    adj.set_visited()
                    queue.append(adj)


# Step 1: Create vertices
vertices = []
while True:
    print('Enter Vertex name:')
    vertex_name = input().strip()
    vertex = Vertex(vertex_name)
    vertices.append(vertex)
    print('Want to create more vertices? [yes/no]:')
    choice = input().strip().lower()
    if choice == 'no':
        break

# Step 2: Add adjacent vertices
print('\nAdd Adjacent vertices!')
for vertex in vertices:
    print(f"\nSpecify the adjacent vertices for vertex '{vertex.get_name()}':")
    while True:
        print('Adjacent Vertex name:', end=' ')
        v_name = input().strip()
        matched = False
        for v in vertices:
            if v_name == v.get_name():
                vertex.add_adjacent_vertex(v)
                matched = True
                break
        if not matched:
            print(f"No such vertex named '{v_name}' found.")
        print('Any more adjacent vertices? [yes/no]:')
        option = input().strip().lower()
        if option == 'no':
            break

# Step 3: Perform BFS from the first vertex
print('\nBFS Traversal Output:')
bfs = BFS()
bfs.breadth_first_search(vertices[0])
