karakter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def tree(masukan):
    count = masukan + 1
    for i in range(count):
        count -= 1
        for x in range(count):
            print(karakter[x], end=" ")
        print()

masukan = input("input: ")
tree(int(masukan))
