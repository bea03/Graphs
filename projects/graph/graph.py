"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        self.vertices[vertex_id] = set()     

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #make queue
        q = Queue()
        #enqueue our starting node
        q.enqueue(starting_vertex)

        #make a set to track if we've been here before
        visited = set()
        
        #while queue isn't empty
        while q.size() > 0:
            #dequeu whatever's at the front of the line, this current_node
            current_node = q.dequeue()
            #if we haven't visited node yet,
            if current_node not in visited:
                print(current_node)
                #mark as visited
                visited.add(current_node)
                #get its neighbors
                neighbors = self.get_neighbors()
                #for each of the neighbors add to queue
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO
        #make a stack
        s = Stack()
        #push on our starting node
        s.push(starting_vertex)
        #make a set to track if we've been here before
        visited = set()
        #while our stack isn't empty
        while s.size() > 0:
        #pop off w/e on top, this is current node
            current_node = s.pop()
        #if havn't visited
            if current_node not in visited:
        #mark as visited
                print(current_node)
                visited.add(current_node)
        #get its neighbors
        #for each neighbor add to stack
                for neighbor in self.get_neighbors(current_node):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #make it visited if not yet
        if visited is None:
            visited = set()

        # base case:
        # no more neighbors

        # track visited nodes
        visited.add(vertex)
        print(vertex)

        # call the function recursively - on neighbors of not visited
        for neighbor in self.vertices[vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue...
        qq = Queue()

        # ...and enqueue A PATH TO the starting vertex ID
        print(qq.enqueue([starting_vertex]))

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while qq.size() > 0:
            # Dequeue the first PATH
            path = qq.dequeue()
            print(path)

            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            print(last_vertex)

            # If that vertex has not been visited...
            if last_vertex not in visited:
                # Mark it as visited...
                visited.add(last_vertex)
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                    # IF SO, RETURN PATH
                    return path

            # Then add A PATH TO its neighbors to the back of the queue
            for next_vert in self.get_neighbors(last_vertex):
                # COPY THE PATH
                new_path = list(path)
                # APPEND THE NEIGHOR TO THE BACK
                new_path.append(next_vert)
                qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # initialize empty list
        path = []
        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty...
        while s.size() > 0:
            # pop the first PATH
            # Grab the last vertex from the PATH
            vert = s.pop()
            # If that vertex has not been visited...
            if vert not in visited:
                print(vert)
                # Mark it as visited...
                visited.add(vert)
                path.append(vert)

                # CHECK IF IT'S THE TARGET
                if vert == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Then add A PATH TO its neighbors to the back of the stack
                for next_vert in self.get_neighbors(vert):
                    # APPEND THE NEIGHOR TO THE BACK
                    s.push(next_vert)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initial case needed
        # if we do not have a visited in place initialize it
        if visited is None:
            # add a set() to the visited vertex
            visited = set()

        if path is None:
            path = []

        # base case needed as well - how do we know we are done?
        # when we have no more neighbors
        # no explicit base case here bc we are handling that in our for loop below `self.dft_recursive(neighbor, visited)`

        # track visited nodes
        visited.add(starting_vertex)
        # copy the path
        new_path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return new_path

        # call the function recursively - on neighbors of not visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, new_path)
                if neighbor_path:
                    return neighbor_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
