from board import Board


def test_builds_all_possible_rows():
    input = [1, 2, 3, 4, 5,
             6, 7, 8, 9, 10,
             11, 12, 13, 14, 15,
             16, 17, 18, 19, 20,
             21, 22, 23, 24, 25]

    b = Board(input)
    assert b.get_potential_rows() == [[1, 2, 3, 4, 5],
                                      [6, 7, 8, 9, 10],
                                      [11, 12, 13, 14, 15],
                                      [16, 17, 18, 19, 20],
                                      [21, 22, 23, 24, 25]]


def test_builds_all_possible_columns():
    input = [1, 2, 3, 4, 5,
             1, 2, 3, 4, 5,
             1, 2, 3, 4, 5,
             1, 2, 3, 4, 5,
             1, 2, 3, 4, 5]

    b = Board(input)
    assert b.get_potential_columns() == [[1, 1, 1, 1, 1],
                                         [2, 2, 2, 2, 2],
                                         [3, 3, 3, 3, 3],
                                         [4, 4, 4, 4, 4],
                                         [5, 5, 5, 5, 5]]


def test_get_all_possible_winners():
    input = [1, 2, 3, 4, 5,
             1, 2, 3, 4, 5,
             1, 2, 3, 4, 5,
             1, 2, 3, 4, 5,
             1, 2, 3, 4, 5]

    b = Board(input)
    assert b.get_potential_winners() == [[1, 2, 3, 4, 5],
                                         [1, 2, 3, 4, 5],
                                         [1, 2, 3, 4, 5],
                                         [1, 2, 3, 4, 5],
                                         [1, 2, 3, 4, 5],
                                         [1, 1, 1, 1, 1],
                                         [2, 2, 2, 2, 2],
                                         [3, 3, 3, 3, 3],
                                         [4, 4, 4, 4, 4],
                                         [5, 5, 5, 5, 5]]


def test_mark_number_changes_all_matching_to_x():
    input = [1, 2, 3, 4, 5,
             6, 7, 8, 9, 10,
             11, 12, 13, 14, 15,
             16, 17, 18, 19, 20,
             21, 22, 23, 24, 25]

    b = Board(input)

    b.mark(1)

    assert b.get_potential_rows()[0] == ['x', 2, 3, 4, 5]
    assert b.get_potential_columns()[0] == ['x', 6, 11, 16, 21]


def test_has_winner_if_a_potential_winner_is_all_marked():
    input = ['x', 'x', 'x', 'x', 'x',
             1, 2, 3, 4, 5,
             1, 2, 3, 4, 5,
             1, 2, 3, 4, 5,
             1, 2, 3, 4, 5]

    b = Board(input)

    assert b.is_winner() == True

def test_calc_winning_score():
    input = ['x', 'x', 'x', 'x', 'x',
             'x', 'x', 'x', 'x', 'x',
             'x', 'x', 'x', 'x', 'x',
             'x', 'x', 'x', 'x', 'x',
             1, 2, 3, 4, 5]

    b = Board(input)

    b.mark(10)
    assert b.calc_score() == 150
