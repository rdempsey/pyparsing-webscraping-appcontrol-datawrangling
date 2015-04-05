#!/usr/bin/env python

import csv

url_file = "/Users/robertdempsey/Dev/lp-scraper/lp/data/start_urls.csv"

base_url = "BASE_URL_HERE"
pages = {'a':17, 'b':49, 'c':38, 'd':26, 'e':11, 'f':22, 'g':30, 'h':36, 'i':3, 'j':12, 'k':26, \
         'l':27, 'm':50, 'n':11, 'o':9, 'p':26, 'q':1, 'r':30, 's':56, 't':17, 'u':2, 'v':8, 'w':29,  \
         'x':1, 'y':4, 'z':4}
final_urls = []


with open(url_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for key,value in pages.items():
      for i in range(1,value+1):
        url = base_url + key + "/" + str(i) + ".html"
        writer.writerow([url])