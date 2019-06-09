import json
import glob
import math
import operator
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

def loadDataset(path, ngram):
    dataset = []
    files = glob.glob(path)
    i=1

    for file_name in files:
        with open(file_name) as files:
            read_data = json.load(files)
        dataset.append((read_data["name"], read_data[ngram]))
        i += 1

    return dataset

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    for x in range(len(trainingSet)):
        # fourier is here
        f_test = np.fft.irfft(testInstance[1])
        f_train = np.fft.irfft(trainingSet[x][1])
        dist, path = fastdtw(np.abs(f_test), np.abs(f_train), dist=euclidean)
        distances.append((trainingSet[x][0], dist))
    distances.sort(key=operator.itemgetter(1))
    return distances
 
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][0] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main(typeSet, dataSet, description):
    # prepare data
    trainingSet = []
    testSet = []

    train_path = "new_data\\" + dataSet + "\\templete\\*.json"
    test_path = "new_data\\" + dataSet + "\\query\\*.json"
    testSet = loadDataset(test_path, typeSet)
    trainingSet = loadDataset(train_path, typeSet)

    print("----------------------------------------------------")
    print("Dataset: " + dataSet)
    print("The prediction of: " + typeSet)
    print("Description: " + description)
    print("Training set: " + str(len(trainingSet)))
    print("Test set: " + str(len(testSet)))
    print("\n")

    # generate predictions
    predictions=[]
    k = 1
    start = time.time()
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        print(neighbors[0:3])
        predictions.append(neighbors[0][0])
        print('> predicted=' + repr(neighbors[0]) + ', actual=' + repr(testSet[x][0]))
    accuracy = getAccuracy(testSet, predictions)
    end = time.time()
    print("\n")
    print('Accuracy: ' + repr(accuracy) + '%')
    print("Time used: " + str(end-start) + " seconds.")
    print("----------------------------------------------------\n")

dataSet = "th2"
typeSet = ["5gram", "4gram", "3gram", "2gram", "1gram", "duration"]
description = "fourier, non-mapping"

for type_i in typeSet:
    main(type_i, dataSet, description)