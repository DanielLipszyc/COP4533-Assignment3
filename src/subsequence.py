import sys

lines = []
file = open(sys.argv[1])
lines = file.read().strip().split('\n')
file.close()

K = int(lines[0])
vals = {}
for i in range(1, K+1):
    letter, value = lines[i].split()
    vals[letter] = int(value)
A = lines[K+1]
B = lines[K+2]
m = len(A)
n = len(B)

table = []
for i in range(m+1):
    row = []
    for j in range(n+1):
        row.append(0)
    table.append(row)

for i in range(1, m+1):
    for j in range(1, n+1):
        if A[i-1] == B[j-1]:
            table[i][j] = table[i-1][j-1] + vals[A[i-1]]
        elif table[i-1][j] > table[i][j-1]:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = table[i][j-1]

result = []
i = m
j = n
while i > 0 and j > 0:
    if A[i-1] == B[j-1]:
        result.append(A[i-1])
        i -= 1
        j -= 1
    elif table[i-1][j] >= table[i][j-1]:
        i -= 1
    else:
        j -= 1

result.reverse()
print(table[m][n])
print(''.join(result))