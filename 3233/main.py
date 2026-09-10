"""สลากกินแบ่ง"""
def main():
    """Code"""
    text, num = input().split()
    textout, numout = input().split()
    if text == textout:
        if num == numout:
            print(1000000)
        elif num[-3:] == numout[-3:]:
            print(2000)
        elif num[-2:] == numout[-2:]:
            print(1000)
        else:
            print(20)
    else:
        if num == numout:
            print(100000)
        elif num[-3:] == numout[-3:]:
            print(200)
        elif num[-2:] == numout[-2:]:
            print(100)
        else:
            print(0)
main()
