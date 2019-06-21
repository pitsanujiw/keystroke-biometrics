import json
import glob
import math
import operator
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def loadDataset(path, ngram):
    dataset = []
    files = glob.glob(path)
    i=1

    for file_name in files:
        with open(file_name) as files:
            read_data = json.load(files)
        # print(type(read_data[ngram]))
        # dataset.update({str(i)+"_"+read_data["name"]:read_data[ngram]})
        dataset.append(read_data[ngram])
        i += 1

    return dataset

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        # dist = euclideanDistance(testInstance, trainingSet[x], length)
        dist, path = fastdtw(testInstance, trainingSet[x], dist=euclidean)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
 
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main():
    # prepare data
    trainingSet = []
    testSet = []

    ngram = "5gram"
    train_path = "new_data\\en\\templete\\*.json"
    test_path = "new_data\\en\\query\\*.json"
    trainingSet = loadDataset(train_path, ngram)
    testSet = loadDataset(test_path, ngram)

    print("training set = " + str(len(trainingSet)))
    print("test set = " + str(len(testSet)))

    # generate predictions
    print("The experiment of " + ngram)
    predictions=[]
    k = 1
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        print(neighbors)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

main()