"""หาร10"""
def main():
    """Code"""
    N = int(input())
    NO = N // 10
    NOR = NO * 10
    for i in range(NO + 1):
        print(NOR, end=" ")
        NOR -= 10
        i += 1
main()
