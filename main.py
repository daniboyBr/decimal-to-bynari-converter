

def main():
    num_decimal = 1
    binario = []
    resto = 0

    while (True):
        resultado = int(num_decimal / 2)
        resto = int(num_decimal % 2)
        num_decimal = resultado

        binario.insert(0, str(resto))

        if (resultado == 1 or resultado == 0):
            binario.insert(0, str(resultado))
            break
            
    print("".join(binario))

if __name__ == "__main__":
    main()
