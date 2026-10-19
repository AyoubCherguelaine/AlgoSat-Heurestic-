# Algorithm

## The SAT problem

A formula in **CNF** (conjunctive normal form) is an AND of clauses. Each clause is an OR
of literals, and a literal is a variable `Xi` or its negation `¬Xi`.

```
(X1 ∨ ¬X2) ∧ (X2 ∨ X3 ∨ ¬X1) ∧ ...
```

The goal is to find a true/false value (here `1` / `0`) for every variable so that **every**
clause is true. A clause is true when at least one of its literals is true.

SAT is NP-complete, so exact solvers can take exponential time. This project uses a
**heuristic** instead: it is fast, but it cannot guarantee that it finds a solution.

## Heuristic: greedy hill climbing on the number of satisfied clauses

### Objective (score)

```
score(sol) = number of clauses satisfied by assignment sol
```

The maximum possible score is `len(Clauses)`. Reaching it means `sol` is a solution.

### Neighbourhood

A *neighbour* of `sol` is the same assignment with exactly one variable flipped
(`0 → 1` or `1 → 0`). With `n` variables, each assignment has `n` neighbours.

### Search loop (App.py)

```
sol ← [0, 0, ..., 0]                       # one entry per variable
if score(sol) = |clauses|: done

repeat at most fin = 100 + |clauses| / 2 times:
    for each variable i:
        scores[i] ← score(sol with variable i flipped)
    best ← index of the highest score  (first one on ties)
    sol  ← sol with variable best flipped
    if scores[best] = |clauses|: done (solution found)

print sol and score(sol)
```

### Cost

One iteration evaluates `n` neighbours. Each evaluation checks all `m` clauses, and each
clause check is linear in the clause length `L`. So one step costs about `O(n · m · L)`.
For the default run, `n = 429` and `m = 1500`.

### Stopping rule

- **Success:** a neighbour satisfies every clause.
- **Budget:** the number of steps reaches `fin = 100 + m/2`. For 1500 clauses that is 850.

### Limits of plain hill climbing

- It can stall in a **local optimum**, where no single flip improves the score.
- There is no randomisation, restart or tabu list, so every run on the same input gives
  the same result.

Common extensions are GSAT/WalkSAT-style random walks, random restarts, and tabu
search. None of them is implemented here.

> On the first 1500 clauses of `bmc-ibm-7`, this reaches 1494 / 1500 satisfied clauses
> before the step budget runs out. See [behavior-notes.md](behavior-notes.md).
