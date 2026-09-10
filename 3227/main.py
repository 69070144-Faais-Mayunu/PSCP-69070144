"""ไพ่ 44 ใบ"""
def main():
    """Code"""
    card = input()
    num = ""
    text = ""
    for char in card:
        if char.isdigit():
            num += char
        else:
            text += char
    backs = {
                "D": "diamonds",
                "H": "hearts",
                "S": "spades",
                "C": "clubs"
            }
    if num:
        print(num, "of", backs[text.upper()])

    else:
        names = {
            "A": "ace",
            "J": "jack",
            "Q": "queen",
            "K": "king"
        }
        name = names[text[0].upper()]
        back = backs[text[1].upper()]
        print(name, "of", back)
main()
