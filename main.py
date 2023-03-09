import math

def count_pairs(number_list, power, distance):
    divisible_by_power = set()


    number_list = number_list.strip('[]').split(',')
    number_list = sorted(number_list)


    for number in number_list:
        if int(number) % power == 0:
            divisible_by_power.add(number)

    power_results = {}
    for number in number_list:
        power_results[number] = math.pow(int(number), power)

    pair_count = 0
    for i in range(len(number_list)):
        for j in range(i+1, len(number_list)):
            if number_list[i] in divisible_by_power or number_list[j] in divisible_by_power:
                if abs(power_results[number_list[i]] - power_results[number_list[j]]) <= distance:
                    pair_count += 1
    
    return pair_count


if __name__ == '__main__':
    input_str = input("Input: ")
    number_list, power, distance = input_str.split(", ")
    power = int(power)
    distance = int(distance)

    print(count_pairs(number_list, power, distance))
