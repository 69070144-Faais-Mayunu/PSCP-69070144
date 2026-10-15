"""Point Sorting"""
def main():
    """Code"""
    T = int(input())
    ans = []
    for _ in range(T):
        t = int(input())
        points = []
        for _ in range(t):
            x, y = map(int, input().split())
            distance = x + y
            neg_y = -y
            points.append((distance, neg_y, x, y))
        points.sort()
        for distance, neg_y, x, y in points:
            ans.append((x, y))
    for x,y in ans:
        print(x,y)
main()
