# Create a Basic Bank account managing
class SBI:
    ROI=0.07
    def __init__(self,name,Mobno,Aadhar,PAN,Bal,Pin):
        self.name=name
        self.Mobno=Mobno
        self.Aadhar=Aadhar
        self.PAN=PAN
        self.Bal=Bal
        self.Pin=Pin
    def Details(self):
        print(f'''
            name   :  {self.name}
            Mobno  :  {self.Mobno}
            Aadhar :  {self.Aadhar}
            PAN    :  {self.PAN}
            Bal    :  {self.Bal}''')
    def withdraw(self):
        if self.checkpin()==self.Pin:
            amount=int(input("Enter Amount to Withdraw : "))
            if self.Bal>=amount:
                self.Bal-=amount
                print("Amount Debited Succeesfully")
                print(f'Available Bal is {self.Bal}')
            else:
                print('Insufficient Balance')
        else:
            print('Enter Correct Pin')
    @staticmethod
    def checkpin():
        return int(input('Enter your pin : '))
    def deposit(self):
        amount=int(input("Enter Amount to Deposit : "))
        self.Bal+=amount
        print('Amount Credited Successfully')
        print(f'Available Balance is {self.Bal}')
    def checkbal(self):
        print(f'Available Bal is {self.Bal}')
    @classmethod
    def ChangeROI(cls):
        changedROI=float(input('enter the New ROI : '))
        cls.ROI=changedROI
    def changepin(self):
        oldpin=int(input('Enter your Old Pin : '))
        if self.Pin==oldpin:
            newpin=int(input('Enter your New Pin'))
            self.Pin=newpin
            print('Your Pin is Changed')
        else:
            print("Enter Valid Pin ")
cust1=SBI('RAJ',1234567890,123465789087,'ADFS6354',10000,9876)
cust2=SBI('RAM',9543217890,233876510953,'FDRE5427',9000,8765)
cust2.changepin()