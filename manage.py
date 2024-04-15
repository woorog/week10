import sys
from collections import deque

top, a, b = map(int, sys.stdin.readline().split())

lists = set()
lists.add((0, a))
lists.add((0, b))
q = deque()
q.append((0, a))
q.append((0, b))
max = 0

while q:
    water, now = q.popleft()
    if now == top:
        max = top
        break
    elif now > top:
        continue
    else:
        if max < now:
            max = now

    if water == 0:
        plemon = (0, now + a)
        porange = (0, now + b)
        drink = (1, int(now / 2))
        if plemon not in lists:
            q.append(plemon)
            lists.add(plemon)
        if porange not in lists:
            q.append(porange)
            lists.add(porange)
        if drink not in lists:
            q.append(drink)
            lists.add(drink)
    else:
        plemon = (1, now + a)
        porange = (1, now + b)
        if plemon not in lists:
            q.append(plemon)
            lists.add(plemon)
        if porange not in lists:
            q.append(porange)
            lists.add(porange)

print(max)
