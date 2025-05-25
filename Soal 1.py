data = input("Masukkan data berupa angka, pisahkan dengan koma (contoh: 90,90,90): ")

y = tuple(map(int, data.split(',')))

def semua_sama(t):
    return all(x == t[0] for x in t)

print(semua_sama(y))
