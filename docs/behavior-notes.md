# Behaviour notes

This page records how the code behaves and what it is known to do, so its output can be
read correctly.

## Fixed bugs

| Bug | Fix |
|-----|-----|
| `GetOneSol` flipped the list **in place**, so the flips added up while neighbours were evaluated. Each step inverted the whole assignment instead of testing one flip at a time. | `GetOneSol` now works on a copy (`list(sol)`), in both `Sat/Sat.py` and `Basics.py`. |
| `nbVar` was the *count* of distinct variables, but variable `i` is read at index `i-1`. If the numbering had gaps this caused an `IndexError`, and the full `bmc-ibm-7.txt` does have gaps: 8630 variables, highest number 8710. | `nbVar` is now the highest variable number. |
| A file shorter than the number of lines read made `Sat("")` raise `ValueError`. | `App.py` stops reading at the first empty line. |

## Current results

On the first 1500 clauses of `bmc-ibm-7.txt`, `App.py` reaches **1494 / 1500**
satisfied clauses after the full budget of 850 steps (about 3 minutes). Plain greedy
search stalls in a local optimum. That is a limit of the heuristic, not a bug (see
[algorithm.md](algorithm.md)).

## Other notes

- `Sat.ListVariable` is a class attribute. Every `Sat` object created in the same
  process adds to the same list.
- `CalculSat.max` returns index `0` if every score is `0`. Ties go to the lowest index.
- `Basics.py` has no iteration limit. It solves its built-in instance in one step, but
  an unsatisfiable or harder instance would make it loop forever.
- In `App.py`, `print(i<fin)` is a debug print. The variable named `open` hides the
  built-in `open()` after that line, which does no harm because `open()` is not called
  again.
