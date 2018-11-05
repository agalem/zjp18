def selection(chart, prime_implicants):
	temp = []
	select = [0]*len(chart)
	for i in range(len(chart[0])):
		count = 0
		rem = -1
		for j in range(len(chart)):
			if chart[j][i] == 1:
				count += 1
				rem = j
		if count == 1:
			select[rem] = 1
	for i in range(len(select)):
		if select[i] == 1:
			for j in range(len(chart[0])):
				if chart[i][j] == 1:
					for k in range(len(chart)):
						chart[k][j] = 0 
			temp.append(prime_implicants[i])
	while 1:
		max_n = 0; rem = -1; count_n = 0
		for i in range(len(chart)):
			count_n = chart[i].count(1)
			if count_n > max_n:
				max_n = count_n
				rem = i
		
		if max_n == 0:
			return temp
		
		temp.append(prime_implicants[rem])
		
		for i in range(len(chart[0])):
			if chart[rem][i] == 1:
				for j in range(len(chart)):
					chart[j][i] = 0