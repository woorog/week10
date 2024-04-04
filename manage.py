import copy
import sys

y,x,tc=map(int,sys.stdin.readline().split())



board=[]
for _ in range(y):
    board.append(list(map(int,sys.stdin.readline().split())))

for _ in range(tc):
    r,c,s=map(int,sys.stdin.readline().split())

    cnt=0

    while 2*s-2*cnt>=1:
        cb=copy.deepcopy(board)
        sx=c-s+cnt-1
        ex=c+s-cnt-1
        sy=r-s+cnt-1
        ey=r+s-cnt-1

        print(sx,ex,sy,ey)
        temp=board[sy+1][sx]

        for i in range(sx,ex):
            cb[sy][i]=temp
            temp=board[sy][i]

        for i in range(sy,ey):
            cb[i][ex]=temp
            temp=board[i][ex]


        for i in range(ex,sx,-1):
            cb[ey][i]=temp
            temp=board[ey][i]

        for i in range(ey,sy,-1):
            cb[i][sx]=temp
            temp=board[i][sx]


        # for i in range(y):
        #     print(cb[i])

        cnt+=1
        board=cb

ans=sum(board[0])
for i in range(y):
    if sum(board[i])<ans:
        ans=sum(board[i])

print(ans)
