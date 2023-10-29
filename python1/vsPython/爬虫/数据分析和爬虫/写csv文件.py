import csv

with open("test.csv",'w',encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['张飞',42])
    csv_writer.writerow(['赵云',42])
    csv_writer.writerow(['吕布',42])