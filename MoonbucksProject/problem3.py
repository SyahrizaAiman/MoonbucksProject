from problem1 import ranking
from problem2 import newRankingList
 
 
rankingList1 = ranking.values.tolist()
newRanking1=[['',0]  for i in range(5)]
for i in range(len(rankingList1)):
    newRanking1[i][0] = rankingList1[i][0]
    newRanking1[i][1] = 5-i
    newRankingList[i][1]=5-i
 
finalRanking=[['',0]  for i in range(5)]
for i in range(len(ranking)):
    countryName = newRanking1[i][0]
    point = newRanking1[i][1]
    for i in range(len(newRankingList)):
        if newRankingList[i][0]==countryName:
            point+=newRankingList[i][1]
            finalRanking[i][0] = countryName
            finalRanking[i][1] = point
 
print(finalRanking)
