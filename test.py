A= [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

A1 = [[i[0],-i[1]] for i in A]
A1.sort()

print A1

B = [i for i in range(len(A))]
C = [0]*len(A)
for i in A1:
    #print i
    C[B[-i[1]]] = [i[0],-i[1]]
    B.pop(-i[1])
print C
