def parkingDillema(cars, k):
	n = len(cars)
	if 0 == n or k < 0:
		return 0
	
	cars.sort()
	roofSize = 100000
	
	for index,value in enumerate(cars):
		curr = cars[index+k-1] - cars[index] + 1
		if roofSize > curr:
			roofSize = curr
		if index + k == n:
			break
	return roofSize


cars = [2,10,8,17]
k = 3

result = parkingDillema(cars, k)

cars = [1,2,3,10]
k = 4

result = parkingDillema(cars, k)