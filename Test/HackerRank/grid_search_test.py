from HackerRank.grid_search import does_pattern_exist
from Test.unit_test_template import UnitTestTemplate


class GridSearchTest(UnitTestTemplate):
    def test_does_pattern_exist_easy_found(self):
        grid = ['1234567890',
                '0987654321',
                '1111111111',
                '1111111111',
                '2222222222']
        pattern = ['876543',
                   '111111',
                   '111111']
        expected = True
        actual = does_pattern_exist(grid, pattern)
        self.assertEqual(expected, actual)

        pattern = ['11',
                   '11',
                   '22']
        expected = True
        actual = does_pattern_exist(grid, pattern)
        self.assertEqual(expected, actual)

    def test_does_pattern_exist_medium_found(self):
        grid = ['7283455864',
                '6731158619',
                '8988242643',
                '3830589324',
                '2229505813',
                '5633845374',
                '6473530293',
                '7053106601',
                '0834282956',
                '4607924137']
        pattern = ['9505',
                   '3845',
                   '3530']
        expected = True
        actual = does_pattern_exist(grid, pattern)
        self.assertEqual(expected, actual)

    def test_does_pattern_exist_hard_not_found(self):
        grid = ['400453592126560',
                '114213133098692',
                '474386082879648',
                '522356951189169',
                '887109450487496',
                '252802633388782',
                '502771484966748',
                '075975207693780',
                '511799789562806',
                '404007454272504',
                '549043809916080',
                '962410809534811',
                '445893523733475',
                '768705303214174',
                '650629270887160']
        pattern = ['99',
                   '99']
        expected = False
        actual = does_pattern_exist(grid, pattern)
        self.assertEqual(expected, actual)

    def test_does_pattern_exist_not_found_due_to_misalignment(self):
        grid = ['11111',
                '12121',
                '21212']
        pattern = ['12',
                   '12']
        expected = False
        actual = does_pattern_exist(grid, pattern)
        self.assertEqual(expected, actual)
