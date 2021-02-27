side = int(input("Nummber of pound signs: "))
for i in range(side+1):
    print(" " * (side-i) + "#" * i)