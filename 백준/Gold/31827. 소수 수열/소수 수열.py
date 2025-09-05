prime = [True for i in range(1000001)]
prime[0] = False
prime[1] = False

for i in range(2,1001):
    if not prime[i]:
        continue

    for j in range(i*2, 1000001, i):
        prime[j] = False

n, k = map(int, input().split())

primes = []
for i in range(1000001):
    if prime[i]:
        primes.append(i)

answer = []
for p in primes:
    if p % k == 1:
        answer.append(p)
    if len(answer) == n:
        break

print(' '.join(map(str, answer)))