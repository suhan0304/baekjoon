import sys

input = sys.stdin.readline

l = int(input())
s = list(map(int, input().split()))
n = int(input())
s.sort()


def combination(l, r):
    return int((r - l + 1) * (r - l) / 2)


if n in s:
    print(0)
else:
    left = 0
    right = 0
    for x in s:
        if x < n:
            left = x
        elif x > n and right == 0:
            right = x
    left += 1
    right -= 1
    print(
        combination(left, right) - combination(left, n - 1) - combination(n + 1, right)
    )
