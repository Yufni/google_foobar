def solution(l):
    if len(l) < 3:
        return 0
    
    counter = 0
    right_counter = 0
    left_counter = 0

    for i in range(len(l)):
        for k in range(i+1,len(l)):
            if l[k]%l[i] == 0:
                right_counter += 1
        for j in range(i):
            if l[i]%l[j] == 0:
                left_counter += 1
        counter += right_counter * left_counter
        right_counter = 0
        left_counter = 0


    #Try 1
    # for i in range(len(l)-2):
    #     for k in range(i+1,len(l)-1):
    #         if l[k]%l[i] == 0:
    #             for j in range(k+1,len(l)):
    #                 if l[j]%l[k] == 0:
    #                     contador += 1
    
    return counter


if __name__ == '__main__':
    l = []
    for i in range(1,2000):
        l.append(i)
    print(solution([1,1,1]))