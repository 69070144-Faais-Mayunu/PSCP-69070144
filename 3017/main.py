"""Bill Code"""
def main():
    """The Code"""
    foodcost = int(input(""))
    tip = max(50, foodcost * 0.1)
    if tip > 1000:
        tip = 1000
    vat = (foodcost + tip) * 0.07
    total = foodcost + tip + vat
    print(f"{total:.2f}")
main()
