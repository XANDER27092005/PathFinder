from collections import deque
# Define the graph
d = {
    'victoria island': ['lekki', 'ikoyi', 'lagos island', 'oniru'],
    'lekki': ['victoria island', 'ajah', 'epe'],
    'ikoyi': ['victoria island', 'lagos island', 'obalende'],
    'lagos island': ['victoria island', 'apapa', 'ikeja'],
    'ajah': ['lekki', 'sangotedo'],
    'epe': ['lekki'],
    'yaba': ['ikoyi', 'surulere', 'lagos mainland', 'ebute metta'],
    'surulere': ['ikoyi', 'yaba', 'mushin'],
    'apapa': ['lagos island', 'festac'],
    'ikeja': ['lagos island', 'maryland', 'ogba'],
    'sangotedo': ['ajah', 'lekki'],
    'lagos mainland': ['yaba', 'ojuelegba', 'ebute metta'],
    'mushin': ['surulere', 'oshodi'],
    'festac': ['apapa', 'amuwo odofin'],
    'maryland': ['ikeja', 'ojota'],
    'ogba': ['ikeja', 'agege'],
    'ojuelegba': ['lagos mainland', 'surulere'],
    'oshodi': ['mushin', 'isolo'],
    'amuwo odofin': ['festac', 'mile 2'],
    'ojota': ['maryland', 'ketu'],
    'agege': ['ogba', 'dopemu'],
    'isolo': ['oshodi', 'ilasa'],
    'oniru': ['victoria island'],
    'obalende': ['ikoyi', 'lagos island'],
    'marina': ['lagos island'],
    'ebute metta': ['yaba', 'lagos mainland'],
    'aguda': ['surulere'],
    'opebi': ['ikeja'],
    'eko atlantic': ['victoria island'],
    'ketu': ['ojota'],
    'mile 2': ['amuwo odofin'],
    'dopemu': ['agege'],
    'ilasa': ['isolo']
}



def bfs_shortest_path(start, goal):
    
   
    start = start.lower()
    goal = goal.lower()

    if start not in d:
        return f"{start} is an invalid location"

    if goal not in d:
        return f"{goal} is an invalid destination"
    # Initialize the queue with the start node and the initial path
    queue = deque([(start, [start])])

    # Set to keep track of visited nodes
    visited = set()

    while queue:
        node, path = queue.popleft()  # Use popleft for correct BFS order

        # If the goal node is found, return the path
        if node == goal:
            return path

        # Mark the node as visited
        visited.add(node)

        # Iterate over the neighbors of the current node
        for neighbor in d[node]:
            if neighbor not in visited:
                # Append the neighbor and the updated path to the queue
                queue.append((neighbor, path + [neighbor]))

    return f"No path found between {start} and {goal}"



