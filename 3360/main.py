"""หั่นขนมปัง"""

def main():
    """Code"""
    W, H, M, N = map(int, input().split())
    Xlist = list(map(int, input().split()))
    Ylist = list(map(int, input().split()))
    width = []
    height = []
    for i in range(M):
        if not i:
            width.append(Xlist[i])
        else:
            width.append(Xlist[i] - Xlist[i - 1])
    width.append(W - Xlist[M - 1])
    for i in range(N):
        if not i:
            height.append(Ylist[i])
        else:
            height.append(Ylist[i] - Ylist[i - 1])
    height.append(H - Ylist[N - 1])
    area1 = 0
    area2 = 0
    for w in width:
        for h in height:
            area = w * h
            if area > area1:
                area2 = area1
                area1 = area
            elif area > area2:
                area2 = area
    print(area1, area2)
main()
