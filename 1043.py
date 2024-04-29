import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
truth = set(input().rstrip().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().rstrip().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & truth:
            truth = truth.union(party)

cnt = 0
for party in parties:
    if party & truth:
        continue
    cnt += 1

print(cnt)