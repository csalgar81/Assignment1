def main():
    request_pool = ['R','C','A','M','Q']
    print("Shopping List v1 - Carlos Salgar")
    print("R - List Required Items\nC - List Completed Items\nA - Add new item\nM - mark an item as completed\nQ - Quit")
    load_items_file()
    user_request = input(">>> ").upper()
    while user_request not in request_pool:
        print("Not valid")
        user_request = input(">>> ").upper()

def load_items_file():
    import csv
    items_file = open("items.csv", "r")
    items_reader = csv.reader(items_file)
    items_names = []
    items_prices = []
    items_priorities = []
    items_status = []
    i = 0
    for row in items_reader:
        items_names.append(row[0])
        items_prices.append(row[1])
        items_priorities.append(row[2])
        items_status.append(row[3])

main()