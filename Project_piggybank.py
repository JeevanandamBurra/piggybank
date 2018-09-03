
# coding: utf-8

# In[4]:


import piggybank as pb


# In[7]:


try:
    count=0
    
    while True:
        print('===============================')
        print(' Welcome to Piggy BANK ')
        print('Please choose an options to Start or End.') 
        print('Option 1: Start')
        print('Option 2: End')
        print('===============================')
        option = input('Choose an Option:')
        op=option.upper()
        
        if op== 'START':
            if(count==0):                
                obj=pb.BankAcc()                      
                count=1 
            else:
                
                print('Please Choose any of below mentioned Options:\n')
                print('Add , Withdraw, BalCheck, UpdateName or AccDetails \n')
                Mop = input('Select an Option:')

                mop=Mop.upper()

                if mop=='ADD':
                    obj.Add()
                elif mop=='WITHDRAW':
                    obj.Withdraw()

                elif mop=='BALCHECK':
                    obj.BalCheck()

                elif mop=='UPDATENAME':
                    obj.UpdateName()

                elif mop=='ACCDETAILS':
                    obj.AccDetails()            

                else:
                    print('Please select valid option.')
            
        elif op=='END':            
            print('\n Have a nice day')
            break
        else:
            print('Input a valid Option.')
except ValueError:
    print('Input a valid Option.')

