Understand:
        Graph contains 500 rooms. must visit every room once and with the fewest moves (at least 2000 or less for MVP)
        run a traversal and build a graph
Plan:
BFT, use a dictionary as visited
building graph as we go

        nodes: Rooms  (room)
        edges: connected n/s/e/w
        
        dictionary: 
            key = room
            values = direction with its ? default then room num or none

        finished when graph has no ? (that means not explored) and 0-499 rooms

Has it been explored?
    if no: preform BFS with this as starting node
    yes: next node

    


