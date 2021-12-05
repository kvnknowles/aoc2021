def find_popular_at(input_list, param):
    sum_of_ones = 0
    for x in input_list:
        count = int(x[param]) if x[param] == '1' else 0
        sum_of_ones += count
    if sum_of_ones >= len(input_list) / 2:
        return '1'
    else:
        return '0'

def find_least_popular_at(input_list, param):
    sum_of_ones = 0
    for x in input_list:
        count = int(x[param]) if x[param] == '1' else 0
        sum_of_ones += count
    if sum_of_ones < len(input_list) / 2:
        return '1'
    else:
        return '0'

def filter_at(input_list, filter_bit, filter_value):
    return [x for x in input_list if x[filter_bit] == filter_value]


def get_oxygen_gen_rating(input_list):
    calc_bit = 0
    while len(input_list) > 1:
        popular_value = find_popular_at(input_list, calc_bit)
        input_list = filter_at(input_list, calc_bit, popular_value)
        calc_bit += 1

    return input_list[0]

def get_co2_scrub_rating(input_list):
    calc_bit = 0
    while len(input_list) > 1:
        least_popular = find_least_popular_at(input_list, calc_bit)
        input_list = filter_at(input_list,calc_bit,least_popular)
        calc_bit += 1

    return input_list[0]

def convert_to_decimal(binary_value):
    return int(binary_value, 2)


f = open("input.txt", "r")

positions = []
for x in f:
    positions.append(x)

oxy_gen_rating = get_oxygen_gen_rating(positions)
oxy = convert_to_decimal(oxy_gen_rating)

co2_scrub_rating = get_co2_scrub_rating(positions)
co2 = convert_to_decimal(co2_scrub_rating)

print(oxy*co2)
