def main():

    def print_required_items():
        row_number = 0
        i = 0
        total_price=0
        there_are_required_items = False
        for status in items_status:
            if status == 'r':
                print("{}.  {}\t$  {:<6.2f} ({})".format(row_number, items_names[i], items_prices[i], items_priorities[i]))
                row_number += 1
                total_price += items_prices[i]
                there_are_required_items = True
            i += 1
        if there_are_required_items:
            print("Total expected price for {} items: ${:.2f}".format(row_number+1,total_price))
        else:
            print("There are no required itmes")

    def print_completed_items():
        row_number = 0
        i=0
        total_price = 0
        there_are_completed_items = False
        for status in items_status:
            if status == 'c':
                print("{}.  {}\t$  {:<6.2f} ({})".format(row_number, items_names[i], items_prices[i], items_priorities[i]))
                row_number += 1
                total_price += items_prices[i]
                there_are_completed_items = True
            i += 1
        if there_are_completed_items:
            print("Total expected price for {} items: ${:.2f}".format(row_number + 1, total_price))
        else:
            print("There are no completed items")

    def user_input():
        valid_request_entries = ['R', 'C', 'A', 'M', 'Q']
        user_request = input(">>> ").upper()
        while user_request not in valid_request_entries:
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
        elif request == 'C':
            print_completed_items()
            request = user_input()
        elif request == 'A':
            entered_item_name = input("Name: ")
            while entered_item_name.strip() == "":#Enter name and validates
                print("Input can not be blank")
                entered_item_name = input("Name: ")
            valid_price = False #Enter price and validates
            while valid_price == False:
                try:
                    entered_item_price = float(input("Price: $"))
                    valid_price = True
                except ValueError:
                    print("Invalid Price. Must be number")
            #TODO Add price >= 0 validation
            valid_priority_entries= ['1','2','3']#Enter priority and validates
            entered_item_priority = input("Priority: ")
            while entered_item_priority not in valid_priority_entries:
                print("Invalid priority. Enter 1,2 or 3")
                entered_item_priority = input("Priority: ")
            #TODO Print added item with formsat: Watch, $50.00 (priority 2) added to shopping list
            items_names.append(entered_item_name)
            items_prices.append(entered_item_price)
            items_priorities.append(entered_item_priority)
            items_status.append('r')
            request = user_input()




main()