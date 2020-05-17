# coding : utf-8

# from operator import itemgetter
# phone_book = {"Linda": "7750", "Bob": "9345", "Carol": "5834"}
#
# print({k:phone_book[k] for k in sorted(phone_book,key=lambda k:phone_book[k],reverse=True)})
# a = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# print(sorted(a,key=itemgetter(1,2)))

# my_dict = {"Li":["M",7],"Zhang":["E",2],"Wang":["P",3],"Du":["C",2],"Ma":["C",9],"Zhe":["H",7]}
#
# game_result = [{"name":"Bob","wins":10,"losses":3,"rating":75},{"name":"David","wins":3,"losses":5,"rating":57},{"name":"Carol","wins":4,"losses":5,"rating":57},{"name":"Patty","wins":9,"losses":3,"rating":71.48}]
#
# a=sorted(game_result,key=lambda item:(item["rating"],item["name"]))
# b=[{'losses': 5, 'name': 'Carol', 'rating': 57, 'wins': 4}, {'losses': 5, 'name': 'David', 'rating': 57, 'wins': 3}, {'losses': 3, 'name': 'Patty', 'rating': 71.48, 'wins': 9}, {'losses': 3, 'name': 'Bob', 'rating': 75, 'wins': 10}]
# print(a)
# print(a==b)
from collections import Counter
some_data = ["a", "2", 2, 4, 5, "2", "b", 4, 7, "a", 5, "d", "z", "a"]

c=Counter(some_data)
print(dict(c))


