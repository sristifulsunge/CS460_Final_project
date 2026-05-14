# The Torchbearer

**Student Name:** Sristi Fulsunge
**Student ID:** 130490344
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  A single shortest-path run from S is not enough as dijkstras gives us the shortest path one from node to all other nodes. It does not tell us from which relic to pick first, second, etc. It does not give us the order of the relics.

- **What decision remains after all inter-location costs are known:**
  Once we run dijsktras on all nodes to figure out the shortest path from any relic to any relic, we still need to know which path allows us to use the cheapest travel fuel. The order still remains unknown after all inter-location costs are known. 

- **Why this requires a search over orders (one sentence):**
  This still requires a search over orders as we need to figure out which is the shortest path we can choose among all the paths possible. 

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| S | The problem requires us to find the shorted path from the entrance S to all nodes |
| {R1, R2, ..., Rk} | We are required to find the shiortest path from all relics to each and every relic in order  |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Dictionary |
| What the keys represent | Source Node(S) or Relics(R1, R2, ..., Rk) |
| What the values represent | Another dictionary with it's key-value pair representing the destination source with distance|
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | The dictionary here represents a hash map that allows constant time lookup|

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** K+1
- **Cost per run:** O(mlogn)
- **Total complexity:** O((K+1)mlog(n))
- **Justification (one line):** We run dijkstras on the source node S and for each k relics. 

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  The shortest distances from source to these nodes have been finalised. 

- **For nodes not yet finalized (not in S):**
  The current distance stored is the shortest path known so far, but a more optimal path might occur later. 

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  At the initial step the distance from the soruce to all different points is infinite (or a very large number), as no path is found yet.
  The distance stored for source is 0. The loop starts correctly. 

- **Maintenance : why finalizing the min-dist node is always correct:**
  While running the loop, either the minimum distance has already been found, or the shortest path has not been found yet. The nodes having the smallest distance is finalised as no further shortest path exists in later runs. 

- **Termination : what the invariant guarantees when the algorithm ends:**
  All nodes have their correct shortest distance from the source. 

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

The route planner gives us the correct shortest distance, that can be used later to find the order of the relics to find the most efficient path. 

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
