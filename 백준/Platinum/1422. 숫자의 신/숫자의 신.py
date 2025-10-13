K, N = map(int, input().split())
numbers = [input().strip() for i in range(K)]
max_num = max(numbers, key=lambda x: (len(x), x))

for i in range(N - K):
    numbers.append(max_num)

numbers.sort(key=lambda x: x * 10, reverse=True)

print(''.join(numbers))