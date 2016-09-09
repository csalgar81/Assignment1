# CARLOS SALGAR, 9 September 2016
# https://github.com/csalgar81/Assignment1

def main():

    valid_request_entries = ['R', 'C', 'A', 'M', 'Q']
    valid_priority_entries = ['1', '2', '3']

    """
    function get_user_choice_from_menu()
        get user_request
        while user_request not in valid_request_entries
            print 'not valid'
            get user_request
        return user_request
    """
    def get_user_choice_from_menu():
        user_request = input(">>> ").upper()
        while user_request not in valid_request_entries:
            print("Not valid")
            user_request = input(">>> ").upper()
        return user_request

    def print_menu():
        print("Menu\nR - List Required Items\nC - List Completed Items\nA - Add new item\nM - "
              "mark an item as completed\nQ - Quit")

    """
    function print_requied_items
        row_number = 0
        i = 0
        total_price = 0
        there_are_required_items = False
        for item_status in items_status_list
            if item_status = 'r'
                print row_number, item_name, item_price, item_priority
                row_number +=1
                total_price += item_price
                there_are_required_items = True
            i += 1
        if there_are_required_items = True
            print total_price
        else
            print "There are no required items"
    """
    def print_required_items():
        row_number = 0
        i = 0
        total_price = 0
        there_are_required_items = False
        for status in items_status:
            if status == 'r':
                print("{}.  {:<17}$  {:<6.2f} ({})".format(row_number, items_names[i], items_prices[i],
                                                           items_priorities[i]))
                row_number += 1
                total_price += items_prices[i]
                there_are_required_items = True
            i += 1
        if there_are_required_items:
            print("Total expected price for {} items: ${:.2f}".format(row_number, total_price))
            number_of_required_items = i
        else:
            print("There are no required itmes")

    def print_completed_items():
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

    def get_new_item_name():
        entered_item_name = input("Name: ")
        while entered_item_name.strip() == "":
            print("Input can not be blank")
            entered_item_name = input("Name: ")
        return entered_item_name

    def get_new_item_price():
        price_is_valid = False
        while not price_is_valid:
            try:
                entered_item_price = float(input("Price: $"))
                if entered_item_price >= 0:
                    price_is_valid = True
                else:
                    print("Price must be >=0")
            except ValueError:
                print("Invalid input. Enter a valid number")
        return entered_item_price

    def get_new_item_priority():
        entered_item_priority = input("Priority: ")
        while entered_item_priority not in valid_priority_entries:
            print("Invalid priority. Enter 1,2 or 3")
            entered_item_priority = input("Priority: ")
        return entered_item_priority

    def get_number_of_required_items():
        number_of_required_items = 0
        for status in items_status:
            if status == 'r':
                number_of_required_items += 1
        return number_of_required_items

    def get_item_to_mark_as_completed():
        total_required_items= get_number_of_required_items()
        valid_input = False
        while not valid_input:
            try:
                item_to_mark_as_completed = int(input("Enter the number of an item to mark as completed: \n>>> "))
                if item_to_mark_as_completed in range (0,total_required_items):
                    valid_input = True
                else:
                    print ("Invalid item number")
            except ValueError:
                print("Invalid item.  Must be an integer")
        return item_to_mark_as_completed

    def save_items_to_csv_file():
        items_file.close()
        final_items_file = open("items.csv", 'w')
        total_number_of_items = len(items_names)
        for i in range(0, total_number_of_items):
            print(items_names[i], ",", items_prices[i], ",", items_priorities[i], ",", items_status[i],
                  file=final_items_file)
        final_items_file.close()


    # MAIN PROGRAM STARTS HERE

    # Loads .csv file
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

    print_menu()

    next_request = get_user_choice_from_menu()

    while next_request != 'Q':

        if next_request == 'R':

            print_required_items()
            print_menu()
            next_request = get_user_choice_from_menu()

        elif next_request == 'C':

            print_completed_items()
            print_menu()
            next_request = get_user_choice_from_menu()

        elif next_request == 'A':

            # Ask the user for new item details
            new_item_name = get_new_item_name()
            new_item_price = get_new_item_price()
            new_item_priority = get_new_item_priority()

            # Add new item details to lists in memory
            items_names.append(new_item_name)
            items_prices.append(new_item_price)
            items_priorities.append(new_item_priority)
            items_status.append('r')

            # Print confirmation of item added
            print("{}, ${:.2f} (priority {}) added to shopping list".format(new_item_name, new_item_price,
                                                                            new_item_priority))

            print_menu()
            next_request = get_user_choice_from_menu()

        elif next_request == 'M':

            print_required_items()

            item_to_complete = get_item_to_mark_as_completed()

            # Mark item as completed
            items_status[item_to_complete] = 'c'

            # Print confirmation of item completed
            print("{} marked as completed".format(items_names[item_to_complete]))

            print_menu()

            next_request = get_user_choice_from_menu()

    # If user selects 'Q', save all items to csv.file
    save_items_to_csv_file()
main()
