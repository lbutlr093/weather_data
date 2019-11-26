## TODO: Description
import os
import re
import time
from bs4 import BeautifulSoup
import urllib.request as urllib2

## Set up the variables
site_url_pt_1 = "http://api.wunderground.com/history/airport/"
site_url_pt_2 = "/DailyHistory.html?"

# just any old leap year. All others will be calculated from this
leap_years_base = 1992

# the beginning and end years to get data from
start_year = input("Enter starting year (yyyy): ")
end_year = input("Enter ending year (yyyy): ")

# the specific airport we want weather data from
airport = input("Enter airport to find weather data near (e.g. MSP, ORD, etc...): ")

# empty list to have urls appended later
urls = []

# create a range of years to iterate over
years = list(range(int(start_year), int(end_year) + 1))

## Create strings for all URLs to be visited
for year in years:
	# if the year is a multiple of 4 from our leap year, we know it is also a leap year
	if abs(year - leap_years_base) % 4 == 0:
		for digit in list(range(1, 367)):
			url = site_url_pt_1 + str(airport) + str(year) + "/1/" + str(digit) + site_url_pt_2
			urls.append(url)
	
	# else, it is not a leap year
	else:
		for digit in list(range(1, 366)):
			url = site_url_pt_1 + str(airport) + str(year) + "/1/" + str(digit) + site_url_pt_2
			urls.append(url)

for url in urls:
	base_page = urllib2.urlopen(url)
	page_soup = BeautifulSoup(base_page, "html.parser")
	soup = str(page_soup)
	
	file_name = "weather_html_data/file_" + str(time.time()).replace(".", "") + ".txt"
	file = open(file_name, 'w')
	file.write(soup)
	time.sleep(2)					# Reduce the frequency of requests