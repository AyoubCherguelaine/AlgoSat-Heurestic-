# Code reference

## `Sat/` package

`Sat/__init__.py` runs `from Sat.Sat import *`, so `from Sat import Sat, CalculSat`
imports both classes from `Sat/Sat.py`.

### `class Sat` (`Sat/Sat.py`)

One object is one clause.

| Member | Description |
|--------|-------------|
| `ListVariable` | **Class-level** list shared by all instances. It holds every distinct variable number seen across all clauses. `App.py` uses its length as the number of variables. |
| `__init__(self, file)` | `file` is one line of the input, e.g. `"1 -2 "`. The line is split on single spaces and its last token (the empty string after the trailing space) is dropped. Each integer `v` becomes variable `abs(v)` with polarity `1` if `v > 0`, else `0`. |
| `AddVar(self, Var)` | Adds new variable numbers to `Sat.ListVariable`. |
| `__Forma(self, varibles, var)` | Private. Builds `self.clause = {variable: polarity}`. |
| `GetClause(self)` | Returns the `self.clause` dict. |
| `GetValidation(self, Solution)` | Returns `True` if the clause is satisfied by `Solution`, a 0/1 list where variable `i` is `Solution[i-1]`. |
| `Display(self)` | Prints each literal as `Xi : polarity`. |

Example: the line `"2 -5 7 "` gives `clause = {2: 1, 5: 0, 7: 1}`, which means `X2 ∨ ¬X5 ∨ X7`.

### `class CalculSat` (`Sat/Sat.py`)

Helper functions for the search. They do not use the object's state.

| Method | Description |
|--------|-------------|
| `__init__(self)` | Sets `self.Sol = []` (not used afterwards). |
| `GetOneSol(self, sol, index)` | Returns a **copy** of `sol` with `sol[index]` flipped between 0 and 1. The list passed in is not changed. |
| `max(self, listm)` | Returns the index of the first largest value, or `0` if every value is `0`. |
| `score(self, clauses, Sol)` | Counts the `Sat` objects in `clauses` for which `GetValidation(Sol)` is true. |

## `App.py`: main program

1. Opens `bmc-ibm-7.txt` and reads **up to 1500 lines** into `Sat` objects (`Clauses`),
   stopping early at an empty line.
2. `nbVar = max(Clauses[0].ListVariable)`, the highest variable number (429 here).
3. `sol = [0] * nbVar`.
4. If `sol` already satisfies every clause, it prints it and the search stops.
5. Main loop. Runs while not solved and `k < fin`, where `fin = 100 + len(Clauses)/2`:
   - for each variable `i`, flips it with `GetOneSol` and records the score;
   - picks `MIndex = calc.max(scores)` and flips that variable;
   - stops if `scores[MIndex] == len(Clauses)`.
6. Prints the final `sol` and its score.

Debug output during the loop: `fin`, then `k = …` and `i<fin` on every iteration.

To change the instance size, edit the `while(i<1500)` bound in `App.py`.

## `Basics.py`: prototype

A standalone first version that does not use the `Sat` package. Clauses are dense
vectors with one entry per variable:

- `1`: the variable appears positively (`X`)
- `-1`: the variable appears negated (`¬X`)
- `0`: the variable does not appear

```python
nbVar = 4
clauses = [[1, 1, 0, 1], [0, -1, 1, 0], [1, 0, -1, -1],
           [1, 0, 0, 1], [-1, 1, -1, -1], [1, 1, 1, 0]]
```

It defines module-level versions of `GetOneSol`, `TestClause`, `score` and `max`, then
runs the same greedy loop, printing the scores at every step. The loop has **no
iteration limit**: it only stops when every clause is satisfied.
