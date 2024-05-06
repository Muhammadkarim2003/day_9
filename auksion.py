from replit import clear
from art import logo

print(logo)
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"G'olib {winner}, Taklifi ${highest_bid}")

while not bidding_finished:
    name = input("Ismingiz nima? ")
    price = int(input("Sizning taklifingiz nima? $"))
    bids[name] = price
    should_continue = input("Boshqa ishtirokchilar bormi? 'ha' yoki 'yoq': ")
    if should_continue == "yoq":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "ha":
        clear()
