def solution(src: int, dest: int) -> int:

    if src == dest:
        return 0

    def lim_position_vertical(initial_position):
        n = initial_position
        yield n
        while True:
            n += 8
            if n <= 63:
                yield n
            else:
                break

    def lim_list(generator):
        return [i for i in generator]

    def lim_position_hotizontal(initial_position):
        return [i for i in range(initial_position, initial_position + 8)]
            

    def movements(src):

        def remove_movement(init_range, final_range):
            for i in range(init_range, final_range):
                available_movements.discard(i)

        #(up, left) = 1, (up, rigth) = 2,
        #(rigth, up) = 3, (rigth, down) = 4,
        #(down, rigth) = 5, (down, left) = 6,
        #(left, down) = 7, (left, up) = 8
        available_movements = {1,2,3,4,5,6,7,8}
        if src in up1_null:
            remove_movement(1,4)
            available_movements.discard(8)
        if src in up2_null:
            remove_movement(1,3)
        if src in right1_null:
            remove_movement(2,6)
        if src in right2_null:
            remove_movement(3,5)
        if src in down1_null:
            remove_movement(4,8)
        if src in down2_null:
            remove_movement(5,7)
        if src in left1_null:
            remove_movement(6,9)
            available_movements.discard(1)
        if src in left2_null:
            remove_movement(7,9)
        
        destiny_cells = set()

        if 1 in available_movements:
            destiny_cells.add(src - 17)
        if 2 in available_movements:
            destiny_cells.add(src - 15)
        if 3 in available_movements:
            destiny_cells.add(src - 6)
        if 4 in available_movements:
            destiny_cells.add(src + 10)
        if 5 in available_movements:
            destiny_cells.add(src + 17)
        if 6 in available_movements:
            destiny_cells.add(src + 15)
        if 7 in available_movements:
            destiny_cells.add(src + 6)
        if 8 in available_movements:
            destiny_cells.add(src - 10)
        
        return destiny_cells
    

    #Cells can not make (up, left), (left, up), (left, down), (down, left)
    left1_null = frozenset(lim_list(lim_position_vertical(0)))

    #Cells can not make (left, up), (left, down)
    left2_null = frozenset(lim_list(lim_position_vertical(1)))

    #Cells can not make (up, rigth), (rigth, up), (rigth, down), (down, rigth)
    right1_null = frozenset(lim_list(lim_position_vertical(7)))

    #Cells can not make (rigth, up), (rigth, down)
    right2_null = frozenset(lim_list(lim_position_vertical(6)))

    #Cells can not make (left, up), (up, left), (up, rigth), (rigth, up)
    up1_null = frozenset(lim_position_hotizontal(0))

    #Cells can not make (up, left), (up, rigth)
    up2_null = frozenset(lim_position_hotizontal(8))

    #Cells can not make (left, down), (down, left), (down, rigth), (rigth, down)
    down1_null = frozenset(lim_position_hotizontal(56))

    #Cells can not make (down, left), (down, rigth)
    down2_null = frozenset(lim_position_hotizontal(48))

    dest_cells = {}
    dest_cells[1] = movements(src)
    if dest in dest_cells[1]:
        return 1
    
    count = 1

    while True:
        new_destines = set()
        for i in dest_cells[count]:
            new_destines = new_destines | movements(i)
        
        count += 1
        dest_cells[count] = new_destines

        if dest in dest_cells[count]:
            return count


if __name__ == '__main__':
    print(solution(19, 36))
