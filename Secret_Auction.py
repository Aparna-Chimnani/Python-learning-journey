print("Welcome to the secret auction program.\n")
name= input("What is your name? \n")
bid= int(input("What is your bid?$ \n"))

dict={}
dict[name]=bid

question=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

continue_bidding=True

while continue_bidding:
    if question == 'yes':
        print('\n'*35)
        name= input("What is your name? \n")
        bid= int(input("What is your bid?$ \n"))
        dict[name]=bid
        question=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        
    else:
        continue_bidding=False
        max_bid=max(dict.values())
        for name, bid in dict.items():
            if bid == max_bid:
                print(f"The winner is {name} with a bid of ${max_bid}.")