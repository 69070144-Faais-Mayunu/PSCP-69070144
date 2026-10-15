"""Giraffe"""
def main():
    """Code"""
    N = int(input())
    numlist = []
    count = 0
    for _ in range(N):
        numlist.append(int(input()))
    if N == 1:
        count = 1
    else:
        for i in range(N):
            if not i:
                if numlist[i] > numlist[i + 1]:
                    count += 1
            elif i == N - 1:
                if numlist[i] > numlist[i - 1]:
                    count += 1
            else:
                if numlist[i - 1] < numlist[i] > numlist[i + 1]:
                    count += 1
    print(count)
main()
