"""Pad Thai"""
def main():
    """Code"""
    recipe = ['Pad Thai Sauce','Tofu','Pickle Turnip','Shrimp'
              ,'Bean Sprouts','Noodle','Chives','Lime','Egg','Oil','Peanuts']
    tested = ['Sour','Salty','Sweet']
    teste = []
    added = []
    while True:
        add = input()
        if add == "Cook":
            break
        added.append(add)
    while True:
        teste_add = input()
        if teste_add == "End":
            break
        teste.append(teste_add)
    for k in added:
        if k not in recipe:
            print( "This is not Pad Thai!!!")
            return
    for c in recipe:
        if c not in added:
            print("This is bad!")
            return
    for i in tested:
        if i not in teste:
            print("Not Bad...")
            return
    for y in teste:
        if y not in tested:
            print("Not Bad...")
            return
    print("Delicious!")
main()
