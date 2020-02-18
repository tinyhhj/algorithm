from PIL import Image
import random
import sys
import numpy as np

size = 3
iter = 6


class Node:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dist = 0

    def setDist(self, pos, dist):
        self.x = pos[1]
        self.y = pos[0]
        self.dist = dist


def getL2Norm(p1, p2):
    return (int(p1[0]) - int(p2[0])) ** 2 + (int(p1[1]) - int(p2[1])) ** 2 + (int(p1[2]) - int(p2[2])) ** 2


def dist(img1, img2,mask, p1, p2, sat=sys.maxsize):
    ans = 0
    for i in range(size):
        for j in range(size):
            if mask[p1[0]+i,p1[1]+j] == 255: continue
            ans += getL2Norm(img1[p1[0] + i, p1[1] + j, :], img2[p2[0] + i, p2[1] + j, :])
        if ans >= sat:
            return sat
    return ans


def unsigned(i):
    return i & 0xffffffffffffffff


def patchmatch(img1, img2, mask):
    _height, _width = img1.shape[:2]
    __height, __width = img2.shape[:2]
    target = [[Node() for _ in range(_width)] for _ in range(_height)]
    for i in range(_height - size + 1):
        for j in range(_width - size + 1):
            x = np.random.randint(__width - size + 1)
            y = np.random.randint(__height - size + 1)
            target[i][j].setDist((y, x), dist(img1, img2,mask, (i, j), (y, x)))
    print("random initialization finish")
    # iter만큼 반복한다.
    for it in range(iter):
        # 방향을 왼>오,위>아래 or 반대
        xst, xend, xd = 0, _width - size + 1, 1
        yst, yend, yd = 0, _height - size + 1, 1
        if it % 2 == 1:
            xst, xend, xd = _width - size, -1, -1
            yst, yend, yd = _height - size, -1, -1
        for i in range(yst, yend, yd):
            for j in range(xst, xend, xd):
                # 최선의 매핑지점 in img2
                bestY = target[i][j].y
                bestX = target[i][j].x
                bestDist = target[i][j].dist

                # x축 이전단계와 비교하여 더 비슷한 매핑을 따른다
                # j-xd = j == 0 일때 -1이 되야함
                # j == _width-size+1+x 이 -1 x = -_width+size-2
                # j-xd = _width-size + 1 = -1
                if unsigned(j - xd) < unsigned(_width - size + 1):
                    compareY = target[i][j - xd].y
                    compareX = target[i][j - xd].x + xd
                    if unsigned(compareX) < unsigned(__width - size + 1):
                        compareDist = dist(img1, img2,mask, (i, j), (compareY, compareX), bestDist)
                        if bestDist > compareDist:
                            bestY = compareY
                            bestX = compareX
                            bestDist = compareDist

                # y축 이전단계와 비교
                if unsigned(i - yd) < unsigned(_height - size + 1):
                    compareY = target[i - yd][j].y + yd
                    compareX = target[i - yd][j].x
                    if unsigned(compareY) < unsigned(__height - size + 1):
                        compareDist = dist(img1, img2,mask, (i, j), (compareY, compareX), bestDist)
                        if bestDist > compareDist:
                            bestY = compareY
                            bestX = compareX
                            bestDist = compareDist

                # best guess 주변에서 탐색
                r =7
                while r >= 1:
                    # print("r is %d"%r)
                    xmin = max(0, bestX - r)
                    xmax = min(bestX + r + 1, __width - size + 1)
                    ymin = max(0, bestY - r)
                    ymax = min(bestY + r + 1, __height - size + 1)
                    # print(r,xmin,xmax,ymin,ymax)
                    count = 0
                    while True:
                        xp = np.random.randint(xmin, xmax)
                        yp = np.random.randint(ymin, ymax)
                        count += 1
                        # all hole skip
                        if (mask[ymin:ymax, xmin:xmax] == 255).all():
                            break
                        if count > size * size:
                            break
                    compareDist = dist(img1, img2,mask, (i, j), (yp, xp), bestDist)
                    if bestDist > compareDist:
                        bestY = yp
                        bestX = xp
                        bestDist = compareDist
                    r = r // 2
                target[i][j].setDist((bestY, bestX), bestDist)
        print('{} is finished'.format(it))
                # print("iter: %d"%it)

    return target;


if __name__ == '__main__':
    img1 = np.array(Image.open('image/20471811_1.jpg'))
    mask = np.array(Image.open('mask/20471811_1.jpg'))
    mask = (mask >= 200) * 255
    print(mask[79:82,24:27])


    h, w = img1.shape[:2]
    # img1.show()
    # img2.show()
    img3 = patchmatch(img1, img1,mask)
    img4 = img1.copy()
    # (200,0,380,200)
    for i in range(h):
        for j in range(w):
            if mask[i,j] == 255:
                img4[i, j, :] = img1[img3[i][j].y, img3[i][j].x, :]
    img4 = Image.fromarray(img4)
    img4.save('result.jpg')

    img4.show()
