import matplotlib.pyplot as plt
from math import sqrt, atan2

def solution(dimensions, your_position, trainer_position, distance):
    width = dimensions[0]
    height = dimensions[1]

    your_right_points = [your_position]
    your_left_points = []
    dead_points = []

    trainer_right_points = [trainer_position]
    trainer_left_points = []
    target_points = []

    point_dict = {}

    def grade(point):
        if point[0] - your_position[0] == 0:
            if point[1] < your_position[1]:
                return 'Vertical_Bot'
            if point[1] > your_position[1]:
                return 'Vertical_top'
        else:
            return atan2(float(point[1] - your_position[1]), float(point[0] - your_position[0]))

    def length(origin, point):
        x = origin[0] - point[0]
        y = origin[1] - point[1]
        return sqrt((x**2) + (y**2))

    def left_bot_gen(position, measure, stop):
        actual_position = position
        while True:
            if actual_position <= stop:
                actual_position -= position * 2
                yield actual_position
                actual_position -= (measure - position) * 2
                yield actual_position
            else:
                raise StopIteration
    
    def right_top_gen(position, measure, stop):
        actual_position = position
        while True:
            if actual_position <= stop:
                actual_position += (measure - position) * 2
                yield actual_position
                actual_position += position * 2
                yield actual_position
            else:
                raise StopIteration
    
    if length(your_position, trainer_position) > distance:
        return 0

    if length([0,0], trainer_position) < length([0,0], your_position) and not isinstance(grade(trainer_position), str):
        point_dict[grade(trainer_position)] = [trainer_position, 'target', length(your_position, trainer_position)]
    else:
        point_dict[grade(trainer_position)] = [trainer_position, 'target', length(your_position, trainer_position)]


    def create_points(generator, list, dict, axis, coordinate, identifier):
        for element in generator:
            if axis == 0:
                point = [element, coordinate]
            elif axis == 1:
                point = [coordinate, element]
            

            if length(your_position, point) > distance:
                return

            try:
                if dict[grade(point)][2] < length(your_position, point):
                    list.append(point)
                else:
                    dict[grade(point)] = [point, identifier, length(your_position, point)]
                    list.append(point)
            except KeyError:
                dict[grade(point)] = [point, identifier, length(your_position, point)]
                list.append(point)
    

    def calculate(guy, left_list, right_list, printing_list):
        if guy == your_position:
            identifier = 'dead_point'
        elif guy == trainer_position:
            identifier = 'target'
        right_points = right_top_gen(guy[0], width, distance * 2)
        left_points = left_bot_gen(guy[0], width, distance * 2)
        create_points(right_points, right_list, point_dict, 0, guy[1], identifier)
        create_points(left_points, left_list, point_dict, 0, guy[1], identifier)
        def quadrants(point_list, dict):
            for element in point_list:
                top_points = right_top_gen(guy[1], height, distance * 2)
                bot_points = left_bot_gen(guy[1], height, distance * 2)
                create_points(top_points, printing_list, dict, 1, element[0], identifier)
                create_points(bot_points, printing_list, dict, 1, element[0], identifier)
        quadrants(right_list, point_dict)
        quadrants(left_list, point_dict)

    calculate(your_position, your_left_points, your_right_points, dead_points)
    calculate(trainer_position, trainer_left_points, trainer_right_points, target_points)

    # print('Dict: ', point_dict)

    def counter(dict):
        count = 0
        for element in dict:
            if dict[element][1] == 'target':
                count +=1
        return count
    
    
    result = counter(point_dict)

    print(result)


    # plt.plot([point[0] for point in your_right_points], [point[1] for point in your_right_points], '^')
    # plt.plot([point[0] for point in your_left_points], [point[1] for point in your_left_points], '^')
    # plt.plot([point[0] for point in dead_points], [point[1] for point in dead_points], '^')
    # plt.plot([point[0] for point in trainer_right_points], [point[1] for point in trainer_right_points], 'o')
    # plt.plot([point[0] for point in trainer_left_points], [point[1] for point in trainer_left_points], 'o')
    # plt.plot([point[0] for point in target_points], [point[1] for point in target_points], 'o')
    # plt.plot([point_dict[point][0][0] for point in point_dict], [point_dict[point][0][1] for point in point_dict], '*')
    # plt.show()



if __name__ == '__main__':
    solution([300,275], [150,150], [185,100], 500)
    # 9
    solution([300,275], [150,150], [185,100], 3000)
    # 338
    solution([3, 2], [1, 1], [2, 1], 4)
    # 7
    solution([1250,1250], [150,300], [800,950], 10000)
    # 200
    solution([23,10],[6,4],[3,2],23)
    # 8
    solution([10, 10], [4, 4], [3, 3], 3000)
    # 739323
    solution([2,5], [1,2], [1,4], 11)
    # 27
    solution([10, 10], [5, 5], [5, 4], 300)
    # 2637
    solution([10, 10], [5, 4], [5, 5], 300)
    # 2637
    solution([10, 10], [5, 5], [4, 5], 300)
    # 2637
    solution([10, 10], [5, 6], [4, 5], 300)
    # 2770
    solution([10, 10], [5, 5], [4, 7], 300)
    # 2733
    solution([10,10],[4,4],[3,4],150)
    # 658
    solution([1250,1250], [1000,1000], [500,400], 10000)
    # 196
    solution([5,5], [2,2], [1,1], 34)
    # 133