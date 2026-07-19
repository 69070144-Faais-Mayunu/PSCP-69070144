"""Surprising vote"""
def main():
    """The Code"""
    Sumall = float(input(""))
    Maxvote = float(input(""))
    minvote = max(0, Sumall - (Maxvote * 2))
    check = Maxvote - minvote
    if check > 2 or check < 0:
        print("Surprising")
    else:
        print("Not surprising")
main()
