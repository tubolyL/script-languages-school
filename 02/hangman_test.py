import unittest

import parameterized as parameterized

from hangman import get_all_index


class HangmanTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_all_index_should_return_empty_if_there_is_no_match(self):
        #Given
        text = "b"
        word = "a"
        expected = []
        #When
        actual = get_all_index(text, word)
        #Then
        self.assertEqual(actual, expected)

    def test_get_all_index_should_return_zero_for_a_single_letter_matching_string(self):
        text = "l"
        word = "hello"
        expected = [2, 3]

        actual = get_all_index(text, word)
        self.assertEqual(expected, actual)

    def test_get_all_index_should_raise_value_error_if_text_is_empty(self):
        #Given
        text = ''
        word = "hello"
        #When Then
        with self.assertRaises(ValueError):
            get_all_index(text, word)

    def test_get_all_index_should_raise_type_error_if_text_is_integer(self):
        # Given
        text = 1
        word = "hello"
        # When Then
        with self.assertRaises(TypeError):
            get_all_index(text, word)

    def test_get_all_index_should_raise_type_error_if_text_is_list(self):
        # Given
        text = [1]
        word = "hello"
        # When Then
        with self.assertRaises(TypeError):
            get_all_index(text, word)

    ### I Have No idea

    @parameterized.expand(
        {
            (1,),
            ([1],),
            (1 + 5j,)
        })
    def test_get_all_index_should_raise_type_error_if_text_is_not_str(self):
        text = "a"
        word = "hello"
        self.assertRaises(TypeError, get_all_index, text, word)


if __name__ == "__main__":
    unittest.main()

