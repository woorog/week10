import sys

y,x=map(int,sys.stdin.readline().split())

board=[]
for _ in range(y):
    board.append(list(map(int,sys.stdin.readline().split())))

print(board)
dp=[99999999999]*x
pdp=board[0]

dpcheck=[0]*x


for i in range(1,y):
    for k in range(x):

        if k-1>=0:
            dp[k]=min(pdp[k-1]+board[i][k],dp[k])
            print(dp[k-1])
        if k+1<x:
            dp[k]=min(pdp[k+1]+board[i][k],dp[k])
        if pdp[k]+board[i][k]<dp[k]:
            if dpcheck[k]==2:
                dpcheck[k]=0
                continue
            else:
                dp[k]=pdp[k]+board[i][k]
                dpcheck[k]+=1

    pdp=dp
    dp=[99999999999]*x
    print(pdp)
print(min(pdp))




import sys

y,x=map(int,sys.stdin.readline().split())

board=[]
for _ in range(y):
    board.append(list(map(int,sys.stdin.readline().split())))

dp=[99999999999]*x
pdp=board[y-1]

dpcheck=[0]*x
# for i in range(y,0,-1):
#     print(i,999)

for i in range(y-2,-1,-1):
    for k in range(x):
        if k-1>=0:
            dp[k]=min(pdp[k-1]+board[i][k],dp[k])
        if k+1<x:
            dp[k]=min(pdp[k+1]+board[i][k],dp[k])

        if pdp[k]+board[i][k]<dp[k]:
            dpcheck[k]+=1
            if dpcheck[k]==2:
                dpcheck[k]=0
            else:
                dp[k]=pdp[k]+board[i][k]

    pdp=dp
    dp=[99999999999]*x

print(min(pdp))



#
# import sys
#
# y,x=map(int,sys.stdin.readline().split())
#
# board=[]
# for _ in range(y):
#     board.append(list(map(int,sys.stdin.readline().split())))
#
#
# dp=[99999999999]*x
# pdp=board[0]
#
#
# dpcheck=[10]*x
#
#
# for i in range(1,y):
#     for k in range(x):
#         if pdp[k]+board[i][k]<dp[k]:
#             if dpcheck[k]==0:
#                 pass
#             else:
#                 dp[k]=pdp[k]+board[i][k]
#                 dpcheck[k]=0
#
#         if k-1>=0 and pdp[k-1]+board[i][k]<dp[k]:
#             if k+1<x and dpcheck[k+1]==1:
#                 pass
#             else:
#                 dp[k]=pdp[k-1]+board[i][k]
#                 dpcheck[k]=1
#
#         if k+1<x and pdp[k+1]+board[i][k]<dp[k]:
#             if k-1>=0 and dpcheck[k-1]==-1:
#                 pass
#             else:
#                 dp[k]=pdp[k+1]+board[i][k]
#                 dpcheck[k]=-1
#
#
#     pdp=dp
#     dp=[99999999999]*x
#
# print(min(pdp))
