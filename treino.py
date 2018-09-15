def searchInList(search='', matriz=[]):
	result = []
	if len(matriz) > 0:
		for item in matriz:
			itemLower = item.lower();
			if itemLower.startswith(search.lower()):
				result.append(item)
	
	return result[:5];

print(searchInList('t',['Teste','teste2','tesas','tesadsf','adsfasd','fasdf','Fadsfa','fdsaf','fdsafklj','fdsfa','fsadfas','fdsafa']))
			