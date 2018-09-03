
# coding: utf-8

# In[1]:


class BankAcc:
    balance=0
    def __init__(self):
        self.name = input('Please Enter Your Name: ')
        self.no = input('Please Enter Your Account No: ')
        #self.balance = int(input('Please Enter Intial amount:'))
        #self.balance=balance
        self.AccDetails()
    def Add(self):
        amount=int(input('Enter Amount to Add:'))
        self.balance+= amount
        print('\n----------------------------\n') 
        print('After Adding your updated balance is {} Rupees'.format(float(self.balance)))

    def Withdraw(self):
        amount=int(input('Enter Amount to Withdraw:'))
        if(int(self.balance)>amount):
            self.balance -= amount
            print('\n----------------------------\n') 
            print('After Withdrawing your updated balance is {} Rupees'.format(float(self.balance)))
        else:
            print('You dont have enough amount to withdraw.\n Your Current balance is {} Rupees'.format(float(self.balance)))          
    def BalCheck(self):
        #self.balance += amount
        print('\n----------------------------\n') 
        print('Your updated balance is {} Rupees'.format(float(self.balance)))
    def UpdateName(self):
        Name=input('Enter Updated Name:')
        self.name=Name
        print('Your Updated Name in Bank Records is ',self.name)
        print('\n----------------------------\n') 
    def AccDetails(self):
        print('\n------------Account Details----------------\n')
        print('Hello Mr/Mis: {}'.format(self.name))
        print('Your Account Details are here:')
        print('Acc Holder Name: {} '.format(self.name))
        print('Your Acc Num is: {}'.format(self.no))
        print('Your updated balance is {0:.2f} Rupees'.format(float(self.balance)))
        print('\n----------------------------\n')   
        

