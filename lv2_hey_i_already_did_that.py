def solution(n,b):
    k = len(n)

    def decimal_to_other_base(number, base):
        new_number = ''

        while number > 0:
            remainder = number % base
            new_number = str(remainder) + new_number
            number = int(number / base)
        
        return new_number
    
    
    def new_id(number, base):
        x = int(''.join(sorted(number, reverse = True)), base)
        y = int(''.join(sorted(number)), base)
        z = str(decimal_to_other_base(x-y, base))

        result = ''   

        if len(z) < k:
            for i in range(k-len(z)):
                result = result + '0'
            return result + z
        else:
            return z
    
    def comprobation(list):
        cicle_list = []
        max_number = []
        answer = 0
        for element in reversed(list):
            if element in cicle_list:
                max_number.append(answer)
                cicle_list = [element]
                answer = 1
            else:
                cicle_list.append(element)
                answer += 1
            
            if len(max_number) >= 3:
                if max_number[0] == max_number[1] and max_number[0] == max_number[2]:
                    return max_number[0], True
            
        return 0, False
    

    id_list = [n]

    answer = False

    while not(answer):
        n = new_id(n, b)
        id_list.append(n)
        full_answer = comprobation(id_list)
        answer = full_answer[0]
        
    
    return answer


if __name__ == '__main__':
    solution('210022', 3)