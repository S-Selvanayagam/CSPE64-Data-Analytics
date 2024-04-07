import csv

basket_dict = {}

csv_file = './DataSet/small1.csv'  

with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        basket_number, item = row
        if basket_number in basket_dict:
            basket_dict[basket_number].append(item)
        else:
            basket_dict[basket_number] = [item]

for basket_number, items in sorted(basket_dict.items(), key=lambda x: int(x[0])):
    print(f"{', '.join(items)}")
