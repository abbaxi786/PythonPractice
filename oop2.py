
class BankAccount:
    def __init__(self,holderName,deposit=0):
        
        self.deposit = deposit
        self.holderName = holderName        
        pass

    def DepositAmmount(self,amount):
        self.deposit += amount
        print(f"This {amount} have been add to your account and your amount is {self.deposit}")

        
    def WithdrawAmount(self,amount):
        if(self.deposit == 0):
            print("The account is empty")
        elif(amount>self.deposit):
            print("Not enough amount !!")
            return
        else:
            self.deposit-= amount
            print(f"This {amount} have been deducted from your account and you remaing is {self.deposit}")
        
def main():
    B1 = BankAccount("Faraz",5000)
    B1.DepositAmmount(750)
    B1.WithdrawAmount(400)
    B1.WithdrawAmount(5356)
    B1.WithdrawAmount(500)
    B1.WithdrawAmount(4850)
    B1.WithdrawAmount(500)
    
if(__name__ == "__main__"):
    main()