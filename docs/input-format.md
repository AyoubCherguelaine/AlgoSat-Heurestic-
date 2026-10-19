# Input format

`bmc-ibm-7.txt` holds 39 774 clauses from the `bmc-ibm-7` SAT benchmark (bounded model
checking of IBM hardware designs). It is a stripped-down version of the DIMACS CNF
format:

- **one clause per line**;
- literals are integers separated by **single spaces**;
- a positive integer `v` means `Xv`, and a negative one `-v` means `¬Xv`;
- each line **ends with a trailing space** before the newline;
- there is **no** `p cnf` header, no `c` comment lines and no terminating `0`.

Example (the first lines of the file):

```
1 -2 
1 -3 
2 3 4 5 6 7 8 9 10 11 -1 
```

These lines mean `(X1 ∨ ¬X2) ∧ (X1 ∨ ¬X3) ∧ (X2 ∨ X3 ∨ … ∨ X11 ∨ ¬X1)`.

## Using your own instance

The parser in `Sat.__init__` depends on this exact layout. To give it a standard DIMACS
`.cnf` file, first convert it to the same layout:

```bash
# drop comments and header, remove the trailing 0, keep a trailing space
grep -v '^[cp%]' input.cnf | sed -E 's/[[:space:]]*0[[:space:]]*$/ /' > my-instance.txt
```

Check these requirements before running:

- Variables are numbered from 1. Gaps in the numbering are allowed: the assignment
  has one entry per number up to the highest one used.
- `App.py` reads up to 1500 lines and stops early at an empty line.
- Change the file name in `App.py` (`open('bmc-ibm-7.txt')`) to point at your file.
