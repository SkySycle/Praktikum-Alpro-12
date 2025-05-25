name = input("Enter a file name: ")
try:
    fhand = open(name)
except:
    print("File tidak ditemukan.")
    quit()

import re
counts = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time.split(':')[0]
        counts[hour] = counts.get(hour, 0) + 1

for k in sorted(counts):
    print(k, counts[k])
