def invest(cap, int, anni):
	schei=cap*(1+(int/100.0))**anni		#formula interesse composto
	return(schei)
print invest(1000, 10, 2)
