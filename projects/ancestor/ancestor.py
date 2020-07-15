'''Plan
    nodes: people
    edges: when child has a parent
    DFS
    add stack to this as well
'''
class Graph:
        def __init__(self):
            self.vertices = {}
        
        def add_vertex(self, vertex):
            if vertex not in self.vertices:
                self.vertices[vertex] = set()

        def add_edge(self, v1, v2):
            self.vertices[v1].add(v2)

        def get_neighbors(self, vertex):
            return self.vertices[vertex]

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.enqueue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

    #bulid a path we would like to search
    
def build_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    return graph

def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)

    s = Stack()
    visited = set()

    s.push([starting_node])
    
    longest_path = []
    #no ancestor
    aged_one = -1

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]
        
        #if path longer or equal but the value is smaller
        if len(path) > len(longest_path) or (len(path) == len(longest_path) and current_node < aged_one):
            longest_path = path
            aged_one = longest_path[-1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)
    
    return longest_path[-1]

#as we pass through, keep track of longest path seen so far