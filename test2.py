data = []
def load_data(file):
    f = open(file, "rt", encoding='utf-8')
    global data
    print(data)
    data = f.readline()
    print("Data : ")
    print(data)

    lt_num_data = []
    temp = data.split()
    print(temp)

    for i in temp:
        lt_num_data.append(int(i))

    print(lt_num_data)
    f.close()

    return lt_num_data

data = load_data("C:/PythonExam/test.txt")