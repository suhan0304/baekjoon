import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    graph.append(input()[:-1])

print(graph)