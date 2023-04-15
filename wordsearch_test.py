"""
לשים את כל הקבצים בתיקיה עם הקובץ wordsearch.py
מקווה שיעבוד בסדר, זאת פעם ראשונה שאני מנסה אז תהיו סלחנים.
אם לא עברתם את הטסט ממליץ לדאבג ולראות איפה נכשלתם ולבדוק
"""
import timeit
start = timeit.default_timer()


import unittest
import sys
try: from wordsearch import *
except: print("make sure that the script name is 'wordsearch")
zmatrix_file = 'matrix^1.txt'
zword_file = "words^1.txt"
zword_list = read_wordlist(zword_file)
zmatrix_list = read_matrix(zmatrix_file)




class MyTestCase(unittest.TestCase):


    def test_existance_of_variable(self):
        if not zmatrix_list or not zword_list:
            sys.exit()
    def test_results(self):

        direction_yzl = [('milai',1),('zooop',1),('aba',1),('dldi',1),('ooo',1),('sis',1),('hi',1)]
        direction_rdu = [('messi',2),('shlomi',2),('ssi',2),('hod',1),('aba',1),('hi',2)]
        direction_xw = [('hi',2),('ooo',1),('kn',1),('sis',1),('dldi',1)]

        zwords_found = find_words(zword_list,zmatrix_list,'rdu')
        for result in zwords_found:
            assert result in direction_rdu, "r, d or u problem \n  problem:" + str(set(zwords_found)-set(direction_rdu)) + "\nshould found: " + str(set(direction_rdu)-set(zwords_found))
        assert len(zwords_found) == len(direction_rdu),"r, d or u problem \n shouldnt found:" + str(set(zwords_found)-set(direction_rdu)) + "\nshould found: " + str(set(direction_rdu)-set(zwords_found))
        zwords_found = find_words(zword_list, zmatrix_list, 'yzl')
        for result in zwords_found:
            assert result in direction_yzl, "y z or l problem \n  problem:" + str(set(zwords_found)-set(direction_yzl)) + "\nshould found: " + str(set(direction_yzl)-set(zwords_found))
        assert len(zwords_found) == len(direction_yzl), "y z or problem \n :" + str(set(zwords_found) - set(direction_yzl)) + "\nshould found: " + str(set(direction_yzl) - set(zwords_found))
        zwords_found = find_words(zword_list, zmatrix_list, 'xw')
        for result in zwords_found:
            assert result in direction_xw, "x or w problem \n  problem:" + str(set(zwords_found)-set(direction_xw)) + "\nshould found: " + str(set(direction_xw)-set(zwords_found))
        assert len(zwords_found) == len(direction_xw), "x or w problem \n  :" + str(set(zwords_found) - set(direction_xw)) + "\nshould found: " + str(set(direction_xw) - set(zwords_found))
        stop = timeit.default_timer()
        print("אם לא נכשלת עד עכשיו הכל טוב בחיפוש")
        print("מי רוצה לשפר את הטסט, שיקח את זה כתרגיל בית")
        print('Running time: ', stop - start)

