frase = str(input("Escribe una frase: ")).lower()

vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
consonantes = 0

for letra in frase:
    if letra.isalpha():
        if letra in vocales:
            vocales[letra] += 1
        else:
            consonantes += 1

print("\nResumen")
print(f"- Vocales: {sum(vocales.values())}")
for vocal, cantidad in vocales.items():
    print(f"  - {vocal.upper()}: {cantidad}")
print("- Consonantes:", consonantes)
