import random
import time
import sys
import nltk
nltk.download('gutenberg')
from nltk.corpus import gutenberg
from nltk.util import ngrams
from nltk.probability import ConditionalFreqDist
from collections import defaultdict


def readFile(fileNum):
    texts = []
    for title in range(3, fileNum):  # 1 & 2 are n and m
        text = gutenberg.words(sys.argv[title]) 
        texts.extend(text)
        
    return texts

#texts = gutenberg.words('austen-emma.txt')

def reshapeText (texts, ngramValue):
    endingPunctuation = ['.','?','!']  # Each sentance will end with a ending punctution
    returnText = []
    line = []
    for word in texts:
        line.append(word.lower())  # transfer all words to lower case
        if word in endingPunctuation:
            if len(line) >= ngramValue: 
                line.append('%20e')
                returnText.extend(line)
            line = ['%20s']
    
    return returnText

def cleanNgram(nngramList):
    ngramArray = []
    for ngram in nngramList:
        if ( ('%20e' in ngram and ngram.index('%20e') != len(ngram) - 1) or ('%20s' in ngram and ngram.index('%20s') != 0)):
            continue
        ngramArray.append(ngram)
    return ngramArray

def endWordDictProcess(endWord_dict):
    ngramdict = {}
    for key,value in endWord_dict.items():
            endings = set(value)
            ngramdict[key]={}
            cnt = 0


            for end in endings:
                freuncy = value.count(end) / float(len(end)) #compute the count of each words for a gram
                ngramdict[key][end] = freuncy
                cnt += freuncy

            for keysub, valuesub in ngramdict[key].items():
                ngramdict[key][keysub] = valuesub / cnt  #normalization of the propability
    return ngramdict

def ngramLists(texts, n):
    res = []
    for i in range(len(texts)):
        res.append(tuple())
    for i, t in enumerate(texts):
        t = t.lower()
        for k in range(n):
            if(i >= k):
                res[i-k] = res[i-k] + (t,)
    for k in range(1, n):
        res.pop(len(texts) - k)
    return res

def generateRes(texts, ngramValue):

    textwithBE = reshapeText(texts, ngramValue) # find the head and tail for each sentance
    ngramArray = cleanNgram(ngramLists(textwithBE,ngramValue))  # ngram within sentance itself


    cfdist = ConditionalFreqDist()  # if we get a b c,  -> a b  with c last word
    endWord_dict = defaultdict(list)   # collection of { a : [b,c,d,e,f]}

    for ngram in ngramArray:
        text_outlast = tuple(ngram[:-1]) 
        endword = ngram[-1] 
        cfdist[text_outlast][endword] += 1
        endWord_dict[text_outlast].append(endword)

    #cover the endWord_dick to a dictionary with frequency
    ngramdict = endWordDictProcess(endWord_dict)
    
    #return ngramArray
    return ngramdict, cfdist, ngramArray
def beginGrams(ngramArray):
    beginG = []
    for ngram in ngramArray:
        if ngram[0] == '%20s':
            beginG.append(ngram)
    return beginG


def generateSentences(texts, ngramValue, numSentences):
    ngramdict, cfdist, ngramArray = generateRes(texts, ngramValue)
    
    begingrams = beginGrams(ngramArray)
    
    for sentidx in range(numSentences):
        startwords = random.choice(begingrams)
        beginpart = tuple(startwords[:-1])
        endwordSet = ngramdict[beginpart]
        
        pridictEnd = ''
        
        seed = random.uniform(0,1)   # get a prob between 0 - 1
        for word, freq in endwordSet.items():
            seed -= freq
            if seed <= 0:
                pridictEnd = word #find the predicted word based on the distribution
                break
        testprint = ' '.join(beginpart) + " " + pridictEnd

        while (pridictEnd != '%20e'):  # if sentense is not ended
            
            #shift out the first word,  for next round loop

            beginpart += tuple([pridictEnd])
            beginpartlist = list(beginpart)
            beginpartlist.pop(0)  

            
            beginpart = tuple(beginpartlist)

            #Predict until reaches end point
            for key,value in ngramdict.items():
                if(key == beginpart):
                    seed = random.uniform(0,1)
                    for word,freq in value.items():
                        seed -= freq
                        if seed <= 0:
                            pridictEnd = word
                            break
                            
            # if it meets ending, group as sentance
            if pridictEnd != '%20e':
                testprint = testprint + " " + pridictEnd
        print("New Sentence " + str(sentidx+1) + ": ", testprint[7:])

def getFileNames(fileNum):
	res = ""
	for file in range(3, fileNum):
		res += sys.argv[file] + " "
	return res

def main():
    start = time.time();
    
    # first input is ngram value
    ngramValue = int(sys.argv[1])
    # second input is number of sentences
    sentenceNum = int(sys.argv[2])
    # next, count how many files we have to read
    fileNum = len(sys.argv)
    
    # full text to use, save as []
    fullText = readFile(fileNum)
    
    # generate result
    generateSentences(fullText, ngramValue, sentenceNum)
    
    # count time
    returnTime = time.time() - start
    
    txtNames = getFileNames(fileNum)

    print('Time Spend is: ' + str(returnTime))

    with open("ngram-log.txt", "a+") as text_file:
        text_file.write("%s" % returnTime + " secs python ngram.py " + "%s %s %s" % (ngramValue, sentenceNum, txtNames) + "\n")

if __name__ == '__main__':
    main()