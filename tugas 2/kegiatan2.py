data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

def findInteger(data) :
    parts = data.split()
    integers = list(filter(lambda x : x.isdigit(),parts))
    return integers
    
splitted_integers = list(map(findInteger, data))

for integers in splitted_integers:
    print (integers)