from binary import *
from matrix import *

B = [
[0,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,0,1,1,1,0,0,0,1,0],
[1,1,0,1,1,1,0,0,0,1,0,1],
[1,0,1,1,1,0,0,0,1,0,1,1],
[1,1,1,1,0,0,0,1,0,1,1,0],
[1,1,1,0,0,0,1,0,1,1,0,1],
[1,1,0,0,0,1,0,1,1,0,1,1],
[1,0,0,0,1,0,1,1,0,1,1,1],
[1,0,0,1,0,1,1,0,1,1,1,0],
[1,0,1,0,1,1,0,1,1,1,0,0],
[1,1,0,1,1,0,1,1,1,0,0,0],
[1,0,1,1,0,1,1,1,0,0,0,1]
]

I_12 = [
[1,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,1]]

## decode consumes a received message r, and decode it to a codeword of Extended Golay Code
## req: r is an vector with 24 elements, assuming already in binary form
def decode(r):
    mat_b = Matrix(B)
    new_mat = mat_b.col_join(I_12, "left")
    s1 = Binary(new_mat.product(r))
    print(s1.value())
    if s1.value() == [0]*12:
        print("accept r and stop")
        print(r)
        return r
    elif s1.weight() <= 3:
        e = s1.value() + [0] * 12
        c = s1.sub(r, e).value()
        print(c)
        return c
    for i in range(len(B)):
        if s1.diff(B[i])[0] > 2:
            continue
        x = r[0:12]
        y = r[12:]
        if s1.diff(B[i])[0] == 1:
            j = s1.diff(B[i])[1][0]
            x[j] = (1 + x[j]) % 2
            y[i] = (1 + y[i]) % 2
            c = x + y
            print(c)
            return c
        else:
            j = s1.diff(B[i])[1][0]
            k = s1.diff(B[i])[1][1]
            x[j] = (1 + x[j]) % 2
            x[k] = (1 + x[k]) % 2
            y[i] = (1 + y[i]) % 2
            c = x + y
            print(c)
            return c
    new_mat = mat_b.col_join(I_12, "right")
    s2 = Binary(new_mat.product(r))
    if s2.weight() <= 3:
        e = [0] * 12 + s2.value()
        c = s2.sub(r, e).value()
        print(c)
        return c
    for i in range(len(B)):
        if s2.diff(B[i])[0] > 2:
            continue
        x = r[0:12]
        y = r[12:]
        if s2.diff(B[i])[0] == 1:
            j = s2.diff(B[i])[1][0]
            x[i] = (1 + x[i]) % 2
            y[j] = (1 + y[j]) % 2
            c = x + y
            print(c)
            return c
        else:
            j = s2.diff(B[i])[1][0]
            k = s2.diff(B[i])[1][1]
            x[i] = (1 + x[i]) % 2
            y[j] = (1 + y[j]) % 2
            y[k] = (1 + y[k]) % 2
            c = x + y
            print(c)
            return c
    print("r is rejected")

##decode([1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0,1])
##decode([1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,0])
## A3Q5a decode([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1])
## A3Q5b decode([0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0])
## A3Q5c decode([1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0,1])
## A3Q5d decode([1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,1,1,1])