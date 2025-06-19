import collections
class BFS:
    def breadth_first_search(self, graph,root):
        visited, queue = set(), collections.deque(root)
        while queue:
            vertex = queue.popleft()
            visited.add(vertex)
            print(vertex, end = " ")
            for adj_vertex in graph[vertex]:
                if adj_vertex not in visited:
                    visited.add(adj_vertex)
                    queue.append(adj_vertex)

g = {
    'A' : ['B', 'F','G'],
    'B' : ['A', 'C','D'],
    'C' : ['B', 'E'],
    'D' : ['B','E'],
    'E' : ['C', 'D','H'],
    'F' : ['A'],
    'G' : ['A', 'H'],
    'H': ['G', 'E']
}
b = BFS()
b.breadth_first_search(g,'A') 
