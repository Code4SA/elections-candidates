from __future__ import division
import re
from collections import Counter
import sys

"""
Distribution of ID numbers
python ids.py <text file with ids>
"""

def extract_year(id):
    year2 = int(id[0:2])
    2009 - (year2 + 1900)
    if year2 < 10:
        return "0 - 9"
    if year2 < 20:
        return "10 - 19"
    elif year2 < 30:
        return "20 - 29"
    elif year2 < 40:
        return "30 - 39"
    elif year2 < 50:
        return "40 - 49"
    elif year2 < 60:
        return "50 - 59"
    elif year2 < 70:
        return "60 - 69"
    elif year2 < 80:
        return "70 - 79"
    elif year2 < 90:
        return "80 - 89"
    return "90 and over"

def extract_starsigns(id):
    month = int(id[2:4])
    day = int(id[4:6])
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"

def extract_gender(id):
    val = int(id[6])
    if val < 4:
        return "Woman"
    return "Man"

def histogram(hash, count):
    items = hash.items()
    sorted_items = sorted(items, key=lambda x: x[1])
    perc_items = [(key, val/count * 100) for key, val in sorted_items]
    for key, val in perc_items:
        print "%s: %.2f%%" % (key, val)

def print_output(title, hist, count):
    print ""
    print title
    print "=" * 20
    print ""
    histogram(hist, count)

reg = re.compile("\d{13}")
fp = open(sys.argv[1])
party = sys.argv[2]
text = fp.read()
ids = set(re.findall(reg, text))
count = len(ids)


years = Counter()
star_signs = Counter()
gender = Counter()

for id in ids:
    years[extract_year(id)] +=1
    star_signs[extract_starsigns(id)] +=1
    gender[extract_gender(id)] +=1

print "Party : %s" % party
print "Number of Candidates: %d" % count
print "=" * 20
print ""

print_output("Distribution by age", years, count)
print_output("Distribution by star sign", star_signs, count)
print_output("Distribution by gender", gender, count)

