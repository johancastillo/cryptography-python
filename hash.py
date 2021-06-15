import hashlib


class HASH:
    def hashGenerator(h):
        digest = h.hexdigest()
        return digest


x = 0


while x < 1:
    print("Elige el algoritmo a usar:")
    print("1 - SHA256")
    print("2 - SHA512")
    print("3 - Finalizar programa")

    nAlgoritmo = input()


    if nAlgoritmo != "3":
        print("Introduce los datos a hashear")
        data = input()

        algoritmo = ""

        if nAlgoritmo == "1":
            algoritmo = "sha256"
        elif nAlgoritmo == "2":
            algoritmo = "sha512"

        bdata = bytes(data, 'utf8')
        h = hashlib.new(algoritmo, bdata)
        hash1 = HASH.hashGenerator(h)
        print()
        print(hash1)
        print()
    
        x = 0
    else:
        x = 1

print("************")
print("* Good Bye *")
print("************")



