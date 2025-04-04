from functions import *

# 학년 전체 학생의 평균: 50점

if __name__ == '__main__':
    raw_data = get_data_from_excel('class_2_3.xlsx') #1
    scores = list(raw_data.values()) 

    avrg = average(scores) #2
    variance = variance(scores, avrg) #3
    stanard_deviation = std_dev(variance) #4
 
    print('평균: {0}, 분산: {1}, 표준편차: {2}'.format(
        avrg, variance, stanard_deviation))
    evaluateClass(avrg, 50, stanard_deviation, 20) #5