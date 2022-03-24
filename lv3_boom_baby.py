def solution(m, f):
    m = int(m)
    f = int(f)

    counter = 0

    if m == 1 and f == 1:
        return str(counter)
    elif m == 1 and f == 0:
        return str(counter)
    elif m == 0 and f == 1:
        return str(counter)
    elif m == 0 and f == 0:
        return str(counter)
    elif m == 0 and f > 1:
        return 'impossible'
    elif m > 1 and f == 0:
        return 'impossible'
    
    while True:

        if m > f:
            counter = counter + (m // f)
            m = (m % f)
        elif f > m:
            counter = counter + (f // m)
            f = (f % m)

        if m == 1 and f == 1:
            return str(counter)
        elif m == 1:
            return str((f - 1) + counter)
        elif f == 1:
            return str((m - 1) + counter)
        elif m % 2 == 0 and f % 2 == 0:
            return 'impossible'
        elif f == m:
            return 'impossible'
        elif m <= 0 or f <= 0:
            return 'impossible'
        
        counter += 1

        if m > f:
            m = m - f
        elif m < f:
            f = f - m


if __name__ == '__main__':
    print(solution(4, 7))