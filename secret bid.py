from art import logo
print(logo)
bids={}
bidding_finish=False

def find_highest_bidder(bidding_record):
    highest_bid=0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bidding amount ${highest_bid}")
while not bidding_finish:
    name=input("What is your name? : ")
    price=int(input("What is your bid? $ :"))
    bids[name]=price
    other=input("Are there any other bidder 'yes' or 'no'?:")
    if other=="no":
        bidding_finish=True
        find_highest_bidder(bids)
   