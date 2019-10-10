import json
from collections import Counter
from string import punctuation
import operator


def addDataFromDict(data, curDict, keyPreffix=""):
    for key, value in curDict.items():
        if type(value) is dict:
            addDataFromDict(data, value, keyPreffix + key + '.');
        else:
            curKey = keyPreffix + key
            data[curKey].append(value) if curKey in data else data.update({curKey: [value]});


f = open("hw_3_twitter.json")
data = {}
tweets = []
ans1 = 0
for line in f:
    lineData = json.loads(line)
    tweets.append(lineData)
    addDataFromDict(data, lineData);
    ans1 += 1
print("Всего твитов: " + str(ans1))
ans2 = 0
for item in tweets:
    data1 = list(item.keys())
    if "delete" in data1:
        ans2 += 1
ans2 = ans2 / ans1 * 100
print("Процент удаленных твитов: " + str(ans2))
print('\n')

langs = data["lang"]
langTop = Counter()
langTop.update(langs)
top = langTop.most_common(10)
print("Топ по используемым языкам: ")
i = 0
for item in top:
    print(i, end=" ")
    print(item[0] + " " + str(item[1]))
    i += 1
print('\n')

userIds = data["user.id"]
ans3 = 0
users2 = [item for item, count in Counter(userIds).items() if count > 1]
ans3 = len(users2)
print("Пользователей с числом твитов > 1 :" + str(ans3))

hashtags = []
hashtagsRaw = data["entities.hashtags"]
for hashtagRaw in hashtagsRaw:
    for hashDict in hashtagRaw:
        hashtags.append(hashDict["text"])
hashtagsCounter = Counter()
hashtagsCounter.update(hashtags)
hashTop = hashtagsCounter.most_common(20)
i = 1
print("Самые популярные хэштеги: ")
for hashtag in hashTop:
    print(i, end=" ")
    print(hashtag[0] + " " + str(hashtag[1]))
    i += 1
print('\n')

commonStr = ""
for text in data["text"]:
    text.translate(punctuation)
    text.lower()
    commonStr += text + " "
words = commonStr.split(" ")
lsWord = {}
for key in words:
    key = key.lower()
    if key in lsWord:
        value = lsWord[key]
        lsWord[key] = value + 1
    else:
        lsWord[key] = 1
sortedDict = sorted(lsWord.items(), key=operator.itemgetter(1), reverse=True)
print("Словарь частотностей")
for item in sortedDict:
    print(item[0] + " " + str(item[1]))
print('\n')

userFollNumber = data["user.followers_count"]
userDict = {}
i = 0
for item in userFollNumber:
    userDict[data["user.name"][i]] = item
    i += 1
sortedTopUsers = sorted(userDict.items(), key=operator.itemgetter(1))
print("Топ авторов по подписчикам: ")
i = 1
for item in sortedTopUsers:
    print(i, end=" ")
    print(item[0])
    i += 1
print('\n')
