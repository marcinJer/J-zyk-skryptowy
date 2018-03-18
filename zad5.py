import datetime

d = input("Podaj date w postaci rrrr-mm-dd \n")

d = d.split('-')

t = datetime.date(int(d[0]), int(d[1]), int(d[2]))

print(t)

print(datetime.date.today() - t)
