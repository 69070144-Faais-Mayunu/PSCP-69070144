"""กบน้อยกระโดด"""
def main():
    """Code"""
    jump , goal, = map(int,input().split())
    po = 0
    count = 0
    finist = True
    while po < goal:
        po += jump
        jump -= 2
        count += 1
        if po < goal and jump < 0:
            print(-1)
            finist = False
            break
    if finist is True:
        print(count)
main()
