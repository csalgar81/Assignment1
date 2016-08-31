def main():

    def print_required_items():
        row_number = 0
        i = 0
        total_price=0
        for status in items_status:
            if status == 'r':
                print("{}.  {}\t$  {:<6.2f} ({})".format(row_number, items_names[i], items_prices[i], items_priorities[i]))
                row_number += 1
                total_price += items_prices[i]
            i += 1
        print("Total expected price for {} items: ${:.2f}".format(row_number+1,total_price))

    def user_input():
        request_pool = ['R', 'C', 'A', 'M', 'Q']
        user_request = input(">>> ").upper()
        while user_request not in request_pool:
            print("Not valid")
            user_request = input(">>> ").upper()
        return user_request

    # Import items.csv file
    import csv
    items_file = open("items.csv", "r")
    items_reader = csv.reader(items_file)
    items_names = []
    items_prices = []
    items_priorities = []
    items_status = []
    for row in items_reader:
        items_names.append(row[0])
        items_prices.append(float(row[1]))
        items_priorities.append(row[2])
        items_status.append(row[3])

    print("Shopping List v1 - Carlos Salgar")
    print("R - List Required Items\nC - List Completed Items\nA - Add new item\nM - mark an item as completed\nQ - Quit")

    request = user_input()
    while request != 'Q':
        if request == 'R':
            print_required_items()
            request = user_input()








main()