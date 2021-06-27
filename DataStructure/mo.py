












def BBsort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def writeresult(path, result):
    with open(path, 'w' ,encoding='utf-8') as source:
            source.writelines(result)