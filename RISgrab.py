# -*- coding: utf-8 -*-
# Hallo und Wilkommen zum Leverkusener Tagesordnungs-Tool
# Die url von RIS bei "urlStr" eingeben

urlStr = "http://ris.leverkusen.de/si0057.asp?__ksinr=1427"
savepath = "C:/Users/kenet/ris1.csv"

seperator = "smc-card"
end = "</td>"
memory = ""
each = 0

from urllib import request
wert = request.urlopen(urlStr)
inhalt = wert.read()
inhalt_text = inhalt.decode("UTF-8")
memory = inhalt_text
cache = inhalt_text
count = inhalt_text.count("<td")

import csv
with open(savepath, mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    while each < count:
        lcharnr = cache.find(seperator)
        rcharnr = cache.find(end)
        memory = memory[(lcharnr+30):(rcharnr-len(memory)-6)]
        cache = cache[(rcharnr+5):]
        each += 1
       # if each == 0:
        if len(memory) <= 0:
            memory = cache
            continue

        writer.writerow([each,memory]) 
        memory = cache

file.close()