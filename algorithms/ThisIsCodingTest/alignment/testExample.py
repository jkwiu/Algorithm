N, K = 5, 3
A = [1,2,5,4,3]
B=[5,5,6,6,5]

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(K-1):
    print(A[i])
    print(B[i])

    A[i], B[i] = B[i], A[i]

print(sum(A))
