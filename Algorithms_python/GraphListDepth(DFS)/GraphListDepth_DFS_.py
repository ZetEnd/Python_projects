from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, visited, v):

        visited.add(v)
        print(v, end = " ")

        for near in self.graph[v]:
            if near not in visited:
                self.DFSUtil(visited, near)


    def DFS(self, v):

        visited = set()

        self.DFSUtil(visited, v)

if __name__ == "__main__":

    g = Graph()
    g.add_edge(0,1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("research the graph in depth")
    g.DFS(2)