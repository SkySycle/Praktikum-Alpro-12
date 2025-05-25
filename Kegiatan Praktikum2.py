dic_email = dict()
lst = list()

fname = input('Nama File: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File tidak bisa dibuka:', fname)
    quit()

for baris in fhand:
    kata = baris.split()
    if len(kata) < 2 or kata[0] != 'From':
        continue
    email = kata[1]
    if email not in dic_email:
        dic_email[email] = 1
    else:
        dic_email[email] += 1

for key, val in dic_email.items():
    lst.append((val, key))

lst.sort(reverse=True)

jumlah, email = lst[0]
print(email, jumlah)
