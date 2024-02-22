# set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
print(primer)

# primer.add(5)
# primer.remove(1)
# print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)

print(segundo)

# Unión |
print(primer | segundo)
# Intersección &
print(primer & segundo)
# Diferencia -
print(primer - segundo)
# Diferencia simétrica ^, es como un XOR
print(primer ^ segundo)

if 5 in segundo:
    print("Hola mundo")
