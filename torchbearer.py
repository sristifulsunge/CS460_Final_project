"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Sristi Fulsunge
Student ID:   130490344

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return "1. a single shortest-path run from S is not enough as dijkstras gives us the shortest path one from node to all other nodes. " \
    "It does not tell us from which relic to pick first, second, etc. It does not give us the order of the relics. " \
    "2. Once we run dijsktras on all nodes to figure out the shortest path any relic to any relic, we still need to know which path allows us to use the cheapest travel fuel. " \
    "The order still remains unknown after all inter-location costs are known. " \
    "3. This still requires a search over orders as we need to figure out which is the shortest path we can choose among all the paths possible. "


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sources = [spawn]
    for relic in relics:
        if relic not in sources:
            sources.append(relic)
    
    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    
    distances[source] = 0
    priority_queue = [(0,source)]
    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_dist > distances[current_node]:
            continue
        
        for neighbour,cost in graph[current_node]:
            new_dist = current_dist + cost

            if new_dist < distances[neighbour]:
                distances[neighbour] = new_dist
                heapq.heappush(priority_queue,(new_dist, neighbour))
    
    return distances


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    shortest_dist = {}
    shortest_dist[spawn] = run_dijkstra(graph, spawn)
    for relic in relics:
        shortest_dist[relic] = run_dijkstra(graph, relic)


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return "Loop Invarient: " \
    "For nodes already finalized (in S): The shortest distances from source to these nodes have been finalised." \
    "For nodes not yet finalized (not in S): The current distance stored is the shortest path known so far, but a more optimal path might occur later." \
    "Initialization : why the invariant holds before iteration 1: At the initial step the distance from the source to all different points is infinite (or a very large number), as no path is found yet. The distance stored for source is 0. The loop starts correctly." \
    "Maintenance : why finalizing the min-dist node is always correct: While running the loop, either the minimum distance has already been found, or the shortest path has not been found yet. The nodes having the smallest distance is finalised as no further shortest path exists in later runs." \
    "Termination : what the invariant guarantees when the algorithm ends: All nodes have their correct shortest distance from the source. The loop ends correctly." \
    "Why This Matters: The route planner gives us the correct shortest distance, that can be used later to find the order of the relics to find the most efficient path."


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "Why Greedy Fails: " \
    "The failure mode: Greedy always picks the shortest distance locally, but this could lead to a hiugher total cost. However, there could be a better, more optimal path in later steps." \
    "Counter-example setup: Taking another graph as an example S-->A (cost = 1), S --> B(cost 2), A-->B (cost 100), A-->T(cost 1), B-->A(cost 1), B-->T(Cost 1). Greedy always picks the locally most optimal path." \
    "Greedy picks S-->A-->B-->T and gives us a total cost of 102, while we could pick S-->B-->A-->T giving us a total cost of 4. " \
    "What greedy picks: The shortest path known locally, i.e. from S to B" \
    "What optimal picks: Could pick S to C that could lead to a cheaper overall cost." \
    "Why greedy loses: Choosing the closest relic first could lead to future expensive paths, while a slightly more expensive path at the first step could lead to a more cheaper path." \
    "What the Algorithm Must Explore: " \
    "The algorithm must explore all possible different combinations/orders to evaluate the minimum cost path that explores all relics from a given starting positon to end position."



# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    remaining_relics = set(relics)
    relics_collected = []
    cost_so_far = 0

    best =[float('inf'), []]

    _explore(dist_table, spawn, remaining_relics, relics_collected, cost_so_far, exit_node, best)
    return  best[0], best[1]


def _explore(dist_table, current_loc, relics_remaining, relics_collected,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """

    #Pruning 
    #It allows the algorithm to skip when any path computed is more expensive than 
    #the best complete route. This way we are evaluating all the paths possible that 
    #include all relic, and discard those whose current cost plus remaining cost is
    #more than the minimum fuel evalauted so far. 

    if cost_so_far >= best[0]:
        return 
    
    #base case
    if not relics_remaining:

        exit_cost = dist_table[current_loc][exit_node]
        if exit_cost == float('inf'):
            return
        
        total_cost = exit_cost + cost_so_far
        if total_cost <= best[0]:
            best[0] = total_cost
            best[1] = relics_collected
            return 

    #recurrsive case 
    for relic in list(relics_remaining):
        travel_cost = dist_table[current_loc][relic]

        if travel_cost == float('inf'):
            continue
        
        relics_remaining.remove(relic)
        relics_collected.append(relic)

        _explore(dist_table,relic,relics_remaining,relics_collected,cost_so_far + travel_cost, exit_node, best)

        relics_collected.pop()
        relics_remaining.add(relic)


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    min_fuel_cost, order_relic = find_optimal_route(dist_table, spawn, relics, exit_node)
    return min_fuel_cost, order_relic


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
