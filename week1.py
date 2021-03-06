import pandas as pd
import itertools as it
import math

def day1():
    myString = "237369991482346124663395286354672985457326865748533412179778188397835279584149971999798512279429268727171755461418974558538246429986747532417846157526523238931351898548279549456694488433438982744782258279173323381571985454236569393975735715331438256795579514159946537868358735936832487422938678194757687698143224139243151222475131337135843793611742383267186158665726927967655583875485515512626142935357421852953775733748941926983377725386196187486131337458574829848723711355929684625223564489485597564768317432893836629255273452776232319265422533449549956244791565573727762687439221862632722277129613329167189874939414298584616496839223239197277563641853746193232543222813298195169345186499866147586559781523834595683496151581546829112745533347796213673814995849156321674379644323159259131925444961296821167483628812395391533572555624159939279125341335147234653572977345582135728994395631685618135563662689854691976843435785879952751266627645653981281891643823717528757341136747881518611439246877373935758151119185587921332175189332436522732144278613486716525897262879287772969529445511736924962777262394961547579248731343245241963914775991292177151554446695134653596633433171866618541957233463548142173235821168156636824233487983766612338498874251672993917446366865832618475491341253973267556113323245113845148121546526396995991171739837147479978645166417988918289287844384513974369397974378819848552153961651881528134624869454563488858625261356763562723261767873542683796675797124322382732437235544965647934514871672522777378931524994784845817584793564974285139867972185887185987353468488155283698464226415951583138352839943621294117262483559867661596299753986347244786339543174594266422815794658477629829383461829261994591318851587963554829459353892825847978971823347219468516784857348649693185172199398234123745415271222891161175788713733444497592853221743138324235934216658323717267715318744537689459113188549896737581637879552568829548365738314593851221113932919767844137362623398623853789938824592"
    # Part 1
    sum = 0
    lastChar=myString[len(myString)-1]
    for char in myString:
      if char == lastChar:
        sum += int(lastChar)
      lastChar = char

    print sum

    # Part 2
    # Creates a tuple of [char in first half, char in second half]
    myStringTuple = zip(myString[:len(myString)/2], myString[len(myString)/2:])
    # Maps each tuple to its sum if elements are equal, 0 otherwise, and sums that new list
    print sum(map(lambda x: int(x[0])*2 if x[0] == x[1] else 0, myStringTuple))


def day2():
    data = pd.read_csv('day2input.tsv', sep='\t', header=None)

    # Part 1
    print (data.max(axis=1) - data.min(axis=1)).sum()

    # Part 2
    # Function to return the division result of a pair of numbers if they divide evenly
    def divider(pair):
        if max(pair[0], pair[1]) % min(pair[0], pair[1]) == 0:
            return max(pair[0], pair[1])/min(pair[0], pair[1])

    # it.combinations(,2) returns all non-repeating 2-length tuples from a list ("ABCD" -> AB, AC, AD, BC, BD, CD)
    # This makes all such combinations and applies the divider function to them, taking one result per row and summing
    print data.apply(lambda x: max(map(divider, it.combinations(x, 2))), axis=1).sum()


def day3():
    # Know that the bottom right of every square is a perfect square, so detect which one we're in
    def detectSpiralLevel(n, target):
        if pow(n, 2) < target < pow(n+2, 2):
            return int(n+2)
        else:
            return detectSpiralLevel(n+2, target)

    def howFarFromACorner(n, target):
        corners = [pow(n, 2) - i*(n-1) for i in range(0, 5)]
        return min(map(lambda x: abs(target-x), corners))

    # Part 1
    target = 312051
    n = detectSpiralLevel(3, target)
    # Have to cut n by half+0.5, n represents the corner/level
    print str(2*math.ceil(n/2) - howFarFromACorner(n, target))
    
    
def day4():
    with open('day4.tsv') as f:
        data = f.readlines()
        f.close()

    # Part 1
    validity = map(lambda x: len(set((x.split()))) == len(x.split()), data)
    print sum(1 for x in validity if x)

    # Part 2
    def moreValidity(row):
        for i in range(len(row)-1):
            for j in range(i+1, len(row)):
                if len(row[i]) == len(row[j]) and sorted(row[i]) == sorted(row[j]):
                       return False
        return True

    validity = map(lambda x: moreValidity(x.split()), data)
    print sum(1 for x in validity if x)


def day5():
    with open('day5input.csv') as f:
        rawData = f.readlines()
        f.close()
    data = [int(x) for x in rawData]

    # Parts 1 and 2: For part 1, set offsetLimit to 999999, for part 2, set to 3
    offsetLimit = 3
    curIndex, numSteps = 0, 0
    state = True
    while state:
        try:
            n = data[curIndex]
            if n >= offsetLimit:
                data[curIndex] = n-1
            else:
                data[curIndex] = n+1
            curIndex += n
            numSteps += 1
        except Exception as e:
            state = False
            print numSteps
            print e


def day6():
    data = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]

    # Parts 1 & 2
    # Fn to distribute the values from a cell to the rest of the cells
    def redistribute(array, amountLeft, curIndex):
        array[curIndex] +=  1
        amountLeft -= 1
        if amountLeft > 0:
            return redistribute(array, amountLeft, (curIndex+1) % len(array))
        else:
            return array

    def selectDonorBank(array):
        maxVal = max(array)
        return min([i for i, j in enumerate(array) if j == maxVal])

    oldLists = []
    oldLists.append(list(data)) # list(data) required everywhere so we're copying, not referencing
    state = True
    itr = 0

    while state:
        index = selectDonorBank(data)
        toDistribute = data[index]
        data[index] = 0
        data = list(redistribute(data, toDistribute, (index + 1) % len(data)))
        itr += 1
        if data in oldLists:
            state = False
            print "Loop started on iteration " + str([i for i, j in enumerate(oldLists) if j == data])
        else:
            oldLists.append(list(data))

    print "Loop detected on iteration " + str(itr)


def day7():
    def cleandata(row):
        if len(row) < 3:
            return (row[0], None)
        else:
            return (row[0], row[3:])


    def findTowers(data, rows):
        kill = []
        print rows
        for val in rows:
            if val in data.keys():
                kill += [val]
            if val[:-1] in data.keys(): # I AM LAZY AND DO NOT WANT TO STRIP COMMAS
                kill += [val[:-1]]
        return data, kill

    with open('day7input.txt') as f:
        rawData = f.readlines()
        f.close()
    data = dict(cleandata(x.split()) for x in rawData)

    while len(data) > 3:
        keysToKill = []
        for key, value in data.iteritems():
            if value is None:
                keysToKill += [key]
            else:
                data, kill = findTowers(data, value)
                keysToKill += kill

        for elem in set(keysToKill):
            data.pop(elem)
        print keysToKill
    print data



day7()
