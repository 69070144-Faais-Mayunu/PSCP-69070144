"""Duplicate I"""
def main():
    """Code"""
    m = int(input())
    n = int(input())
    mlist = []
    nlist = []
    same = []
    for _ in range(m):
        mlist.append(int(input()))
    for _ in range(n):
        nlist.append(int(input()))
    mlist.sort(reverse=True)
    nlist.sort(reverse=True)
    for i in mlist:
        for k in nlist:
            if i == k:
                same.append(i)
    same.sort(reverse=True)
    if same:
        for y in same:
            print(y)
    else:
        print("Nope")
main()
