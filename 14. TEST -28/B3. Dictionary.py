students = [ #list of dictionary
    {"id":1,"name":"John","age":12},
    {"id":2,"name":"Smith","age":13},
    {"id":3,"name":"Sourav","age":30},
    {"id":4,"name":"Joe","age":22},
    {"id":5,"name":"Ronn","age":24}
]

for it in students:
    for k in it.keys():
        print(f"{k} : {it[k]}")


