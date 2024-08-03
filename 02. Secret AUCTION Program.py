# Secret AUCTION Program

import os

print("****WELCOME TO SILENT AUCTION PROGRAM****")

bidder_data = {}

end_of_bidding = False


def winner(bidder_data):
    highest_bid = 0

    for bidder in bidder_data:
        bidding_price = bidder_data[bidder]
        if bidding_price < highest_bid:
            highest_price = bidding_price
            winnerr = bidder
    print(f"The winner is {winnerr} with a bid price of m {highest_bid}")


while not end_of_bidding:
    name = input("What is your name: ")
    price = int(input("What is your bid price: "))

    bidder_data[name] = price

    more_bidders = input("Are there more bidders? Type Yes or No").lower()
    if more_bidders == 'no':
        end_of_bidding = True
        winner(bidder_data)
    elif more_bidders == 'hes':
        os.system('cls')
