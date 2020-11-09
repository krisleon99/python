item = [1,2,3,[4,5,[6,7,[8,9]]],10,11]
print(item)
arr_items = []

def check(value):
	if isinstance(value, list):
		for x in value:
			check(x)
	else:
		arr_items.append(value)
	

for x in item:
	check(x)
	
print("tu lista final es:")
print(arr_items)
