"""CuteCat CuteFox"""

def main():
    """Code"""
    n = int(input())

    CAT = {}
    FOX = {}

    for _ in range(n):
        data = input().replace("{", "").replace("}", "")
        data = data.replace('"', "").replace(":", "").split()

        name = data[0]
        key = data[1]

        if key.startswith("Cat"):
            CAT[key] = name
        else:
            FOX[key] = name

    if "Cat01" not in CAT and "Garfield" not in CAT.values() \
            and "Garfield" not in FOX.values():
        CAT["Cat01"] = "Garfield"

    if "Fox01" not in FOX and "Fubuki" not in CAT.values() \
            and "Fubuki" not in FOX.values():
        FOX["Fox01"] = "Fubuki"

    print("Cat :", len(CAT))
    print("Fox :", len(FOX))

    for key in sorted(CAT, key=lambda x: int(x[3:])):
        print(CAT.get(key), ":", key)

    for key in sorted(FOX,  key=lambda x: int(x[3:])):
        print(FOX.get(key), ":", key)

main()
