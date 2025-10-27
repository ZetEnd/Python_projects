class Graph:
    def __init__(self, numvertex):
        self.adj_matrix = [[-1]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {}
        self.verticeslist = [0]*numvertex

    def set_vertex(self, vtx, id):
        if 0<= vtx <= self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id

    def set_edge(self, frm, to, cost = 0):
        frm = self.vertices[frm]
        to = self.vertices[to]

        self.adj_matrix[frm][to] = cost

        self.adj_matrix[to][frm] = cost

    def get_vertex(self):
        return self.verticeslist

    def get_edges(self):
        edge = []

        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if(self.adj_matrix[i][j] != -1):
                    edge.append((self.verticeslist[i],
                                self.verticeslist[j],
                                self.adj_matrix[i][j]))

        return edge

    def get_matrix(self):
        return self.adj_matrix



if __name__ == "__main__":

    G = Graph(6)

    G.set_vertex(0,'a')
    G.set_vertex(1,'b')
    G.set_vertex(2,'c')
    G.set_vertex(3,'d')
    G.set_vertex(4,'e')
    G.set_vertex(5,'f')
    G.set_edge('a','e',10)
    G.set_edge('a','c',20)
    G.set_edge('c','b',30)
    G.set_edge('b','e',40)
    G.set_edge('e','d',50)
    G.set_edge('f','e',60)

    print("graph vertex:")
    print(G.get_vertex())

    print("graph edges:")
    print(G.get_edges())

    print("matrix:")
    print(G.get_matrix())