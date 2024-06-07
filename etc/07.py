# 기본 은행 계좌 클래스

class Log():
	Logs = []
	def __init__(self):
		pass
	def append(self, change, money, owner, balance):
		self.Logs.append(f"{change} {money} \n 계좌주: {owner} 잔액: {balance}")
	def show_log(self):
		for i in self.Logs:
			print(i+"\n")
Today_log = Log()

class BankAccount:
	record = []
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance
		Today_log.append("new", balance, owner, balance)
	def deposit(self, money):
		self.balance += money
		Today_log.append("deposit(+)", money, self.owner, self.balance)
		return "deposit(+)", money, self.owner, self.balance
	def withdraw(self, money):
		self.balance -= money
		Today_log.append("withdraw(-)", money, self.owner, self.balance)
		return "withdraw(-)", money, self.owner, self.balance
	def __str__(self):
		return f"계좌 소유자: {self.owner} \n 잔액: {self.balance}"
	def __add__(self, other):
		if isinstance(other, BankAccount):
			return BankAccount(f"{self.owner} & {other.owner}", self.balance + other.balance)
		return NotImplemented
	def __eq__(self, other):
		if isinstance(other, BankAccount):
			return self.balance == other.balance
		return NotImplemented
	
# 저축 계좌 클래스 (이자 기능 추가)
class SavingsAccount(BankAccount):
	def add_interest(self, point): 
		eja = self.balance * (point)
		self.balance = self.balance * (1 + point)
		Today_log.append("interest", eja, self.owner, self.balance)
		return "interest", eja, self.owner, self.balance
		
# 당좌 계좌 클래스 (오버드래프트 기능 추가)
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, overdraft_limit):
        self.owner = owner
        self.balance = balance
        self.overdraft = overdraft_limit
		
    def withdraw(self, money):
        if self.balance >= self.overdraft:
            self.balance -= money
            Today_log.append("withdraw(-)", money, self.owner, self.balance)
            return "withdraw(-)", money, self.owner, self.balance
        else: print("Insufficient funds, overdraft limit reached")

class Customer:
	accounts = []
	def __init__(self, name):
		self.name = name
	def add_account(self, account):
		self.accounts.append(account)
	def get_total_balance(self):
		sum = 0
		print("hihihihi")
		for i in self.accounts:
			sum += i.balance
		print("hihihi")
		return sum
		

# 예시 실행
acc = BankAccount("Charlie", 500)
print(acc)
print(acc.deposit(100))
print(acc.withdraw(200))
print(acc.withdraw(500))

acc1 = SavingsAccount("Alice", 1000)
acc1.add_interest(0.05)
print(acc1)

acc2 = CheckingAccount("Bob", 500, 200)
print(acc2.withdraw(600))
print(acc2)

customer = Customer("Alice")
acc1 = SavingsAccount("Alice", 1000)
acc2 = CheckingAccount("Alice", 500, 200)
customer.add_account(acc1)
customer.add_account(acc2)
print(customer)
print(customer.get_total_balance())
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 1500)
acc3 = acc1 + acc2
print(acc3)
print(acc1 == acc2)
acc4 = BankAccount("Charlie", 1000)
print(acc1 == acc4)

Today_log.show_log()