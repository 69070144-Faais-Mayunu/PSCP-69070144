"""ส่งต่อ"""
def main():
    """Code"""
    N, S, = input().split()

    send = []
    sending = None
    sended = []
    total = 0
    for _ in range(int(N)):
        n = input()
        send.append(n)
    while True:
        if S in sended:
            break
        sended.append(S)
        if sending == "0":
            break
        sending = send[int(S) - 1]
        S = sending
        total += 1
    print(total)
main()
