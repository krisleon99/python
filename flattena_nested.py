item = [1,2,3,[4,5,[6,7,[8,9]]],10,11]
print(item)
arr_items = []

def check(value):
	print(value)
	if isinstance(value, str):
		arr_items.append(value)
	elif isinstance(value, int):
		arr_items.append(value)
	elif isinstance(value, list):
		for x in value:
			check(x)
	
	print("tu lista es:")
	print(arr_items)
	

for x in item:
	check(x)