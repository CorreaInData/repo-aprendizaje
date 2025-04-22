frase = str(input("Escribe una frase: ")).lower()

vocal_a, vocal_e, vocal_i, vocal_o, vocal_u= 0, 0, 0, 0, 0
consonantes = 0

for i in frase:
    if i.isalpha():
        if i == "a":
            vocal_a += 1
        elif i == "e":
            vocal_e += 1
        elif i == "i":
            vocal_i += 1
        elif i == "o":
            vocal_o += 1
        elif i == "u":
            vocal_u += 1
        else:
            consonantes += 1
    else:
        pass

print("\nResumen")
print("- Vocales:", vocal_a + vocal_e + vocal_i + vocal_o + vocal_u)
print("  - A:", vocal_a)
print("  - E:", vocal_e)
print("  - I:", vocal_i)
print("  - O:", vocal_o)
print("  - U:", vocal_u)
print("- Consonantes:", consonantes)
