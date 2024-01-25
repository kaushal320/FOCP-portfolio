print("BPP Pizza Price Calculator")
print("=========================")
#FOR NUMBER OF PIZZAS
while True:
     while True:
          try:
               num_of_pizza=int(input("How many pizzas ordered? "))
               if num_of_pizza<=0:
                    print("Enter a positive integer!") 
               else:
                    break
          except ValueError:
               print("Please enter a valid number!")
                    
                    
     #FOR DELIVERY REQUIRED
     while True:
          delivery=input("Is delivery required(Y/N)? ")
          delivery.lower()
          if delivery not in ['y','n']:
               print("please answer'Y'or 'N'")
          else:
               break
     #FOR TUESDAY
     while True:
          tuesday=input("Is it Tuesday(Y/N)? ")
          tuesday.lower()
          if tuesday not in ['y','n']:
               print("Answer either 'Y'or'N'")
          else:
               break
     #For if the customer uses the app
     while True:
          app=input("Did the customer use the app(Y/N)? ")
          app.lower()
          if app not in ['y','n']:
               print("please answer'Y'or'N'")
          else:
               break
     #CALCULATE THE TOTAL PRICE
     Pizza_price=12 
     delivery_cost=2.5
     if tuesday=='y':
          Pizza_price=Pizza_price* 0.5 #FOR TUESDAY DISCOUNT
     total_price=num_of_pizza * Pizza_price

     if delivery=='y' and num_of_pizza<5:
          total_price=total_price+delivery_cost

     if app=='y':
          total_price=total_price*0.75

     total_price=round(total_price,2)
     print(f"Total price:£{total_price:.2f}.")


         
        
