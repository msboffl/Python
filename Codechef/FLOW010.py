T = int(input("Enter Test Cases: "))
for _ in range(T):
    alphabet = str(input("Enter String: "))
    if(alphabet == "B" or "b"):
        print("BattleShip")
    elif(alphabet == "C" or "c"):
        print("Cruiser")
    elif(alphabet == "D" or "d"):
        print("Destroyer")
    elif(alphabet == "F" or "f"):
        print("Frigate")
