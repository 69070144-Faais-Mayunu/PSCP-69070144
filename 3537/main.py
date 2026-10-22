"""Impostor"""
def main():
    """Code"""
    Crewmate = {}
    Imposter = {}
    Dead = {}

    while True:
        Player = input()
        if Player == "Start":
            break

        Player = Player.replace("{", "").replace("}", "")
        Player = Player.replace('"', "").replace(":", "").split()

        name = Player[0]
        key = Player[1]

        if key == "Crewmate":
            Crewmate[name] = key
        else:
            Imposter[name] = key

    while True:
        Vote = input()
        if Vote == "End":
            break

        if Vote in Crewmate:
            Dead[Vote] = Crewmate.pop(Vote)
        elif Vote in Imposter:
            Dead[Vote] = Imposter.pop(Vote)

    print(len(Imposter),"Impostor Remains")
    print("***Alive***")
    Alive = {}
    Alive.update(Crewmate)
    Alive.update(Imposter)
    for key in sorted(Alive):
        print(key, ":", Alive[key])
    print("***Dead***")
    for key in sorted(Dead):
        print(key,":",Dead.get(key))
main()
