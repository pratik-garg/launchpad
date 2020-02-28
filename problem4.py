#problem 4
duplicate = [int(x) for x in input().split()]
final_list = [] 
for num in duplicate: 
  if num not in final_list: 
    final_list.append(num) 
print(final_list)
