import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pygtrie as trie

fileMy = open('MoonbucksProject\\Article\\Malaysia.txt', 'r', encoding='utf-8')
My = fileMy.read()
fileMy.close()

fileId = open('MoonbucksProject\\Article\\Indonesia.txt', 'r', encoding='utf-8')
Id = fileId.read()
fileId.close()

filePh = open('MoonbucksProject\\Article\\Philippine.txt', 'r', encoding='utf-8')
Ph = filePh.read()
filePh.close()

fileSg = open('MoonbucksProject\\Article\\Singapore.txt', 'r', encoding='utf-8')
Sg = fileSg.read()
fileSg.close()

fileTh = open('MoonbucksProject\\Article\\Thailand.txt', 'r', encoding='utf-8')
Th = fileTh.read()
fileTh.close()

list_ct = [My,Id,Ph,Sg,Th]
n_ct = len(list_ct)
n_articles = 5
articles = [txt for txt in list_ct]

i = 0
for country in list_ct:
    x = country.split("SplitText")
    articles[i] = x
    i += 1
file_ptWord = open('MoonbucksProject\PositiveWord.txt','r',encoding='utf-8')
positiveWord = file_ptWord.read().lower().split(", ")
file_ptWord.close()
file_ntWord = open('MoonbucksProject\\NegativeWord.txt','r',encoding='utf-8')
negativeWord = file_ntWord.read().lower().split(",    ")
file_ntWord.close()
file_stopWord = open('MoonbucksProject\StopWord.txt','r',encoding='utf-8')
stopWord = file_stopWord.read().lower().split()
file_stopWord.close()

dictionaryPositive = trie.StringTrie()
dictionaryNegative = trie.StringTrie()
dictionaryStop = trie.StringTrie()

for word in positiveWord:
    dictionaryPositive[word] = None

for word in negativeWord:
    dictionaryNegative[word] = None

for word in stopWord:
    dictionaryStop[word] = None

countryName = {'Country':['Indonesia', 'Malaysia', 'Philiphines','Singapore', 'Thailand']}
data = pd.DataFrame(countryName)

total_good_word = [0, 0, 0, 0, 0]
total_bad_word = [0, 0, 0, 0, 0]
total_stop_word = [0, 0, 0, 0, 0]
article_good_word = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
article_bad_word = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
article_stop_word = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
word_counter = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
# for analysis

for i in range(len(list_ct)):
    for j in range(n_articles):
        word_counter[i][j] = len(articles[i][j])
        for words in articles[i][j].split():
            word_counter
            if dictionaryPositive.__contains__(words):
                total_good_word[i] += 1
                article_good_word[i][j] += 1
            elif dictionaryNegative.__contains__(words):
                total_bad_word[i] += 1
                article_bad_word[i][j] += 1
            elif dictionaryStop.__contains__(words):
                total_stop_word[i] += 1
                article_stop_word[i][j] += 1
            else:
                continue

data['Good'] = total_good_word
data['Bad'] = total_bad_word
data['Stop'] = total_stop_word
data['article_good_word'] = article_good_word
data['article_bad_word'] = article_bad_word
data['article_stop_word'] = article_stop_word
print("--------------------------------------------------------------------------------------------------------")
print(data)
print("--------------------------------------------------------------------------------------------------------")
print("\n")

# Total GOOD or BAD Word count visualization
countryNames = ['Indonesia', 'Malaysia', 'Philiphines','Singapore', 'Thailand']

#GOOD or BAD Word Count per article visualization

#GoodWordsPieChart
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

def func(pct, allvals):
    absolute = int(round(pct/100.*np.sum(allvals)))
    return "({:.1f}%\n({:d})".format(pct, absolute)

wedges, texts, autotexts = ax.pie(data['Good'], autopct=lambda pct: func(pct, data['Good']), textprops = dict(color="w"))

ax.legend(wedges, countryNames,
          title="Country",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Good words by country")

plt.show()

#BadWordsPieChart
fig, ax = plt.subplots(figsize = (6, 3), subplot_kw = dict(aspect="equal"))

def func(pct, allvals):
    absolute = int(round(pct/100.*np.sum(allvals)))
    return "({:.1f}%\n({:d})".format(pct, absolute)

wedges, texts, autotexts = ax.pie(data['Bad'], autopct=lambda pct: func(pct, data['Bad']), textprops = dict(color="w"))

ax.legend(wedges, countryNames,
          title="Country",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Bad words by country")

plt.show()

fig, ax = plt.subplots()

p1 = ax.bar(countryNames, data['Good'] ,color='g', label = 'good')
p2 = ax.bar(countryNames, data['Bad'], bottom=data['Good'], color='y', label= 'bad')
p3 = ax.bar(countryNames, data['Stop'],bottom=data['Good']+data['Bad'] ,color='orange' ,label='stop')

ax.axhline(0, color='grey', linewidth=0.8)
ax.set_ylabel('Words')
ax.set_title('Words over country')
ax.legend()

# Label with label_type 'center' instead of the default 'edge'
ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p3, label_type='center')

plt.show()

# sorting by ranking
data['ranking'] = data["Good"] / data['Bad']
ranking = data.sort_values(by = 'ranking', ascending=False); 
print((ranking))