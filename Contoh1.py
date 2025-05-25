mahasiswa = [
    ('Andi', 85),
    ('Budi', 92),
    ('Citra', 78),
    ('Dina', 90),
    ('Eka', 88)
]

urut = []
for nama, nilai in mahasiswa:
    urut.append((nilai, nama))

urut.sort(reverse=True)

for nilai, nama in urut:
    print(f"{nama}: {nilai}")
