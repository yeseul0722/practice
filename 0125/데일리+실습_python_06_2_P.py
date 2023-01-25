grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
# print(grain_lst.sort()) #None 반환
# print(grain_lst) # 정렬된 리스트 확인 /[('감자', 2000), ('고구마', 3000), ('옥수수', 4500), ('토란', 1300)]
# grain_dict = dict(grain_lst)
# key = list(grain_dict.keys())
# value = list(grain_dict.values())
# max_value = 
# print(value.index(max(value))) # 2 # print(value.index(4500))

# max_idx = value.index(max(value))
# print(key[max_idx])
# print(key, value) #dict_keys(['감자', '고구마', '옥수수', '토란']) dict_values([2000, 3000, 4500, 1300])
grain_lst.sort(key=lambda x : x[1], reverse=True) #reverse는 역순으로
print(grain_lst[0][0])