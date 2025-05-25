directory = {}

directory[('Andi', 'Wijaya')] = '081234567890'
directory[('Budi', 'Santoso')] = '085612345678'
directory[('Citra', 'Lestari')] = '082298765432'

for (last, first), nomor in directory.items():
    print(f"{first} {last}: {nomor}")
