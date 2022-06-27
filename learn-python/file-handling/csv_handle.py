import csv

reader = csv.DictReader(open("lob_top_brands.csv"))
for x in reader:
    print(x['lob'])