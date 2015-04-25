import string
from operator import itemgetter

#go through the list, and see if there are any matching three sequences
def main():

    #this goes through the entire list and finds all of the words that repeat, and the position where they can be found
    def findRepeatingSequencesOfThree(message):
        newString = []
        #print len(message)
        for i in range(len(message)-3):
            for x in range(i+3,len(message)-3,1):
                newWord =[]
                if message[i] == message[x] and message[i+1] == message[x+1] and message[i+2] == message[x+2]:
                    #print "True!"
                    newWord.append(message[i:i+3])
                    join = "".join(newWord)
                    newString.append(join)
        m = list(set(newString))
        return m


    #this finds which out of all the repetitions appears most frequently
    def findMostFrequent(listOfRepetitions,message):
        rating = [0]*len(listOfRepetitions)
        for i in range(len(listOfRepetitions)):
            for j in range(len(message)):
                if listOfRepetitions[i] == message[j:j+3]:
                    rating[i] += 1
        zippem = zip(rating,listOfRepetitions)
        sortem = sorted(zippem, reverse=True)
        (x,y) = zip(*sortem)
        return y

    #this finds the spacing in between the most common element from the list of repetitions in the message
    #and gives their positions in the message
    def findSpacing(listOfRepetitions, message):
        mostCommon = listOfRepetitions[0]
        listPosition = [0]*len(message)
        finalList = []
        for i in range(len(message)):
            if mostCommon == message[i:i+3]:
                listPosition[i] += 1
        for p in range(len(listPosition)):
            if listPosition[p] != 0:
                finalList.append(p)
        return finalList

    #this found the common difference between the list of position values of the repeating sequences,
    #sorting them so the most frequent lengths appeared first
    def findCommonDifference(listOfPositionValues):
        newList = []
        keepTrack = {}
        temp = []
        listOfDictionary = []
        for i in range(len(listOfPositionValues)-1):
            x = listOfPositionValues[i+1] - listOfPositionValues[i]
            newList.append(x)
        byMostCommon = sorted(newList)
        for b in range(len(newList)):
            listElement = newList[b]
            if keepTrack.has_key(listElement):
                keepTrack[listElement] += 1
            else:
                keepTrack[listElement] = 0
        listOfDictionary = dict.items(keepTrack)
        sort = sorted(listOfDictionary,key=itemgetter(1), reverse=True)
        return sort

    #this makes a series of lists from the message with each new list starting from the keyValue's distance
    def makeSeriesOfLists(message, keyValue):
        dictOfLists = {}
        listDict = []
        finalListOfLists = []
        for i in range(keyValue):
            partIOfKey = i
            for j in range(i,len(message),keyValue):
                if dictOfLists.has_key(partIOfKey):
                    dictOfLists[partIOfKey].append(message[j])
                else:
                    dictOfLists[partIOfKey] = [message[j]]
        listDict = dict.items(dictOfLists)
        for p in range(len(listDict)):
            x,y = listDict[p]
            finalListOfLists.append(y)
        return finalListOfLists

    #this is just a basic frequency finding function that gives me
    def frequencyFinder(message):
        counts = [0]*256
        for i in range(len(message)):
            charnum = message[i]
            #print charnum
            #print ord(charnum)
            k = ord(charnum)
            counts[k] += 1
            #print counts[k]
        for h in range(len(counts)):
            counts[h] = (counts[h]/(float(len(message))))
        newlist = []
        for p in range(256):
            newlist.append(p)
        zipped = zip(counts, newlist)
        sortem = sorted(zipped, reverse=True)
        return sortem

    #this finds the frequency of each list from the grand list of lists from the original message
    def findFrequencyOfEachSubList(listOfLists):
        newList = []
        for i in range(len(listOfLists)):
            j = frequencyFinder(listOfLists[i])
            newList.append(j)
        return newList

    def cracker(engFreq, encFreq, message):
        newmessage = ['_'] * len(message)
        for i in range(50):
            (a,b) = engFreq[i]
            (x,y) = encFreq[i]
            for o in range(len(message)):
                if message[o] == chr(y):
                    newmessage[o] = chr(b)
        newmessage = "".join(newmessage)
        return newmessage

    def switchFrequencies(englishFreq, encryptedFreq, listOfLists):
        newList = []
        for i in range(len(listOfLists)):
            h = cracker(englishFreq,encryptedFreq,listOfLists[i])
            newList.append(h)
        flattened = [val for sublist in newList for val in sublist]
        join = "".join(flattened)
        return join

    def switchThenCaesarForMultipleLists(englishFreq,listOfLists):
        newList = []
        for i in range(len(listOfLists)):
            encFrequency = frequencyFinder(listOfLists[i])
            a = switchThenCaesar(englishFreq,encFrequency,listOfLists[i])
            join = "".join(a)
            newList.append(join)
        return newList

    def switchThenCaesar(englishFreq, encFreq, message):
        j = switchFrequencies(englishFreq,encFreq,message)
        m = message
        keepTrack = {}
        newList = []
        finalListOfPossibleKeys = []
        listToReturn = []
        for i in range(len(m)):
            a = ord(j[i])
            b = ord(m[i])
            c = a - b
            newList.append(c)
        for x in range(len(newList)):
            listElement = newList[x]
            if keepTrack.has_key(listElement):
                keepTrack[listElement] += 1
            else:
                keepTrack[listElement] = 1
        listDict = dict.items(keepTrack)
        listDict = sorted(listDict, key = itemgetter(1), reverse=True)
        for p in range(len(listDict)):
            x,y = listDict[p]
            finalListOfPossibleKeys.append(x)
        key = finalListOfPossibleKeys[0]
        print key
        h = decode(message, key)
        listToReturn.append(h)
        return listToReturn

    #this takes the list of lists of lists, and puts the lists of lists into a list so you get a list of
    # lists... by god... there's got to be a better way of explaining this function

    def reorderListsToPositions(listOfStrings):
        newList = []
        p = [list(x) for x in zip(*listOfStrings)]
        result = sum(p, [])
        joined = "".join(result)
        return joined

    #this was to test that it worked
    def encode(message,key):
        newmessage =[]
        for i in range(len(message)):
            t = ord(message[i])
            j = (t-key)%256
            newmessage.append(chr(j))
        join = "".join(newmessage)
        return join

    #this decrypts teh given message
    def decode(message,key):
        newMessage = []
        for i in range(len(message)):
            x = ord(message[i])
            l = (x+key)%256
            newMessage.append(chr(l))
        join = "".join(newMessage)
        return join

    filename = "project-2B-sberger.ciphertext"
    f = open(filename, "rb")
    ciphertext = f.read()

    #this is the list of common english values by frequency
    z = [(0.16045412180666435, 32), (0.098016753478579938, 101), (0.068166380165811474, 116), (0.06124023994267111, 111),
         (0.059313862763936222, 97), (0.054000743896957346, 114), (0.051075419375499941, 115), (0.049562781025744865, 104),
         (0.048462014582103675, 105), (0.044992984678307646, 110), (0.034849418309917814, 99), (0.030033762581983047, 117),
         (0.021438736926154583, 108), (0.019672197066633351, 112), (0.018968079927276175, 100), (0.018624278901043036, 119),
         (0.017211879948243154, 121), (0.016837202889996596, 32), (0.014909246007298232, 102), (0.014526383210331839, 109),
         (0.014473104103927287, 103), (0.01243686569500512, 46), (0.0097749209070947373, 47), (0.0083030676414876207, 106),
         (0.0077020620881101424, 107), (0.0073301136094368639, 120), (0.0053427024139312655, 44), (0.0030774069303048973, 73),
         (0.0024402117952186668, 118), (0.0021185266244742101, 73), (0.0017755872549484227, 98), (0.0017438495662276527, 63),
         (0.001466108887558108, 77), (0.0012475353027933474, 120), (0.0012438014570614921, 59), (0.0012139306912066496, 83),
         (0.0011672576195584585, 122), (0.0009932029646735111, 72), (0.00096017279089171412, 66), (0.00091278167198739681, 67),
         (0.0008709913216808625, 71), (0.0008653905530830795, 33), (0.00080550541192216942, 87), (0.0007885594966775953, 78),
         (0.00071876530338214624, 113), (0.00071172844027211121, 68), (0.00069463891557631195, 106), (0.00061062738660956758, 70),
         (0.00059885141160910082, 82), (0.00058506490429148126, 122), (0.00056610845672975434, 69), (0.0005355196436187858, 86),
         (0.00050823384788599706, 79), (0.0004780758631287042, 89), (0.00038645303324702404, 71), (0.00027630458415729258, 76),
         (0.00023192926372870451, 58), (0.00018195317470233352, 75), (0.00017908098567782942, 48), (0.0001605553664697781, 40),
         (0.00015998092866487728, 41), (0.00011273341921178516, 49), (0.00010698904116277701, 88), (9.3202533845157418e-05, 74),
         (8.6740108540023242e-05, 195), (6.7065613722170288e-05, 85), (6.1752064026837733e-05, 42), (5.1268574087397837e-05, 56),
         (4.8683603965344169e-05, 169), (4.6960290550641717e-05, 50), (3.8200114025904272e-05, 53), (3.446626829404897e-05, 95),
         (2.6998576830338358e-05, 51), (2.6567748476662747e-05, 0), (2.599331067176193e-05, 167), (2.1541417683780604e-05, 52),
         (2.0536151525204176e-05, 55), (1.8669228659276525e-05, 54), (1.8238400305600913e-05, 90), (1.7663962500700096e-05, 57),
         (1.536621128109683e-05, 47), (1.3642897866394384e-05, 81), (7.8985198173862225e-06, 38), (4.7391118904317333e-06, 93),
         (4.7391118904317333e-06, 91), (3.8774551830805091e-06, 168), (2.8721890245040805e-06, 60), (2.7285795732788766e-06, 62),
         (2.2977512196032645e-06, 170), (2.2977512196032645e-06, 16), (2.1541417683780606e-06, 162), (1.2924850610268364e-06, 175),
         (1.1488756098016323e-06, 160), (1.0052661585764281e-06, 61), (1.0052661585764281e-06, 36), (8.6165670735122424e-07, 64),
         (7.1804725612602013e-07, 11), (7.1804725612602013e-07, 8), (7.1804725612602013e-07, 4), (7.1804725612602013e-07, 1),
         (5.7443780490081613e-07, 29), (5.7443780490081613e-07, 15), (4.3082835367561212e-07, 220), (4.3082835367561212e-07, 203),
         (4.3082835367561212e-07, 180), (4.3082835367561212e-07, 174), (4.3082835367561212e-07, 149), (4.3082835367561212e-07, 148),
         (4.3082835367561212e-07, 96), (4.3082835367561212e-07, 37), (4.3082835367561212e-07, 13), (2.8721890245040806e-07, 213),
         (2.8721890245040806e-07, 209), (2.8721890245040806e-07, 171), (2.8721890245040806e-07, 94), (2.8721890245040806e-07, 35),
         (2.8721890245040806e-07, 27), (2.8721890245040806e-07, 20), (2.8721890245040806e-07, 19), (2.8721890245040806e-07, 18), (2.8721890245040806e-07, 12), (2.8721890245040806e-07, 9), (2.8721890245040806e-07, 7), (2.8721890245040806e-07, 6), (2.8721890245040806e-07, 5), (2.8721890245040806e-07, 3), (2.8721890245040806e-07, 2), (1.4360945122520403e-07, 219), (1.4360945122520403e-07, 204), (1.4360945122520403e-07, 194), (1.4360945122520403e-07, 176), (1.4360945122520403e-07, 164), (1.4360945122520403e-07, 157), (1.4360945122520403e-07, 143), (1.4360945122520403e-07, 142), (1.4360945122520403e-07, 125), (0.0, 255), (0.0, 254), (0.0, 253), (0.0, 252), (0.0, 251), (0.0, 250), (0.0, 249), (0.0, 248), (0.0, 247), (0.0, 246), (0.0, 245), (0.0, 244), (0.0, 243), (0.0, 242), (0.0, 241), (0.0, 240), (0.0, 239), (0.0, 238), (0.0, 237), (0.0, 236), (0.0, 235), (0.0, 234), (0.0, 233), (0.0, 232), (0.0, 231), (0.0, 230), (0.0, 229), (0.0, 228), (0.0, 227), (0.0, 226), (0.0, 225), (0.0, 224), (0.0, 223), (0.0, 222), (0.0, 221), (0.0, 218), (0.0, 217), (0.0, 216), (0.0, 215), (0.0, 214), (0.0, 212), (0.0, 211), (0.0, 210), (0.0, 208), (0.0, 207), (0.0, 206), (0.0, 205), (0.0, 202), (0.0, 201), (0.0, 200), (0.0, 199), (0.0, 198), (0.0, 197), (0.0, 196), (0.0, 193), (0.0, 192), (0.0, 191), (0.0, 190), (0.0, 189), (0.0, 188), (0.0, 187), (0.0, 186), (0.0, 185), (0.0, 184), (0.0, 183), (0.0, 182), (0.0, 181), (0.0, 179), (0.0, 178), (0.0, 177), (0.0, 173), (0.0, 172), (0.0, 166), (0.0, 165), (0.0, 163), (0.0, 161), (0.0, 159), (0.0, 158), (0.0, 156), (0.0, 155), (0.0, 154), (0.0, 153), (0.0, 152), (0.0, 151), (0.0, 150), (0.0, 147), (0.0, 146), (0.0, 145), (0.0, 144), (0.0, 141), (0.0, 140), (0.0, 139), (0.0, 138), (0.0, 137), (0.0, 136), (0.0, 135), (0.0, 134), (0.0, 133), (0.0, 132), (0.0, 131), (0.0, 130), (0.0, 129), (0.0, 128), (0.0, 127), (0.0, 126), (0.0, 124), (0.0, 123), (0.0, 92), (0.0, 43), (0.0, 31), (0.0, 30), (0.0, 28), (0.0, 26), (0.0, 25), (0.0, 24), (0.0, 23), (0.0, 22), (0.0, 21), (0.0, 17), (0.0, 14)]


    testDistribute = makeSeriesOfLists(ciphertext,6)
    #print testDistribute
    testFrequencyShifter = switchThenCaesarForMultipleLists(z,testDistribute)
    #print testFrequencyShifter
    testStitchItBack = reorderListsToPositions(testFrequencyShifter)
    print testStitchItBack



main()

