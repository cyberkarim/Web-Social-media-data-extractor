import requests
from bs4 import BeautifulSoup
import csv

def bubble_sort(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(tab[j][1]) < int(tab[j+1][1]):
                tab[j], tab[j+1] = tab[j+1], tab[j]

def save_data_csv(data):
    file_csv = open('Results/corona_country.csv', 'w', newline='')
    writer = csv.writer(file_csv)
    writer.writerow( [ "N°", "Country", "Total Cases", "New Cases", "Total deaths", "New deaths", "Total recovered", "Active cases" ] )
    for i in range(0, len(data), 1):
        writer.writerow( [ (i+1), data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6] ] )
    file_csv.close()

def extract_data(data):
    URL = "https://www.worldometers.info/coronavirus/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="main_table_countries_today")
    content = results.find_all('td')

    num = []
    countries = []
    total_cases = []
    new_cases = []
    total_deaths = []
    new_deaths = []
    total_recovered = []
    active_cases = []

    i = 1
    for entry in content:
        if (i%19 == 1):
            num.append(entry.text.strip())
        if (i%19 == 2):
            countries.append(entry.text.strip())
        if (i%19 == 3):
            total_cases.append(entry.text.strip())
        if (i%19 == 4):
            new_cases.append(entry.text.strip())
        if (i%19 == 5):
            total_deaths.append(entry.text.strip())
        if (i%19 == 6):
            new_deaths.append(entry.text.strip())
        if (i%19 == 7):
            total_recovered.append(entry.text.strip())
        i += 1

    for i in range(0, len(countries), 1):
        if(total_cases[i].replace(',', '') != "N/A" and total_deaths[i].replace(',', '') != "N/A" and total_deaths[i].replace(',', '') != "" and total_recovered[i].replace(',', '') != "N/A" and total_recovered[i].replace(',', '') != ""):
            active_cases.append( str(int(total_cases[i].replace(',', ''))-int(total_deaths[i].replace(',', ''))-int(total_recovered[i].replace(',', ''))))
        elif(total_cases[i].replace(',', '') == "N/A" or total_deaths[i].replace(',', '') == "N/A" or total_recovered[i].replace(',', '') == "N/A"):
            active_cases.append("N/A")
        elif(total_deaths[i].replace(',', '') == "" and total_recovered[i].replace(',', '') == ""):
            active_cases.append( str(int(total_cases[i].replace(',', ''))))
        elif(total_deaths[i].replace(',', '') == ""):
            active_cases.append( str(int(total_cases[i].replace(',', ''))-int(total_recovered[i].replace(',', ''))))
        elif(total_recovered[i].replace(',', '') == ""):
            active_cases.append( str(int(total_cases[i].replace(',', ''))-int(total_deaths[i].replace(',', ''))))
        else:
            active_cases.append("")

    for i in range(0, len(countries), 1):
        if (num[i] != ""):
            data.append([ countries[i].replace(',', ''), total_cases[i].replace(',', ''), new_cases[i].replace(',', ''), total_deaths[i].replace(',', ''), new_deaths[i].replace(',', ''), total_recovered[i].replace(',', ''), active_cases[i] ])

def main():
    data = []
    extract_data(data)
    bubble_sort(data)
    save_data_csv(data)
