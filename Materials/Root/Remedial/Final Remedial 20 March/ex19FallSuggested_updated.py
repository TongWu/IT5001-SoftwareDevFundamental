#q3
def sumDigitSqrVerI(n):
	ans = 0
	while n > 0:
		ans += (n%10)**2
		n //= 10
	return ans

#q4
def sumDigitSqrVerR(n):
	if n < 10: #base case
		return n**2
	#recursive step
	return (n%10)**2 + sumDigitSqrVerRn(n//10)

#SDS(12345)
# = SDS(1234) + 5**2
# = SDS(123) + 4**2 + 5**2

#q5
#n = 12345 , str(n) = "12345"
def sumDigitSqrVerUltimate(n):
	def f(x):
		return int(x) ** 2
	mapLst = list(map(f, str(n)))
	return sum(mapLst)

#q6
def isHappyNumber(n):
	if n in [1, 7]: #base case
		return True
	elif n < 10:
		return False
	#sumDigitSqrVerI is from Q4
	return isHappyNumber(sumDigitSqrVerI(n)); 

def isHappyNumberIterative(n):
	while n > 10:
		n = sumDigitSqrVerI(n)
	return n in [1, 7]


#q7
class ConfusedFighter(Fighter):
	def __init__(self):
		super().__init__()
		self.name = 'ConfusedFighter'
		self.cost = 50
		
	def act(self,myTeam,enemy):
	
		rndNumber = randint(1, 4)
		if rndNumber == 1:
			super().act(enemy, myTeam);
		else:
			super().act(myTeam, enemy); 

class Vampire(Fighter):
	def __init__(self):
		super().__init__()
		self.name = 'vampire'
		self.cost = 300
		
	def act(self,myTeam,enemy):
	
		target = randAlive(enemy)
		#enemy.hp = 10
		#self.str = 100
		damage = min(self.str, enemy.hp)
		dprint(f'Hurt enemy {target} by damage {self.str}.')
		enemy[target].gotHurt(self.str)
		self.hp = min(self.maxhp, self.hp + damage * 0.5)
	
	#attack all alive enemies
	def act(self,myTeam,enemy):
		for target in enemy:
			dprint(f'Hurt enemy {target} by damage {self.str}.')
			enemy[target].gotHurt(self.str)
			
def deep_map(f,tree):
	ans = () #result array
	for i in tree:
		if type(i) != tuple: #curr item not a tuple
			ans += (f(i),)
		else: 
			ans += (deep_map(f,i),)
	return ans
	
def deep_map(f,tree):	
    if tree==():
        return tree
    elif type(tree)!= tuple:
        return f(tree)
    else:
        return (deep_map(f,tree[0]),)+deep_map(f,tree[1:])


#deep_map(f,  (((81,),),)))
#= (deep_map(f, ((81,),),),)
#= ((deep_map(f, (81,),),),)
def product(string, n):
	if n == 0 or string == "":
		return ""
	if n==1:
		return [i for i in string]
	ans = []
	#all permutations of length n-1
	permutedStr = product(string, n-1)
	for i in range(len(string)):
		currLetter = string[i] #let currLetter be the first letter
		for s in permutedStr: #consider every single permutation
			ans.append(currLetter + s)
	return ans

#string = "abc"
#product("abc", 3)

#permutedStr =
#product("abc", 2)
#aa, ab, ac
#ba, bb, bc
#ca, cb, cc

#product("abc", 3)
#aaa, aab, aac
#aba, abb, abc
#aca, acb, acc
#baa, bab, bac
#bba, bbb, bbc
#bca, bcb, bcc
#caa, cab, cac
#cba, cbb, cbc
#cca, ccb, ccc


#product("abc", 1)
#[a, b, c]


#product("abc", 2)
##aa, ab, ac
#ba, bb, bc
#ca, cb, cc

#rec2('1234','5')
#=rec2("234", "15") + "0"
#=rec2("34", "115") + "0" + "0"
#=rec2("4", "1115") + "0" + "0" + "0"
#=rec2("", "11115") + "0" + "0" + "0" + "0"
#="11115" + "0" + "0" + "0" + "0"
#111150000
	