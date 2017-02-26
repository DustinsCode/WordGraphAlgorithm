import networkx as nx
import matplotlib.pyplot as plt

#ignore warnings
import warnings
warnings.filterwarnings('ignore')


words = ['cats', 'cast', 'past', 'last', 'fast', 'rats', 'arts', 'dart', 'part', 'prat', 'tart', 'tarp']
nx.draw(word_graph(words), with_labels=True, node_color="white")
plt.show()


def word_graph(wordList):
    wordGraph = {}
    for word in wordList:
        edgeList = []
        for word2 in wordList:
            #prevents from trying to connect the same word
            if(word2 != word):
                if(countSameChars(word, word2)):
                    edgeList.append(word2)
        wordGraph[word] = edgeList
    return nx.Graph(wordGraph)
                     
                
                
def countSameChars(word1, word2):
    numSameChars = 0
    numSameIndex = 0
    for num in range(len(word1)):
        if(word1[num] == word2[num]):
            numSameIndex += 1
        if(word1[num] in word2):
            numSameChars += 1
    if(numSameIndex == 3):
        return True
    elif(numSameIndex == 2 and numSameChars == 4):
        return True
    else:
        return False
                