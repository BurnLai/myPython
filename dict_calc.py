# # simple dictionary addition
# inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#
# def check_qty(stuff):
#     total = 0
#     print('Inventory:')
#     for k, v in inventory.items():
#         total = total + v
#         print(v, k)
#     print(f"The total inventory are : {total}")
#
#
# check_qty(inventory)



allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

# calculate items total brought
def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought


print('Number of things being brought:')
print(' - Apples         ' + str(total_brought(allGuests, 'apples')))
print(' - Cups           ' + str(total_brought(allGuests, 'cups')))
print(' - Cakes          ' + str(total_brought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(total_brought(allGuests, 'apple pies')))