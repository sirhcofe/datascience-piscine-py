def NULL_not_found(object: any) -> int:
	obj_type = type(object)

	if object is None:
		print(f"Nothing: None {obj_type}")
	elif isinstance(object, float) and object != object:
		print(f"Cheese: nan {obj_type}")
	elif isinstance(object, int) and object == 0:
		print(f"Zero: 0 {obj_type}")
	# strip: returns a copy of the string by removing both the leading and the trailing characters
	elif isinstance(object, str) and len(object.strip()) == 0:
		print(f"Empty: {obj_type}")
	elif isinstance(object, bool) and object is False:
		print(f"Fake: False {obj_type}")
	else:
		print("Type not Found")
		return 1
	return 0