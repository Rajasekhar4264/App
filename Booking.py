def SingleTon(arg):
    l=[]
    def Inner():
        if len(l)==0:
            l.append(arg())
        return l[0]    
    return Inner
@SingleTon
class Movie1():
    def __init__(self):
        self.Totaltic=200
    def booking(self):
        reqtic=int(input('Enter the no of Tickets Required : '))
        if reqtic<=self.Totaltic:
            print('Tickets Booked Successfully...')
            self.Totaltic-=reqtic
        else:
            print('Tickets Are Not Available')
            print(f'Available Tickets Are Only {self.Totaltic} But You Want More Tickets')

@SingleTon
class Movie2():
    def __init__(self):
        self.Totaltic=200
    def booking(self):
        reqtic=int(input('Enter the no of Tickets Required : '))
        if reqtic<=self.Totaltic:
            print('Tickets Booked Successfully...')
            self.Totaltic-=reqtic
        else:
            print('Tickets Are Not Available')
            print(f'Available Tickets Are Only {self.Totaltic} But You Want More Tickets')
def BUrShow():
    print('1) Movie1 \n2) Movie2')
    movie=int(input('Enter Which Movie You Want To Watch : '))
    if movie==1:
        user=Movie1()
        user.booking()
    elif movie==2:
        user=Movie2()
        user.booking()
    else:
        print('Movie is Not Available')
user1=BUrShow()
print('-'*20)
user2=BUrShow()
print('-'*20)
user3=BUrShow()
print('-'*20)
user4=BUrShow()
