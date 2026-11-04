# 3/11/26

#Polymophism

# class CashPayment:

#     def pay(self,amount):
#         print("Paid",amount,"using cash")


# class UPIPayment:

#     def pay(self,amount):
#         print("Paid",amount,"using upi")

# class Cardpayment:

#     def pay(self,amount):
#         print("Paid",amount,"using card")

# class Netbanking:
     
#     def pay(self,amount):
#         print("Paid",amount,"using netbanking")

# payment=[
#     CashPayment(),
#     UPIPayment(),
#     Cardpayment(),
#     Netbanking()
# ]

# choice=input("Choose payment method (cash/upi/card/netbanking):")  
# if choice == "cash":
#     payment=CashPayment()
# elif choice == "upi":
#     payment = UPIPayment()
# elif choice == "card":
#     payment = Cardpayment()
# elif choice == "netbanking":
#     payment = Netbanking()
#     exit()

# payment.pay(1000)

# class SMS:
#     def send(self,message):
#         print("Sending massage through SMS:",message)

# class Facebook:
#     def send(self,message):
#         print("Sending massage through facebook:",message)
# class Whatsapp:
#     def send(self,message):
#         print("Sending massage through Whatsapp:",message) 

# class Instagram:
#     def send(self,message):
#         print("Sending massage through Instagram:",message)


# choice=input("choose massage methode(SMS/facebook/whatsapp/Instagram): ").lower()
# if choice == "sms":
#     message=SMS()

# elif choice == "Facebook":
#     message = Facebook()

# elif choice =="whatsapp":
#     message = Whatsapp()

# elif choice == "Instagram":
#     message = Instagram()

#     exit()

# message.send("Good morning friends")