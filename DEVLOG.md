# Development Log – The Torchbearer

**Student Name:** Sristi Fulsunge
**Student ID:** 130490344

---

## Entry 1 – [05/08/2026]: Initial Plan

I initially started off by reading the problem. This lead me to understand that we need to dijkstras on not only the source node, but run it on every single node (including the relics) to figure out the shortes distance from any node to any other node in the graph. Since the order of the nodes visted matters, we need to explore every single path combination in order to figure out the one that uses the least amount of fuel. I think the part that I expect to be the most difficult is the backtracking function (_explore). I usually struggle in recurrsion and I think this part will be the hardest to implemenet. I will frst implement the dijkstras code and then go on to find the order of the relics. 

---

## Entry 2 – [Date]: [Bug 1]

In the function precompute_distances, I forgot to return shortest_dist which ended up giving me a nonetype error as the find_optimal_route function was not able to run and dist_table had a none value as the function never ended up returning anything. This is when I realised that the function was not returning anything. 

---

## Entry 3 – [Date]: [Bug 2]

My code was running perfectly well with no errors, however my order was not printing even though the cost was correct. While asigning the best[1] to relics_collected, which stores the relics collected so far, I did not make a copy of the list while assigning it. This was an issue as, while backtracking when each element that was added to the list gets popped out. Since best[1] was pointing to the same list, it also became empty by the end. I fixed this by using .copy() when assigning the best order, so the best route is saved separately before backtracking changes the original list.

---

## Entry 4 – [Date]: Post-Implementation Reflection

The next thing that we could improve if given more time is trying to figure out another algorithm that could be used in order to figure out the order instead of going through every single possible combination. We coukd try to bring it down from K! to another faster way to solve this problem, if there is a way. 

---

## Final Entry – [Date]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 1.5 hours |
| Part 2: Precomputation Design | 1.5 hours |
| Part 3: Algorithm Correctness | 30 mins |
| Part 4: Search Design | 1 hour|
| Part 5: State and Search Space | 45 mins |
| Part 6: Pruning | 2 hours |
| Part 7: Implementation | 6 hours |
| README and DEVLOG writing | 30 mins |
| **Total** | 13 hours |
