from readCSV import read_csv


def write_csv(path , data):
    with open(path,mode="w") as myFile:
        headers = data[0].keys()
        myFile.write(";".join(headers)+"\n")
        for line in data:
            values =[]
            for header in headers:
                values.append(str(line.get(header)))
            myFile.write(";".join(values)+'\n')

readData = read_csv("input.csv")
write_csv("output.csv",readData)