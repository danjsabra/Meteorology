import csv

with open('DesMoinesWeatherData.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    gdddata = []
    for row in csv_reader:
        dailymax = row[4]
        dailymin = row[5]
        date = row[2]
        dailyavg = (int(dailymax) + int(dailymin)) / 2
        
        gdddata.append([date, min(36, max(0, dailyavg - 50))])



filename = 'DesMoinesGDD.csv'
filepath = './' + filename

headers = ['Date', 'Degrees Above 50']

with open(filepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)  
    for row in gdddata:
        writer.writerow(row)



