# class Node
# {
# 	int Id;
# }
#
# class Edge
# {
#   int Start;
#   int End;
# }
#
# class Graph
# {
# 	List<Node> Nodes;
#   List<Edge> Edges;
# }
#
# List<Graph> GetSubgraphs(Graph graph)
class Node(object):
    def __init__(self, id):
        self.Id = id

class Edge(object):
    def __init__(self, start, end):
        self.Start = start
        self.End = end

class Graph(object):
    def __init__(self, nodes, edges):
        self.Nodes = nodes
        self.Edges = edges

class GetSubgraphs(object):
    def __init__(self):
        self.visited = set()
        self.edges = {}
        self.res = []
        self.queue = []

    def getSubgraphs(self, graph):
        edges = graph.Edges

        for edge in edges:
            s = edge.start
            e = edge.end
            # get mapping of start => [end1, end2]
            if s not in self.edges:
                self.edges[s] = [e]
            else:
                self.edges[s].append(e)

        nodes = graph.Nodes
        for node in nodes:
            # tmp will be a list of nodes that connected
            tmp = []
            if node.Id not in self.visited:
                self.queue = [node]
                self.visited.add(node.Id)
                # BFS
                while self.queue:
                    currNode = self.queue.pop(0)
                    self.visited.add(currNode.Id)
                    tmp.append(currNode)
                    # loop through edges
                    for neighboor in self.edges[currNode.Id]:
                        if neighboor not in self.visited:
                            self.queue.append(neighboor)
            self.res.append(self.recreateGraph(tmp))

        return self.res

    # Use connected nodes and self.edges (mapping of start => [end]) to recreate graph
    def recreateGraph(self, nodes):
        edges = []
        for node in nodes:
            if node.Id in self.edges:
                s = node.Id
                for e in self.edges[node.Id]:
                    edges.append(Edge(s, e))

        return Graph(nodes, edges)
