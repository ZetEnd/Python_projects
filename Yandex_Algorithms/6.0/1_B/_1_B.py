
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A == 0:
    M = 1
    N = C+1
if B == 0:
    M = 1
    N = D+1
if C == 0:
    N = 1
    M = B+1
if D == 0:
    N = 1
    M = A+1

if (A>B and C>D) or (A<B and C<D):
    M = min(A,B) + 1
    N = min(C,D) + 1
else:
    M = min(sum(),sum())

