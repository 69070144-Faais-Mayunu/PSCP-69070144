"""Shorten"""
def main():
    """Code"""
    num = int(input())
    numlist = []
    while num != -1:
        numlist.append(num)
        num = int(input())
    if numlist:
        ans = []
        start =numlist[0]
        prev = numlist[0]

        for i in numlist[1:]:
            if i == prev + 1:
                prev = i
            else:
                if start == prev:
                    ans.append(start)
                else:
                    ans.append(f"{start}-{prev}")
                start = i
                prev = i

        if start == prev:
            ans.append(start)
        else:
            ans.append(f"{start}-{prev}")
        print(*ans,sep=", ")
main()
