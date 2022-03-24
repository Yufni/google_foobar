def solution(n):
    from decimal import Decimal, localcontext
    from math import floor

    with localcontext() as ctx:
        ctx.prec = 102

        def prim_number(number):
            return Decimal(floor((Decimal(2).sqrt() - 1) * number))

        def calc_solution(number):
            if number == 0:
                return 0
            return (number * prim_number(number)) + number * (number + 1) / 2 - prim_number(number) * (prim_number(number) + 1) / 2 - calc_solution(prim_number(number))

        return str(int(calc_solution(Decimal(n))))

if __name__ == '__main__':
    print(solution('1000000000000000000000000'))