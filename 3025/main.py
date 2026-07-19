"""season calculator"""
def main():
    """main function"""
    mounths = int(input())
    days = int(input())
    if mounths <= 3:
        if days >= 21 and mounths == 3:
            print("spring")
        else:
            print("winter")
    if 3 < mounths <= 6:
        if days >= 21 and mounths == 6:
            print("summer")
        else:
            print("spring")
    if 6 < mounths <= 9:
        if days >= 21 and mounths == 9:
            print("fall")
        else:
            print("summer")
    if 9 < mounths <= 12:
        if days >= 21 and mounths == 12:
            print("winter")
        else:
            print("fall")
main()
    