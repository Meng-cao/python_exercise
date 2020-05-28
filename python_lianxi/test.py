import operator
intervals = [[6,15],[6,17],[8,13]]
intervals.sort(key = operator.itemgetter(0))
print(intervals)