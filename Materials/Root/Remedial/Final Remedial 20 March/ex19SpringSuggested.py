#q3
def gen(N):
	#return [randint(1, 6) for i in range(N)]
	ans = []
	for i in range(N):
		ans.append(randint(1, 6))
	return ans

def tally(nlist):
	ans = [0,0,0,0,0,0]
	#for i in range(6):
	#	ans[i] = sum(j == (i+1) for j in nlist)
	#return ans
	def count(lst, x):
		ans = 0
		for i in lst:
			if i == x:
				ans += 1
		return ans
	for i in range(6):
		ans[i] = count(nList, i+1)
	return ans 

def checkBingo(nlist):
	talliedList = tally(nlist)
	for i in talliedList:
		if i < 3:
			return False
	return True 

def calProbBingo(N):
	nBingo = 0
	for i in range(N):
		randomBoard = gen(40)
		nBingo += checkBingo(randomBoard)
	return nBingo/N

#q3 task 5 - wishful thinking 

#q4t1 - VendingMachine
#q4t2 - __init__

class CoffeeMchine(VendingMachine):
	def __init__(self):
		self.drinkOption = ["coffee", "tea"]
	
#q4t3 - CoffeeMachine 

#q4t4 - __init__, buyDrink 

class PremiumCoffeeMachine(CoffeeMachine):
	def __init__(self):
		super().__init__(); 
		self.drinkOption.append("Latte")
		self.drinkOption.append("Cappuccino");
		self.sugar = True 
		#asume by default got sugar
	
	def pressAddSugarButton(self):
		self.sugar = True
		print("add sugar pls")
	
	
	def pressNoSugarButton(self):
		self.sugar = False	
		print("no sugar pls")
	
	def dispense(self, drink):
		if (self.sugar):
			print(drink + "dispensed with sugar")
		else:
			print(drink + "dispensed without sugar")


def search(L,n):
	if len(L) == 0:
		return False #redundant 
	for i in L:
		if i == n:
			return True
	return False	

def findSMest(L):
	smallest = L[0]
	largest = L[0]
	for i in L:
		if i < smallest:
			smallest = i
		if i > largest:
			largest = i
	return (smallest, largest);


def DNAreversal(dna,pos,l):
	def revStr(str):
		#return str[::-1]
		ans = ""
		for i in str:
			ans = i + ans
		return ans
	return dna[:pos] + revStr(str[pos:pos+l]) + dna[pos+l:]
		
	


	