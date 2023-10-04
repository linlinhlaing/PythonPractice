import os
print(os.getcwd())
def parse_header(dataLine):
    return dataLine.split(';')
def parse_data(dataLine):
    value = [float(item) if item != '\n' else 0.0 for item in dataLine.split(';')]
    return value
def makeDict(header,floatData):
    result = {}
    for key,value in zip(header,floatData):
        result[key] = value
    # result = [{str(header[i]):(floatData[i])} for i in range(len(header))]
    return result
def read_csv(path):
    with open(path, mode="r") as myFile:
        data = myFile.readlines()
        header = parse_header(data[0].strip())
        dictList = []
        for line in data[1:]:
            floatData = parse_data(line)
            dictData = makeDict(header, floatData)
            dictList.append(dictData)
        return dictList

print(read_csv("username.csv"))

