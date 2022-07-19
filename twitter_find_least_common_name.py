# Find the most common name used in below list name a
from collections import Counter

a = [ "John", "Zeynal", "John", "Faraj", "Zeynal", "John", "Zeynal", "Zeynal", "Zeynal" ]
counter = Counter()
for item in a:
    counter [ item ] =counter[item] -1
print("The least used item is => {}".format(counter.most_common(1) [ 0 ] [ 0 ]))
