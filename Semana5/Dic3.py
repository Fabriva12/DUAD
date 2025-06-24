dictionary= {
    "key_1": "dog",
    "key_2": "cat",
    "key_3": "fish",
    "key_4": "sheep"
}
deleted_list= ["key_2","key_3"]
for key in deleted_list:
    dictionary.pop(key,None)
print(dictionary)