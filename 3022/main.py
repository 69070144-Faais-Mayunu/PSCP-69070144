"""temperature"""
def main():
    """The Code"""
    temperrature = float(input())
    typein = input("")
    typeout = input("")
    c = 0
    result = 0
    if typein == "C":
        c = temperrature
    elif typein == "K":
        c = temperrature - 273.15
    elif typein == "F":
        c = (temperrature - 32) * 5 / 9
    elif typein == "R":
        c = (temperrature - 491.67) * 5 / 9

    if typeout == "C":
        result = c
    elif typeout == "K":
        result = c + 273.15
    elif typeout == "F":
        result = (c * 9 / 5) + 32
    elif typeout == "R":
        result = (c + 273.15) * 9 / 5

    print(f"{result:.2f}")
main()
