#q3
def sumDigitSqrVerI(n):
	ans = 0
	while n > 0:
		ans += (n%10)**2
		n //= 10
	return ans

#q4
def sumDigitSqrVerR(n):
	if n < 10:
		return n
	return n%10 + sumDigitSqrVerR(n//10)
	
#q5
def sumDigitSqrVerUltimate(n):
	return sum(list(map(lambda x:int(x)**2, str(n))))

#q6
def isHappyNumber(n):
	if n in [1, 7]:
		return True
	elif n < 10:
		return False
	digitSum = 0
	while n > 0:
		digitSum += (n%10)
		n = n//10
	return isHappyNumber(digitSum); 

#q7
class ConfusedFighter(Fighter):
	def __init__(self):
		super().__init__()
		self.name = 'ConfusedFighter'
		self.cost = 50
		
	def act(self,myTeam,enemy):
	
		rndNumber = randint(1, 100):
		if rndNumber <= 25:
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
		damage = min(self.str, enemy.hp)
		dprint(f'Hurt enemy {target} by damage {self.str}.')
		enemy[target].gotHurt(self.str)
		self.hp = min(self.maxhp, self.hp + damage * 0.5)

def deep_map(f,tree):

	ans = ()
	for i in tree:
		if type(i) != tuple:
			ans += (f(i),)
		else:
			ans += (deep_map(f,i),)
	return ans
	
def product(string, n):
	if not n or not string:
		return ""
	if n==1:
		return [i for i in string]
	ans = []
	for i in range(len(string)):
		currLetter = string[i]
		permutedStr = product(string[:i] + string[i:], n-1)
		for s in permutedStr:
			ans.append(currLetter + s)
	return list(set(ans))
	
	

	