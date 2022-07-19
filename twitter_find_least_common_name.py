# Find the least common name used in below list name a
from collections import Counter
cnt = Counter()


a = ["John","Zeynal","John","Faraj","Zeynal","John"]

for i in a:
    cnt[i] = cnt[i] + 1
    print(cnt[i])
print("Most common used name is {}".format(cnt.most_common(1)[0][0]))
