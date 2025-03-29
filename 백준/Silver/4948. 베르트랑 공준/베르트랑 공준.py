import sys

prime = [1] * (246913)
prime[0] = 0
prime[1] = 0

for i in range(2, int(246912**0.5) + 1):
    if prime[i]:
        for j in range(i * i, 246913, i):
            prime[j] = 0


while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    print(sum(prime[n+1:2*n+1]))