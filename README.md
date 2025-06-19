# Graph Data Structure
Graph Data Structure is a non-linear data structure consisting of vertices and edges. It is useful in fields such as social network analysis, recommendation systems, and computer networks. In the field of sports data science, graph data structure can be used to analyze and understand the dynamics of team performance and player interactions on the field.


# What is a Graph Data Structure
Graph is a non-linear data structure consisting of vertices and edges. The vertices are sometimes also referred to as nodes and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph is composed of a set of vertices( V ) and a set of edges( E ). The graph is denoted by G(V, E).


# Componenets of Data Structure
- ### Vertices :
   Vertices are the fundamental units of the graph. Sometimes, vertices are also known as vertex or nodes. Every node/vertex can be labeled or unlabelled.
- ### Edges    :
   Edges are drawn or used to connect two nodes of the graph. It can be ordered pair of nodes in a directed graph. Edges can connect any two nodes in any possible way. There are no rules. Sometimes, edges are also known as arcs. Every edge can be labelled/unlabelled.

  
## 📊 Types of Graphs

### ➤ Based on Direction:
- **Undirected Graph**:  
  Edges have no direction.  
  Example: A—B means A is connected to B and vice versa.
  
- **Directed Graph (Digraph)**:  
  Edges have a direction.  
  Example: A → B (from A to B only).

### ➤ Based on Weight:
- **Weighted Graph**:  
  Edges have weights/costs.  
  Example: A → B (weight = 5)

- **Unweighted Graph**:  
  All edges are equal; no weights.

### ➤ Special Types:
- **Cyclic / Acyclic Graph**: Whether the graph has loops.
- **Connected / Disconnected**: Whether every vertex is reachable from any other.
- **Tree**: A special type of acyclic connected graph.
- **Multigraph**: May have multiple edges between the same pair of nodes.

---

## 📐 Graph Representations

### ✅ Adjacency List
Efficient for sparse graphs. Stores neighbors for each vertex.

```python
graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['A'],
  'D': ['B']
}
### 2. **Adjacency Matrix:**
A 2D matrix where `matrix[i][j]` is 1 (or weight) if there is an edge from vertex `i` to vertex `j`.

### 3. **Edge List:**
A list of all edges represented as pairs (or triplets if weighted) of vertices.

---

## 🔁 Graph Traversal Algorithms

Traversal means visiting all vertices in a systematic way.

### ➤ Breadth-First Search (BFS):
- Explores the graph level by level.
- Best for finding the shortest path in unweighted graphs.

### ➤ Depth-First Search (DFS):
- Explores as deep as possible along each branch before backtracking.
- Useful in cycle detection and topological sorting.

---

## 🚦 Dijkstra’s Algorithm

- Used to find the shortest path from a single source to all other nodes in a **weighted** graph with **non-negative weights**.
- It uses a priority queue to always explore the shortest known distance.

---

## 🎯 Real-World Applications of Graphs

| Domain | Application |
|--------|-------------|
| Social Networks | Modeling friendships, followers, and communities |
| Web Crawling | Pages as nodes, hyperlinks as edges |
| Routing & Navigation | Maps, GPS systems (e.g., Google Maps) |
| Sports Analytics | Player movement, passes, and teamwork analysis |
| Recommendation Systems | Connecting users with similar interests |
| Biology | Gene regulation networks, protein interactions |
| Telecommunications | Network routing, traffic modeling |

---

## 🏟️ Sports Data Science Use Case

In sports analytics, graphs can model player interactions and team dynamics:
- **Nodes** = players
- **Edges** = passes/interactions
- **Weights** = number of passes, success rate, etc.

This helps:
- Analyze team connectivity
- Find key players (centrality)
- Visualize strategies and weaknesses

---

## ⚙️ Getting Started

To use this repository:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/graphs.git
   cd graphs
Read through the examples
This repository provides structured explanations and examples to help you learn graph theory with Python.

