username="Nagaraju"
PIN="939163"

import datetime as d
now=d.datetime.now()

cus_name=input("Enter your name :")
cus_pass=str(input("Enter your PIN:"))


if cus_name==username and cus_pass==PIN :
      print('''
1.Deposit
2.Withdraw
3.ministatement
4.exit
       ''')
amount=50000

option=int(input("select your option :"))
if option==1:
      conf_deposit = input('Deposit is confirm ?(yes/no): ')

      if conf_deposit.lower() == 'yes':
        print('Deposit is confirmed.')
      elif conf_deposit.lower() == 'no':
        print('Deposit is not confirmed.')
        print('=======ServerBusy=======')

      else:
             print('Please type either "yes" or "no".')

      dep=int(input("Enter your amount :"))
      amount+=dep
      print("Total amount:",amount)
      print(now.strftime("%c"))
elif option==2:
     conf_with = input('With draw is confirm ?(yes/no): ')

     if conf_with.lower() == 'yes':
        print('Withdraw is confirmed.')
     elif conf_with.lower() == 'no':
        print('Withdraw is not confirmed.')
        print('=======ServerBusy========')

     else:
             print('Please type either "yes" or "no".')


     withd=int(input("Enter your amount :"))
     amount-=withd
     print("total amount :",amount)
     print(now.strftime("%c"))

elif option==3:
      
      print("========ATM========")
      print("Username :",username)
      print("total amount",amount)
      print(now.strftime("%c"))
      print("===================")
      print("Thanks for visiting")
      print("===================")
elif option==4:
      conf_exit = input('Exit is confirm ?(yes/no): ')

      if conf_exit.lower() == 'yes':
        print('Exit.')
      elif conf_exit.lower() == 'no':
        print('Don''t Exit.')
      else:
             print('Please type either "yes" or "no".')

      print(now.strftime("%c"))
else:
      print("Enter your correct logins")


