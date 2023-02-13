import wyrdl


def test_get_random_word():
    word_list = ['snake', 'crane', 'wyrdl']

    assert wyrdl.get_random_word(word_list) in word_list
