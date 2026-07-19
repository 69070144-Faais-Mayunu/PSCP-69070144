"""Castle"""
def main():
    """Code"""
    N = int(input())
    F = 1
    while F ** 2 < N:
        F += 1
    R = N - (F - 1) ** 2
    if not R % 2:
        print(F * 2 - 3)
    else:
        print(F * 2 - 2)
main()
