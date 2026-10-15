"""หุ่นยนต์เคาะเสียงกระเบื้อง"""
def main():
    """Code"""
    N , P = list(map(int, input().split()))
    numlist = []
    for _ in range(N):
        x = list(map(int, input().split()))
        numlist.append(x)
    for i in range(N):
        count = 0
        total = 0
        for k in numlist[i]:
            if k:
                count += 1
                total += k
        print(*numlist[i],count,total)
    countlist = []
    totallist = []
    for x in range(N):
        count = 0
        total = 0
        for y in range(N):
            if numlist[y][x]:
                count += 1
                total += numlist[y][x]
        countlist.append(count)
        totallist.append(total)
    print(*countlist)
    print(*totallist)
    print(f"{sum(countlist)} {sum(totallist)} {sum(totallist) * P:.2f}")
main()
