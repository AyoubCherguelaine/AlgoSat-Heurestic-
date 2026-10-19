# AlgoSat-Heurestic

A small Python project that solves the **SAT (Boolean satisfiability) problem** with a
**greedy hill-climbing heuristic**: start from an all-false assignment, then flip, one at
a time, the variable that satisfies the most clauses, until every clause is satisfied
or an iteration limit is hit.

The default run uses the first 1500 clauses of the `bmc-ibm-7` benchmark (bounded model
checking, IBM).

## Quick start

No dependencies. You only need Python 3 (it was developed on 3.8 / 3.9).

```bash
git clone <repo-url>
cd AlgoSat-Heurestic-

# Main solver: loads bmc-ibm-7.txt and runs the heuristic
python3 App.py

# Small standalone demo: 4 variables, 6 hard-coded clauses
python3 Basics.py
```

`App.py` prints the iteration counter `k`, then the final assignment (`sol`) and its
score, which is the number of satisfied clauses. If the score equals the number of
clauses, the formula is satisfied.

## Project layout

```
AlgoSat-Heurestic-/
├── App.py            # Entry point: reads the CNF file, runs the heuristic
├── Basics.py         # Self-contained prototype on a tiny hard-coded instance
├── Sat/
│   ├── __init__.py   # Re-exports everything from Sat/Sat.py
│   └── Sat.py        # Sat (one clause) and CalculSat (search helpers)
└── bmc-ibm-7.txt     # Benchmark clauses, one per line
```

## Documentation

| Doc | Contents |
|-----|----------|
| [docs/algorithm.md](docs/algorithm.md) | The SAT problem, the hill-climbing heuristic, the scoring function and the stopping rule |
| [docs/code-reference.md](docs/code-reference.md) | Every module, class and function, and how `App.py` uses them |
| [docs/input-format.md](docs/input-format.md) | Format of `bmc-ibm-7.txt` and how to use your own instance |
| [docs/behavior-notes.md](docs/behavior-notes.md) | How the current code actually behaves, with its limits and caveats |

## How it works (short version)

1. Each line of the input file becomes a `Sat` object: a clause stored as
   `{variable_number: 1 (positive) | 0 (negated)}`.
2. The starting assignment `sol` has every variable set to `0`.
3. `score` counts how many clauses `sol` satisfies.
4. At each step, every variable is tried as a flip. The step keeps the flip with the
   best score.
5. The search stops when all clauses are satisfied or after `100 + clauses/2` steps.

See [docs/algorithm.md](docs/algorithm.md) for the details.
