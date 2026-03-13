import art
print(art.logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

continue_bidding = True
auction_users = {}
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid price?: $"))
    auction_users[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(auction_users)
    elif should_continue == "yes":
        print("\n" * 5)
