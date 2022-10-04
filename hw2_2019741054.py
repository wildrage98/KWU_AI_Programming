f = open('hw2.csv','r', encoding='UTF8') #csv파일 읽어오기
index_list = f.readline() 
a = f.readlines() # 읽기시작할 부분
print(index_list)
index_list = index_list.split(',') # 리스트 정렬

dict1 ={} #야구선수 key : 이름. value : 데이터

for line in a:
    line = line.strip() #개행문자 건너뛰기
    string = line.split(',') # ', '기준으로 나눔
    dict1[string[0]] = string[1:] # 딕셔너리에 넣기 key : 선수이름, value : 데이터

def Name(name): #mode 1 이름
    if name not in dict1:
        print("없는 선수")
        return 0
    print(dict1[name])


def Name_Score(name,stats):#mode 2 이름, 항목
    if name not in dict1:
        print("존재하지 않습니다")
        return 0
    if stats not in index_list:
        print("존재하지 않습니다")
        return 0
    temp_list = dict1[name]
    temp_n = index_list.index(stats)
    print(temp_list[temp_n-1])


def stats(stats):#mode 3 항목
    if stats not in index_list:
        print("존재하지 않습니다")
        return 0
    temp_n = index_list.index(stats)
    stats_list = []
    for i in dict1.values():
        stats_list.append(i[temp_n-1])
    stats_list.sort(reverse=True)
    print(stats_list)

while(True):
    mode_num = int(input("1,2,3,4,중 선택해주세요 "))
    if mode_num == 1:
        name = input("이름 : ")
        Name(name)
    elif mode_num == 2:
        name = input("이름 : ")
        stats = input("스탯 : ")
        Name_Score(name,stats)
    elif mode_num == 3:
        stats = input("스탯 : ")
        stats(stats)
    elif mode_num == 4:# 4누를시 종료
        break

f.close()