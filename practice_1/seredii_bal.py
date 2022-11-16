from operator import itemgetter, attrgetter, methodcaller

bal = {"Igor Ezerskiy": [1, 5, 7, 4],
       "Vasia Pupkin": [5, 1, 8, 2],
       "Oleg Fomenko": [1, 1, 2, 5],
       "Ilia Gorban": [1, 4, 5, 8]}
bal_ser = {}
bal_sorted = []
j = 0

for k, v in bal.items():
    for i in v:
        j += i
    bal_ser[k] = j/len(v)
    j = 0
for k, v in sorted(bal_ser.items()):
    bal_sorted.append((k, v))

print(sorted(bal_sorted, key=itemgetter(1), reverse=True))
