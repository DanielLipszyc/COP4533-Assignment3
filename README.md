# COP4533-Assignment3

### Team Members

Daniel Lipszyc - 32328471

### Requirements
Language: Python 3.14.x (Should run on any 3.x)

### Build/Compilation Instructions
1. Clone the Repository

To run:

```bash
python3 src/subsequence.py tests/YOUR_INPUT_FILE > tests/OUTPUT_FILE
```

For input file: example.in:
```bash
python3 src/subsequence.py tests/example.in > tests/example.out
```
### Assumptions
Input file format is:
```bash
a
```


Output format will be:
```bash
a
```


### Written Component
Question 1: 



Question2:

OPT(i, j) = max value of common subsequence of strings A = [1...i] and B = [1...j]  
Base Cases:  
A is an empty string = OPT(0, j)  
B is an empty string = OPT(i, 0)  

Case 1: A[i] == B[j]  
OPT(i, j) = OPT(i-1, j-1) + val(A[i])  
Case 2

Question 3:
```bash
subsequence(A, B, v):
  m = length of A
  n = length of B
  OPT(i, 0) = 0 for i = 0 to m
  OPT(0, j) = 0 for j = 0 to n

  for i = 1 to m
    for j = 1 to n
      if A[i] == B[j]
        OPT(i, j) = OPT(i-1, j-1) + v(A[i])
      else
        OPT(i, j) = max(OPT(i-1, j), OPT(i, j-1))

  return OPT(m, n)
```
Runtime: O(m*n)
