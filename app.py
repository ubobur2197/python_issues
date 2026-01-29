# 1
n = int(input())

while n >= 10:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    n = s

print(n)


# 2
n = int(input())
count = 0

for i in range(2, n + 1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print(count)


# 3
text = input().split()
longest = text[0]

for word in text:
    if len(word) > len(longest):
        longest = word

print(longest)


# 4
a = int(input())
b = int(input())

for i in range(a, b + 1):
    if str(i) == str(i)[::-1]:
        print(i, end=" ")


# 5
nums = list(map(int, input().split()))
max_count = 0
result = nums[0]

for x in nums:
    if nums.count(x) > max_count:
        max_count = nums.count(x)
        result = x

print(result)
