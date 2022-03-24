def solution(n):
    cases = [1] + [0]*(n)
    for block in range(1, n+1):
        for quantity in range(n, block-1, -1):
            cases[quantity] += cases[quantity - block]
    return cases[-1]-1


if __name__ == '__main__':
    print(solution(15))