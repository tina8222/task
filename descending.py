def descending_order(num):
  
    str_num = str(num)
    list_strnum = list(str_num)
    sorted_list = sorted(list_strnum, reverse = True)
    merge_list = "".join(sorted_list)
    final_num = int(merge_list)
    return final_num

print(descending_order(65478)) #87654
print(descending_order(12742)) #74221