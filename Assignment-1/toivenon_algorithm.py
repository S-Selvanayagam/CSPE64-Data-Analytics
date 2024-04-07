import re
import random
import itertools
import time

# Global variables
support = 10  
samplingRate = 0.5
fraction = 0.8
canFreqItems = {}
negBorder = {}
FreqItems = {}
isPrint = False
filename = './DataSet/transformed_dataset.csv'

def splitData(line_list, splitRatio):
    """Split the data into training and testing sets."""
    length = len(line_list)
    splitSize = int(length * splitRatio)
    splitSet = []
    copiedSet = line_list[:]
    while len(splitSet) < splitSize:
        rangeIndex = random.randrange(len(copiedSet))
        splitSet.append(copiedSet.pop(rangeIndex))
    return splitSet

def getRandomSample(ratio):
    """Get a random sample of data."""
    lineList = []
    with open(filename, "r+") as my_file:
        for line in my_file:
            temp = re.sub(r',', ' ', line)
            temp = temp.split()        
            lineList.append(temp)
    return splitData(lineList, ratio)

def getSupportValue(sup):
    """Calculate the support value."""
    return sup * fraction * samplingRate

def getCanFreqItemsAndNegBorder(inputList, _pass, sup):
    """Find candidate frequent items and negative border."""
    global canFreqItems, negBorder
    flag = False
    Items = {}
    for subList in inputList:
        if _pass == 1:
            tempItems = list(itertools.combinations(subList, _pass))
            for tuples in tempItems:
                Items[tuples] = Items.get(tuples, 0) + 1
        else:
            tempItems = list(itertools.combinations(subList, _pass))
            for tuples in tempItems:
                temp2Items = list(itertools.combinations(tuples, _pass - 1))
                for item in temp2Items:
                    if item in canFreqItems:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    tuples = tuple(sorted(tuples))
                    Items[tuples] = Items.get(tuples, 0) + 1

    for key in Items:
        if Items[key] >= sup:
            canFreqItems[key] = Items[key]
        else:
            negBorder[key] = Items[key]

    lenCanFreqItemsCurItr = len(canFreqItems)
    return canFreqItems, negBorder, lenCanFreqItemsCurItr

def getFreqItems(inputList, _pass, sup):    
    """Get frequent items."""
    global FreqItems, isPrint
    flag = False
    Items = {}
    for subList in inputList:
        if _pass == 1:
            tempItems = list(itertools.combinations(subList, _pass))
            for tuples in tempItems:
                Items[tuples] = Items.get(tuples, 0) + 1
        else:
            tempItems = list(itertools.combinations(subList, _pass))
            for tuples in tempItems:
                temp2Items = list(itertools.combinations(tuples, _pass - 1))
                for item in temp2Items:
                    if item in FreqItems:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    tuples = tuple(sorted(tuples))
                    Items[tuples] = Items.get(tuples, 0) + 1

    for key in Items:
        if Items[key] >= sup:
            FreqItems[key] = Items[key]

    lenFreqItemsCurItr = len(FreqItems)
    return FreqItems, lenFreqItemsCurItr

def getList(my_dict):
    """Get sorted list of keys from dictionary."""
    return sorted(my_dict.keys())

def convertTupleToList(freqItems):
    """Convert tuple items to list."""
    return [list(tuples) for tuples in freqItems]

def findMaxLenOfItem(my_list):
    """Find maximum length of item in list."""
    return max(len(item) for item in my_list)

def extractList(my_list,filename):
    """Extract items from the list."""
    maxLen = findMaxLenOfItem(my_list)
    for size in range(1, maxLen + 1):
        new_list = [item for item in my_list if len(item) == size]
        new_list.sort()
        print("Items of size %d : " % size)
        output_file.write("Items of size %d : " % size + "\n")
        print(new_list)
        output_file.write(str(new_list) + "\n")

def compare(list1, list2):
    """Compare two lists."""
    return any(item in list2 for item in list1)

if __name__ == '__main__':
    output_file = open("./Outputs/toivonen_output.txt", "w")
    startTime = time.time()

    repeatToivonen = True
    noOfItr = 0
    while repeatToivonen:
        noOfItr += 1
        repeatToivonen = False

        # Generating Frequent Items from the Sample Data
        line = getRandomSample(samplingRate)    
        sampleSupport = getSupportValue(support)
        _pass = 1    
        lenCanFreqItemsCurItr = 1
        lenCanFreqItemsPrevItr = 0
        while lenCanFreqItemsCurItr != lenCanFreqItemsPrevItr:
            lenCanFreqItemsPrevItr = lenCanFreqItemsCurItr    
            canFreqItems, negBorder, lenCanFreqItemsCurItr = getCanFreqItemsAndNegBorder(line, _pass, sampleSupport)
            _pass += 1

        print("Frequent Item sets from the sample :")  
        output_file.write("Frequent Item sets from the sample :\n")
        canFreqItemsList = getList(canFreqItems)
        canFreqItemsList = convertTupleToList(canFreqItemsList)    
        extractList(canFreqItemsList,output_file)

        print("\nItem sets in negative border from the sample :")  
        output_file.write("\nItem sets in negative border from the sample :\n")
        negBorderList = getList(negBorder)
        negBorderList = convertTupleToList(negBorderList)    
        extractList(negBorderList,output_file)

        line = getRandomSample(1)
        lenFreqItemsCurItr = 1
        lenFreqItemsPrevItr = 0     
        _pass = 1
        while lenFreqItemsCurItr != lenFreqItemsPrevItr:
            lenFreqItemsPrevItr = lenFreqItemsCurItr    
            freqItems, lenFreqItemsCurItr = getFreqItems(line, _pass, support)
            _pass += 1               

            print("******************************************")
            print("\nFrequent items in the entire data set:")
            output_file.write("******************************************\n")
            output_file.write("\nFrequent items in the entire data set:\n")
            FreqItemList = getList(FreqItems)
            FreqItemList = convertTupleToList(FreqItemList)
            extractList(FreqItemList,output_file)

            flag = compare(negBorderList, FreqItemList)
            print("\nIs the negative border of sample in the frequent Item List of whole data set : " + str(flag))
            output_file.write("\nIs the negative border of sample in the frequent Item List of whole data set : " + str(flag) + "\n")
            repeatToivonen = flag

        endTime = time.time()
        print("Toivonen Algorithm Execution Completed!")
        print("Duration: ", endTime - startTime)
        output_file.write("Duration: " + str(endTime - startTime) + "\n")
        output_file.write("No. of Iterations : " + str(noOfItr) + "\n")
        output_file.write("Fraction of transactions used : " + str(samplingRate) + "\n")
        output_file.write("Support : " + str(support) + "\n")
        output_file.write("Confidence : " + str(fraction) + "\n")
        output_file.close()
