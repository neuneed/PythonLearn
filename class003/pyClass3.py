#coding:utf-8



# 贝叶斯推断及其互联网应用（三）：拼写检查



import re, collections   # 加载Python的正则语言模块（re）和collections模块，后面要用到
book = 'big.txt'

# 定义words()函数，用来取出文本库的每一个词
def words(text):
    return re.findall('[a-z]+', text.lower())


# 定义一个train()函数，用来建立一个"字典"结构。文本库的每一个词，都是这个"字典"的键；它们所对应的值，就是这个词在文本库的出现频率。
def train(features):
    model = collections.defaultdict(lambda: 1)   # 每一个词的默认出现频率为1
    for f in features:
        model[f] += 1
    return model


# 使用words()和train()函数，生成上一步的"词频字典"，放入变量NWORDS
NWORDS = train(words(open(book).read()))


# 定义edits1()函数，用来生成所有与输入参数word的"编辑距离"为1的词

#   1)splits：将word依次按照每一位分割成前后两半。比如，'abc'会被分割成 [('', 'abc'), ('a', 'bc'), ('ab', 'c'), ('abc', '')] 。
#   2）beletes：依次删除word的每一位后、所形成的所有新词。比如，'abc'对应的deletes就是 ['bc', 'ac', 'ab'] 。
#   3)transposes：依次交换word的邻近两位，所形成的所有新词。比如，'abc'对应的transposes就是 ['bac', 'acb'] 。
# 　4)replaces：将word的每一位依次替换成其他25个字母，所形成的所有新词。比如，'abc'对应的replaces就是 ['abc', 'bbc', 'cbc', ... , 'abx', ' aby', 'abz' ] ，一共包含78个词（26 × 3）。
# 　5）inserts：在word的邻近两位之间依次插入一个字母，所形成的所有新词。比如，'abc' 对应的inserts就是['aabc', 'babc', 'cabc', ..., 'abcx', 'abcy', 'abcz']，一共包含104个词（26 × 4）。

# edit1()返回deletes、transposes、replaces、inserts的合集，这就是与word"编辑距离"等于1的所有词。对于一个n位的词，会返回54n+25个词。
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


# 定义edit2()函数，用来生成所有与word的"编辑距离"为2的词语
def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)


# 将edit2()改为known_edits2()函数，将返回的词限定为在文本库中出现过的词
def known(words): return set(w for w in words if w in NWORDS)


# 用来从所有备选的词中，选出用户最可能想要拼写的词
def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

print(correct('coop'))
