import csv
from collections import defaultdict
import heapq

def read_csv(file_name):
    # Open and read the CSV file, converting each row to a tuple
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        railway_network = [tuple(row) for row in reader]
    return railway_network

def create_graph(railway_network):
    # Initialize a defaultdict to store the graph, where keys are station names
    # and values are lists of tuples (cost, connected station)
    graph = defaultdict(list)
    for station1, station2, cost in railway_network:
        cost = int(cost.strip())  # Convert the cost from string to integer and remove any surrounding spaces
        station1 = station1.strip().lower()  # Normalize station names to lowercase and strip any spaces
        station2 = station2.strip().lower()
        # Add both directions to the graph since the railway is bidirectional
        graph[station1].append((cost, station2))
        graph[station2].append((cost, station1))
    return graph

def shortest_path(graph, start, end):
    # Use Dijkstra's algorithm with a priority queue (min-heap) to find the shortest path
    # Initialize the queue with a tuple of (current total cost, current station, path taken)
    queue = [(0, start, [])]
    seen = set()  # Set to track visited stations to avoid cycles
    while queue:
        cost, node, path = heapq.heappop(queue)  # Pop the station with the lowest cost
        if node not in seen:
            seen.add(node)  # Mark this node as visited
            path = path + [node]  # Append the current station to the path
            if node == end:
                return cost, path  # Return the total cost and path if the end station is reached
            for c, neighbour in graph[node]:  # Explore all neighbors of the current station
                if neighbour not in seen:
                    heapq.heappush(queue, (cost + c, neighbour, path))  # Push new paths into the queue
    return None, None  # Return None if no path is found from start to end

def main():
    # Read the railway network data from the CSV file and create a graph
    railway_network = read_csv('task1_4_railway_network.csv')
    graph = create_graph(railway_network)
    
    # Ask the user to input the start and end stations
    start = input("Enter the start station: ").strip().lower()
    end = input("Enter the end station: ").strip().lower()

    # Ensure both stations are in the graph, otherwise print an error and exit
    if start not in graph or end not in graph:
        print(f"Error: One or both stations not found in the network. Check your input.")
        return

    # Find the shortest path using Dijkstra's algorithm
    cost, path = shortest_path(graph, start, end)
    if cost is None:
        print("No path found between the stations.")
    else:
        # Output the result with the cheapest cost and the path taken
        print(f"If you try {start.title()} and {end.title()}, we can get the following result:")
        print(f"The total / cheapest cost is {cost} with the following route : {path}")

if __name__ == "__main__":
    main()
