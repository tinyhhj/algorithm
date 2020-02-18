import queue
import random
# bfs
t = int(input())

def isInvalid(r,c,r1,c1):
    return r == r1 or c == c1 or r+c == r1+c1 or r-c == r1-c1

def bfs(mat,path, visit):
    q = queue.Queue()
    q.put(path[0])
    path.clear()

    while not q.empty():
        n = q.get()
        r,c = n
        path.append((r,c))
        visit[r][c] = True
        for i in mat[r][c]:
            r1,c1 = i
            if not visit[r1][c1]:
                q.put((r1,c1))


    return True
def dfs(mat, path,visit,r,c):
    # visit
    path.append((r, c))
    visit[r][c] = True

    if len(path) == len(visit)*len(visit[0]):
        return True

    for i in mat[r][c]:
        if not visit[i[0]][i[1]]:
            if dfs(mat,path,visit,i[0],i[1]):
                return True

    path.pop()
    visit[r][c]= False


for __ in range(t):
    a = input()
    [r,c] = a.split(' ')
    r= int(r)
    c = int(c)

    # 2 for loop
    # r<=20 , c <=20 400 * 400 = 160000
    Matrix = [[[] for x in range(c)] for y in range(r)]
    for i in range(r):
        for j in range(c):
            for k in range(r):
                for l in range(c):
                    # valid point added
                    if not isInvalid(i,j,k,l):
                        Matrix[i][j].append((k,l))
            random.shuffle(Matrix[i][j])



    # memory for visit
    # print(Matrix)
    rr = [x for x in range(r)]
    cc = [x for x in range(c)]
    random.shuffle(rr)
    random.shuffle(cc)
    for i in rr:
        for j in cc:
            finish = False
            visit = [[False for x in range(c)] for y in range(r)]
            path = []
            if dfs(Matrix,path,visit,i,j):
                finish = True
                break
        if finish:
            break
    if finish:
        print("Case #%d: %s"%(__+1, "POSSIBLE"))
        for i in path:
            print("%d %d"%(i[0]+1,i[1]+1))
    else:
        print("Case #%d: %s"%(__+1,"IMPOSSIBLE"))




