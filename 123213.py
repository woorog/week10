# import sys
#
# def go(y1, x1):
#     dis = [(0,1),(0,-1),(-1,0),(1,0)]
#     global nexts
#     count0=0
#     like=0
#
#     for yy,xx in dis:
#         yy+=y1
#         xx+=x1
#         if 0<=yy<n and 0<=xx<n and board[yy][xx]==0:
#             count0+=1
#         if 0<=yy<n and 0<=xx<n and board[yy][xx] in a:
#             like+=1
#
#     if like>nexts[1]:
#         nexts=[count0,like,y1,x1]
#     elif like==nexts[1] and count0>nexts[0]:
#         nexts=[count0,like,y1,x1]
#         return
#     elif like==nexts[1] and count0==nexts[0] and y1+x1<nexts[2]+nexts[3]:
#         nexts=[count0,like,y1,x1]
#     elif like==nexts[1] and count0==nexts[0] and y1+x1==nexts[2]+nexts[3] and x1>nexts[3]:
#         nexts=[count0,like,y1,x1]
#
#
# lists=[]
# numlist=[]
#
# n=int(sys.stdin.readline())
# board=[[0]*n for _ in range(n)]
#
# a=list(map(int,sys.stdin.readline().split()))
#
# board[1][1]=a[0]
#
# del a[0]
#
# lists.append(a)
# numlist.append(board[1][1])
#
# ans=0
# dis = [(0,1),(0,-1),(-1,0),(1,0)]
#
# for j in range(n**2-1):
#     a=list(map(int,sys.stdin.readline().split()))
#     nexts=[-1,-1,0,0]
#         # 인접 좋아하는 학생, 인접빈칸 , 거리
#     lists.append(a)
#     node=a[0]
#     numlist.append(node)
#     del a[0]
#
#     visited=[[0]*n for _ in range(n)]
#     for i in range(n):
#         for k in range(n):
#             if board[i][k] in a:
#                 for dy,dx in dis:
#                     dy+=i
#                     dx+=k
#                     if 0<=dy<n and 0<=dx<n and visited[dy][dx]==0 and board[dy][dx]==0:
#                         visited[dy][dx]=1
#                         go(dy,dx)
#
#
#     board[nexts[2]][nexts[3]]=node
#     print(node)
# print(board)
#
# for i in range(n):
#     for k in range(n):
#         temp=numlist.index(board[i][k])
#         cnt=0
#         for dy,dx in dis:
#             dy+=i
#             dx+=k
#             if 0<=dy<n and 0<=dx<n and board[dy][dx] in lists[temp]:
#                 cnt+=1
#
#
#
#         if cnt==1:
#             ans+=1
#         elif cnt==2:
#             ans+=10
#         elif cnt==3:
#             ans+=100
#         elif cnt==4:
#             ans+=1000
#
#
# print(ans)
#
#
#
#
#
import sys

def go(y1, x1):
    dis = [(0,1),(0,-1),(-1,0),(1,0)]
    global nexts
    count0 = 0
    like = 0

    for yy, xx in dis:
        yy += y1
        xx += x1
        if 0 <= yy < n and 0 <= xx < n and board[yy][xx] == 0:
            count0 += 1
        if 0 <= yy < n and 0 <= xx < n and board[yy][xx] in a:
            like += 1

    if like > nexts[1] or \
            (like == nexts[1] and count0 > nexts[0]) or \
            (like == nexts[1] and count0 == nexts[0] and y1 + x1 < nexts[2] + nexts[3]) or \
            (like == nexts[1] and count0 == nexts[0] and y1 + x1 == nexts[2] + nexts[3] and x1 > nexts[3]):
        nexts = [count0, like, y1, x1]

lists = []
numlist = []

n = int(sys.stdin.readline())
board = [[0] * n for _ in range(n)]

a = list(map(int, sys.stdin.readline().split()))

board[1][1] = a[0]
del a[0]

lists.append(a)
numlist.append(board[1][1])

ans = 0
dis = [(0,1),(0,-1),(-1,0),(1,0)]

for j in range(n ** 2 - 1):
    a = list(map(int, sys.stdin.readline().split()))
    nexts = [-1, -1, 0, 0]  # 인접 좋아하는 학생, 인접빈칸 , 거리
    lists.append(a)
    node = a[0]
    numlist.append(node)
    del a[0]

    empty_spaces = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 0]
    for empty_space in empty_spaces:
        go(empty_space[0], empty_space[1])

    aaa=0
    if nexts==[-1, -1, 0, 0]:
        for i in range(n):
            if aaa==1:
                break
            for k in range(n):
                if board[i][k]==0:
                    aaa=1
                    board[i][k]=node
                    break
    else:
        board[nexts[2]][nexts[3]] = node
print(board)
for i in range(n):
    for k in range(n):
        temp = numlist.index(board[i][k])
        cnt = 0
        for dy, dx in dis:
            dy += i
            dx += k
            if 0 <= dy < n and 0 <= dx < n and board[dy][dx] in lists[temp]:
                cnt += 1

        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000

print(ans)

