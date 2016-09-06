def print_required_items():
    row_number = 0
    i = 0
    total_price=0
    there_are_required_items = False
    for status in items_status:
        if status == 'r':
            print("{}.  {:<17}$  {:<6.2f} ({})".format(row_number, items_names[i], items_prices[i], items_priorities[i]))
            row_number += 1
            total_price += items_prices[i]
            there_are_required_items = True
        i += 1
    if there_are_required_items:
        print("Total expected price for {} items: ${:.2f}".format(row_number,total_price))
        number_of_required_items = i
    else:
        print("There are no required itmes")

def get_user_input():
    valid_request_entries = ['R', 'C', 'A', 'M', 'Q']
    user_request = input(">>> ").upper()
    while user_request not in valid_request_entries:
        print("Not valid")
        user_request = input(">>> ").upper()
    return user_request

    # MAIN PROGRAM STARTS HERE
def main():
    # Loads .csv file
    import csv
    items_file = open("items.csv", "r")
    items_reader = csv.reader(items_file)
    items_names = []
    items_prices = []
    items_priorities = []
    items_status = []
    items = []
    for row in items_reader:
        items.append([row[0], float(row[1])])
        items_names.append(row[0])
        items_prices.append(float(row[1]))
        items_priorities.append(row[2])
        items_status.append(row[3])

    #Print menu and get user entry
    print("Shopping List v1 - Carlos Salgar")
    print("Menu\nR - List Required Items\nC - List Completed Items\nA - Add new item\nM - mark an item as completed\nQ - Quit")
    request = get_user_input()

    while request != 'Q':

        if request == 'R':

            print_required_items()

            # Print menu and start new user request
            print("Menu\nR - List Required Items\nC - List Completed Items\nA - Add new item\nM - mark an item as completed\nQ - Quit")
            request = get_user_input()

        elif request == 'C':

            # Print Completed Items
            row_number = 0
            i = 0
            total_price = 0
            there_are_completed_items = False
            for status in items_status:
                if status == 'c':
                    print("{}.  {}\t$  {:<6.2f} ({})".format(row_number, items_names[i], items_prices[i],
                                                             items_priorities[i]))
                    row_number += 1
                    total_price += items_prices[i]
                    there_are_completed_items = True
                i += 1
            if there_are_completed_items:
                print("Total expected price for {} items: ${:.2f}".format(row_number, total_price))
            else:
                print("There are no completed items")

            # Print Menu and start new user request
            print("Menu\nR - List Required Items\nC - List Completed Items\nA - Add new item\nM - mark an item as completed\nQ - Quit")
            request = get_user_input()

        elif request == 'A':

            # Enter name and validates
            entered_item_name = input("Name: ")
            while entered_item_name.strip() == "":
                print("Input can not be blank")
                entered_item_name = input("Name: ")

            # Enter price and validates
            price_is_number = False
            while not price_is_number:
                try:
                    entered_item_price = float(input("Price: $"))
                    price_is_number = True
                except ValueError:
                    print("Invalid Price. Must be number")
            while entered_item_price < 0:
                print("Price must be  >= zero")
                entered_item_price = float(input("Price: $"))

            # Enter priority and validates
            valid_priority_entries= ['1','2','3']
            entered_item_priority = input("Priority: ")
            while entered_item_priority not in valid_priority_entries:
                print("Invalid priority. Enter 1,2 or 3")
                entered_item_priority = input("Priority: ")

            # Add new item to list
            items_names.append(entered_item_name)
            items_prices.append(entered_item_price)
            items_priorities.append(entered_item_priority)
            items_status.append('r')

            # Print confirmation of item added
            print("{}, ${:.2f} (priority {}) added to shopping list".format(entered_item_name, entered_item_price, entered_item_priority))

            #Print menu and get new user request
            print("Menu\nR - List Required Items\nC - List Completed Items\nA - Add new item\nM - mark an item as completed\nQ - Quit")
            request = get_user_input()

        elif request == 'M':

            print_required_items()

            # Validates Input is integer
            valid_input = False
            while not valid_input:
                try:
                    item_to_mark_as_complete = int(input("Enter the number of an item to mark as completed: \n>>> "))
                    valid_input = True
                except ValueError:
                    print("Invalid item.  Must be an integer")

            # Get number of required items
            number_of_required_items = 0
            for status in items_status:
                if status == 'r':
                    number_of_required_items += 1

            # Validates input is one of  0,1,2,,,,(total required items - 1)
            while item_to_mark_as_complete not in range(0, number_of_required_items):
                print("Invalid item number")
                item_to_mark_as_complete = int(input("Enter the number of an item to mark as completed: \n>>> "))

            # Mark item as completed
            items_status[item_to_mark_as_complete] = 'c'

            # Print confirmation of item completed
            print("{} marked as completed".format(items_names[item_to_mark_as_complete]))

            # Print menu and ask for a new user request
            print("Menu\nR - List Required Items\nC - List Completed Items\nA - Add new item\nM - mark an item as completed\nQ - Quit")
            request = get_user_input()

    # TODO SAVING THE FNAL FILE IS NOT WORKING (FOLLOWING LINES)
    items_file.close()
    final_items_file = open("items.csv", 'w')
    total_number_of_items = len(items_names)
    for i in range(0,total_number_of_items):
        print(items_names[i],",",items_prices[i],",",items_priorities[i],",",items_status[i], file = final_items_file )
    final_items_file.close()








main()