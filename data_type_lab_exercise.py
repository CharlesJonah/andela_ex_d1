def data_type(val):
	#Checks if datatype is string
	if isinstance(val,str):
		return len(val)
	#Checks if datatype is None
	if val is None:
		return 'no value'
	#Checks if datatype is boolean
	if isinstance(val,bool):
		return val
	#Checks if datatype is integer
	if isinstance(val,int):
		#Checks if the integer is less than 100
		if val < 100:
			return 'less than 100'
		#Checks if the integer is greater than 100
		elif val > 100:
			return 'more than 100'
		#Checks if integer is equal to 100
		elif val == 100:
			return 'equal to 100'
		else:
			pass
		#Checks if the datatype is a list
	if isinstance(val,list):
		#Checks if the list has the required minimum length
		if len(val) < 3:
			return None
		else:
			return val[2]