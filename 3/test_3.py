from part2 import find_popular_at, filter_at, get_oxygen_gen_rating, convert_to_decimal


def test_find_popular_at_bit():
    input_list = ['101', '100', '111']
    popular = find_popular_at(input_list, 0)

    assert popular == '1'


def test_find_popular_at_bit_returns_zero():
    input_list = ['101', '000', '011']
    popular = find_popular_at(input_list, 0)

    assert popular == '0'


def test_find_popular_at_bit_returns_one_on_tie():
    input_list = ['101', '000']
    popular = find_popular_at(input_list, 0)

    assert popular == '1'


def test_filter_list_based_on_match():
    input_list = ['101', '000', '100']

    filter_value = '1'
    filtered_list = filter_at(input_list, 0, filter_value)
    assert filtered_list == ['101', '100']


def test_get_oxygen_gen_rating():
    input_list = ['101', '000', '100']
    oxy_gen_rating = get_oxygen_gen_rating(input_list)
    assert oxy_gen_rating == '101'


def test_convert_to_decimal():
    binary_value = '10111'
    decimal_value = convert_to_decimal(binary_value)
    assert decimal_value == 23
