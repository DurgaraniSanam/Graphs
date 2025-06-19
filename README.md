# Graph Data Structure
Graph Data Structure is a non-linear data structure consisting of vertices and edges. It is useful in fields such as social network analysis, recommendation systems, and computer networks. In the field of sports data science, graph data structure can be used to analyze and understand the dynamics of team performance and player interactions on the field.


# What is a Graph Data Structure
Graph is a non-linear data structure consisting of vertices and edges. The vertices are sometimes also referred to as nodes and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph is composed of a set of vertices( V ) and a set of edges( E ). The graph is denoted by G(V, E).


# Componenets of Data Structure
- ### Vertices :
   Vertices are the fundamental units of the graph. Sometimes, vertices are also known as vertex or nodes. Every node/vertex can be labeled or unlabelled.
- ### Edges    :
   Edges are drawn or used to connect two nodes of the graph. It can be ordered pair of nodes in a directed graph. Edges can connect any two nodes in any possible way. There are no rules. Sometimes, edges are also known as arcs. Every edge can be labelled/unlabelled.
## 🧠 Types of Graphs

- **Undirected Graph**: The edges do not have direction.
- **Directed Graph (Digraph)**: Each edge has a direction from one vertex to another.
- **Weighted Graph**: Each edge has an associated numerical value (weight).
- **Unweighted Graph**: All edges are equal; no weights involved.

## 🧱 Graph Representations

| Representation      | Description |
|---------------------|-------------|
| **Adjacency List**  | Dictionary where keys are nodes and values are lists of neighbors. Efficient for sparse graphs. |
| **Adjacency Matrix**| 2D array where cell (i, j) shows connection (or weight) from node i to node j. Efficient for dense graphs. |
| **Edge List**       | A list of all graph edges. Each edge is a pair (or triplet for weighted). Useful for algorithms like Kruskal’s. |

---

### 🔍 Example: Adjacency List (Undirected)
```python
{
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['A'],
  'D': ['B']
}
