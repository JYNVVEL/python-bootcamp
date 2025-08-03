binary_h = list(bin(ord('h')))
binary_h = binary_h[2:]

binary_a = list(bin(ord('a')))
binary_a = binary_a[2:]

binary = (binary_h + binary_a) * 3

print(binary)