def load_data(file):
    f = open(file, "rt", encoding='utf-8')
    lt_num_data = {}
    for i in range(0,20):
        temp = []
        for j in f.readline().split():
            temp.append(int(j))

        # key : i + 회차
        lt_num_data[str(i+1) + "회차"] = temp

    f.close()

    return lt_num_data

def count(data): #딕셔너리를 매개변수로 받는 count함수
    result = {}  #결과를 저장할 딕셔너리 변수
    for key, value in data.items(): #회차인 key는 빈도를 계산할때 필요하지 않다.
        for i in value: #리스트를 도는 반복문
            if i not in result: #시퀀스 자료형에 해당하는지 아닌지를 알아보는 연산자=in과 not in/i를 key로 가지는 쌍이 없으면
                result[i] = 1 #초기값을 1로 쌍을 만들어주면 된다.

data = load_data("C:/PythonExam/test.txt")
print("데이터 가져오기 성공:", data)
