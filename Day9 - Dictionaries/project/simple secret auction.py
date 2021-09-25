"""Simple"""

from art import logo
import re
print(logo)

bids = {}
bid_over = False


def largest_num(dic: dict):
    num = 0
    bidder = ""
    for k, v in dic.items():
        if v > num:
            num = v
            bidder = k
    return bidder, num


while not bid_over:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: ").replace("$", ""))
    bids[name] = bid
    bidding_over = input("Is there another bidder?: ")
    if 'n'.lower() in bidding_over:
        bid_over = True
        print(f"The winner is {largest_num(bids)[0]} with a bid of ${largest_num(bids)[1]}")
