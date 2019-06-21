import time
import json
import glob
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
import operator

def load_data_set(path, ngram):
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
        dist, path = fastdtw(testInstance[1], trainingSet[x][1], dist=euclidean)
        distances.append((trainingSet[x][0], dist))
    distances.sort(key=operator.itemgetter(1))
    return distances
 
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][0] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def experiment(attribute, dataset, experiment_type):
    # prepare data
    training_set = []
    test_set = []
    templete = "\\templete\\*.json"
    query = "\\query\\*.json"

    train_path = dataset + templete
    test_path = dataset + query
    training_set = load_data_set(test_path, attribute)
    test_set = load_data_set(train_path, attribute)

    print("----------------------------------------------------")
    print("dataset: " + dataset)
    print("attribute: " + attribute)
    print("experiment type: " + experiment_type)
    print("training set number: " + str(len(test_set)))
    print("test set number: " + str(len(training_set)))

    # generate predictions
    predictions=[]
    k = 1
    start = time.time()
    for x in range(len(training_set)):
        neighbors = getNeighbors(test_set, training_set[x], k)
        print(neighbors[0:3])
        predictions.append(neighbors[0][0])
        print('> predicted=' + repr(neighbors[0]) + ', actual=' + repr(training_set[x][0]))
    accuracy = getAccuracy(training_set, predictions)
    end = time.time()
    print('Accuracy: ' + repr(accuracy) + '%')
    print("Time used: " + str(end-start) + " seconds.")
    print("----------------------------------------------------\n")

# [non-fourier_non-mapping, non-fourier_mapping, fourier_non-mapping, fourier_mapping]
experiment_type = "non-fourier_non-mapping"
# [typo_data_set, non-typo_data_set]
data_set_type = "cut_non_typo_data_set"
# ["en_puma", "th_font_test", "th_breakfast"]
data_set_names = ["en_puma", "th_font_test", "th_breakfast"]
attributes = ["5gram", "4gram", "3gram", "2gram", "1gram", "duration"] #  "keyPressed", "keyReleased"

for data_set_name in data_set_names:
    for attribute in attributes:
        experiment(attribute, data_set_type+"\\"+data_set_name, experiment_type)