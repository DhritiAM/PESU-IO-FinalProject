
import bs4 as bs
import lxml
import urllib.request
import csv

sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/assignment.html").read()
srccode = bs.BeautifulSoup(sauce,'lxml')

# List of all the hyperlinks
x = []
for i in srccode.find_all('a'):
    x.append(i.get('href'))

base = "https://karki23.github.io/Weather-Data"
links = []
for i in srccode.find_all('a'):
    links.append(base+'/'+i.get('href'))

#Data extraction using the links
j = 0
for link in links:
    sauce1 = urllib.request.urlopen(link).read()
    srccode1 = bs.BeautifulSoup(sauce1,'lxml')
    table = srccode1.find('table')
    output_rows = []
    i = 0
    for table_row in table.find_all('tr'):
        if i==0:
            columns = table_row.find_all('th')
            i = 1
        else:
            columns = table_row.find_all('td')
        output_row = []
        for column in columns:
            output_row.append(column.text)
        output_rows.append(output_row)
    #Writing into the csv file   
    f_name = x[j].strip(".html")+'.csv'
    j = j+1
    with open(f_name, 'wt+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output_rows)





