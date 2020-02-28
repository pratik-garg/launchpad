#problem3 
a = [int(x) for x in input().split()]
ele = int(input("Enter element:"))
count = -1;
for i in a:
	count = count + 1;
	if ele == i:
		print(count)
