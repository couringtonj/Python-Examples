def find_highest_bidder(bidding_dictionary):
        winner=""
        highest_bid=0
        for bidder in bidding_dictionary:
            bid_amount=bidding_dictionary[bidder]
            if bid_amount>highest_bid:
                highest_bid=bid_amount
                winner=bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")
    
bids={}

continue_bidding=True
while continue_bidding:
    bidder_name=input("What is your name? \n")
    bid=int(input("What is your bid? $"))

    bids[bidder_name]=bid
    
    should_contine=input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    
    if should_contine=="no":
        continue_bidding=False
        find_highest_bidder(bids)
        
    