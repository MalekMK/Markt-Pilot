import pyppeteer
import csv
import time

async def get_data(brand, name):
    print("searching for name: {} and brand: {}".format(name, brand))
    browser = await pyppeteer.launch(headless=True)
    page = await browser.newPage()
    await page.goto("https://www.wollplatz.de/#sqr:(q[{}],{})".format(name, brand))
    time.sleep(3)
    try:
        result = await page.Jeval('.productlist-mainholder', 'e => e.innerText')
    except:
        result = 'not found'
    return result


def read_data(path):
    file_data = []
    print("reading data from {}".format(path))
    try:
        with open(str(path), 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                file_data.append(row)
            return file_data
    except:
        return None

async def main():
    data = []
    file_data = read_data("csv/data.csv")
    if (file_data == None):
        print("problem while reading file")
        exit

    if (len(file_data) > 0):
        for row in file_data:
            item = await get_data(row[0], row[1])
            data.append([row[0], row[1], item])

    if(len(data) > 0):
        print('saving results in csv/wollplatz.csv')
        with open('csv/wollplatz.csv', 'w') as csvfile:
            header_columns = ['Brand', 'Name', 'Result']
            writer = csv.DictWriter(csvfile, fieldnames=header_columns)
            writer.writeheader()
            for element in data:
                writer.writerow({
                    "Brand": element[0],
                    "Name": element[1],
                    "Result": element[2]
                })
