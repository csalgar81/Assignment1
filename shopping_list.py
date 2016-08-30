def main():

    print("Shopping List v1 - Carlos Salgar")
    print("R - List Required Items\nC - List Completed Items\nA - Add new item\nM - mark an item as completed\nQ - Quit")
    load_items_file()

def load_items_file():
    import csv
    items_file = open("items.csv", "r")
    items_reader = csv.reader(items_file)
    items = []
    prices = []
    priorities = []
    items_status = []
    i = 0
    for row in items_reader:
        items.append(row[0])
        prices.append(row[1])
        priorities.append(row[2])
        items_status.append(row[3])

main()