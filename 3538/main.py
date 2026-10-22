
"""B - Fully pair?"""
def main():
    """Code"""
    Pair = input()
    Count = {}

    for char in Pair:
        Count[char] = Count.get(char, 0) + 1

    No_Pair = []
    Seen = set()

    for char in Pair:
        if char not in Seen:
            Seen.add(char)
            if Count[char] % 2 == 1:
                No_Pair.append(char)

    if No_Pair:
        print(*No_Pair,sep="")
    else:
        print("fully paired")

main()
