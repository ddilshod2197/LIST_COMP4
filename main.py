matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
juftlar = [x for row in matrix for x in row if x % 2 == 0]
print(juftlar)

names = ["Ali", "vali", "Olim", "sardor", "Nodir"]
katta_boshli = [n for n in names if n[0].isupper()]
print(katta_boshli)
