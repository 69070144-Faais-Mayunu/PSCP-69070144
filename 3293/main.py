"""BigFrame"""
def main():
    """Code"""
    maxlen = None
    Textlist = []
    for _ in range(5):
        Text = input().rstrip()
        Textlist.append(Text)
    for c in Textlist:
        if maxlen is None or len(c) > maxlen:
            maxlen = len(c)
    for i in range(7):
        if i in (0,6):
            print("*"*(maxlen+4))
        elif i == 1:
            print("* ",Textlist[0]," "*(maxlen - len(Textlist[0]))," *",sep="")
        elif i == 2:
            print("* ",Textlist[1]," "*(maxlen - len(Textlist[1]))," *",sep="")
        elif i == 3:
            print("* ",Textlist[2]," "*(maxlen - len(Textlist[2]))," *",sep="")
        elif i == 4:
            print("* ",Textlist[3]," "*(maxlen - len(Textlist[3]))," *",sep="")
        elif i == 5:
            print("* ",Textlist[4]," "*(maxlen - len(Textlist[4]))," *",sep="")
main()
