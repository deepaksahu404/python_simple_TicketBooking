#WRITE A CLASS WHICH HAS METHOD TO BOOK A TICKET,GET STATUS(NO OF SEATS), GET FAIR INFORMATION OF THE TRAINS
#RUNNING UNDER INDIAN RAILWAYS
list = [i for i in range(1,301)]
def helpMessage():
    print('''Recomendeed commends are : 
              - status : to check status
              - book : to book a ticket
              - cancel : to cancel ticket
              - help : to see the help message
              - exit : to exit the program
              ''')
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        #self.seat_no=seat_no
        self.seats=seats
    def getstatus(self):
        print(f"your train name and no is {self.name}")
        print(f"Total seats available is {len(self.seats)} ")
        print(f"Available seats are {self.seats} ")
    def fareInfo(self):
        print(f"The price of the ticket is :rs {self.fare}")
    def bookTicket(self):
        if len(self.seats)>0:
            seat = self.seats.pop()
            print(f"Your ticket has been booked and your seat number is {seat}")
        else:
            print("sorry ! The train is full,You can try Tatkal")
    def cancelseat(self):
        try:
            seat_no = int(input("Enter your seat no :"))
            if seat_no > 300 or seat_no in self.seats:
                print("seat cant not be canceled ,coz seat maynot be booked or was never availlabe!!")
            else:
                self.seats.append(seat_no)
                print(f'Your seat {seat_no} has been canceled , Available seats are {len(self.seats)}')
        except:
            print("Invalid statement")        
            
Intercity=Train("Intercity express : 14507",90,list)
# Intercity.getstatus()
# # Intercity.fareInfo() 
# Intercity.bookTicket()
# Intercity.bookTicket()
# Intercity.bookTicket()
# Intercity.getstatus()  
# Intercity.cancelseat()
print(helpMessage())
while True:
    statement = input("enter statement :")
    if statement == 'status':
        Intercity.getstatus()
    elif statement == "book":
        try:
            n = int(input("how many seats u want to book? :"))
            for i in range(n):
                Intercity.bookTicket()
        except:
            print("Invalid statment")
    elif statement == "cancel":
        Intercity.cancelseat()
    elif statement == "help" or statement == 'h':
        helpMessage()
    elif statement == "exit":
        exit()
    else:
        print("\nenter a valid statement")
 