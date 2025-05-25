data = ('Jochelino Felix Kurniawan', '71241156', 'Jakarta Selatan, DKI Jakarta')

nama = data[0]
nim = data[1]
alamat = data[2]

print("NIM :", nim)
print("NAMA :", nama)
print("ALAMAT :", alamat)

nim_tuple = tuple(nim)
print("NIM:", nim_tuple)

nama_depan = tuple(nama.split()[0].lower())
print("NAMA DEPAN:", nama_depan)

nama_terbalik = tuple(nama.split()[::-1])
print("NAMA TERBALIK:", nama_terbalik)
