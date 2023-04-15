#################################################################
# FILE : ex5.py
# WRITER : Dana Aviran , dana.av , 211326608
# EXERCISE : intro2cs2 ex5 2022
# DESCRIPTION: Word Search game
# SITES I USED: https://stackoverflow.com/questions/11476713/determining-how-many-times-a-substring-occurs-in-a-string-in-python
#################################################################

from os.path import isfile
import sys


def check_input_args():
    # this function checks the input from the commandline
    # and returns a message if there is a wrong input
    all_directions = "udrlwxyz"  # checking the directions value
    if len(sys.argv) != 5:  # if there are more arguments than allowed
        return "the input is not supported."
    elif not isfile(sys.argv[1]):  # if one of two first files does not exist
        return "word file does not exist."
    elif not isfile(sys.argv[2]):
        return "matrix file does not exist."
    else:  # if there is a char in the directions string that is not allowed
        for i in range(len(sys.argv[4])):
            if sys.argv[4][i] not in all_directions:
                return "input of directions is not supported."
    # else, return None


def read_wordlist(filename):
    # takes the filename of the word list and returns
    # a list containing all words
    with open(filename) as our_open_file:
        word_list = our_open_file.readlines()
        for i in range(len(word_list)):
            word_list[i] = word_list[i].strip('\n')
        return word_list


def read_matrix(filename):
    # takes the filename of the matrix list and returns
    # a two dimensional list containing list for each row -
    # which contains each the letters in the row
    new_matrix_lst = []
    row = []
    with open(filename) as our_open_file:
        lst_matrix = our_open_file.readlines()
        for i in range(len(lst_matrix)):
            lst_matrix[i] = lst_matrix[i][:-1]  # we remove the str '\n'
            for j in range(len(lst_matrix[i])):  # we remove the char ','
                if j % 2 == 0:
                    row.append(lst_matrix[i][j])
            new_matrix_lst.append(row)
            row = []
    return new_matrix_lst


def matrix_without_marks(matrix_lst):
    # we get a two dimensional matrix list and return a one dimensional
    # list which contains the letters from left to right in each row
    new_matrix = []
    m_row = ""
    m_width = len(matrix_lst[0])  # the width of each row in matrix
    m_length = len(matrix_lst)  # number of rows in matrix
    i, j = 0, 0
    while i < m_length:
        while j < m_width:
            m_row += matrix_lst[i][j]  # we make a string of letters in row
            j += 1
        new_matrix.append([m_row])  # we append the row
        m_row = ""
        j = 0
        i += 1
    return new_matrix


def matrix_to_letter_combinations(matrix, directions):
    # the function gets a two dimensional list of the matrix and directions
    # and returns a list of strings that contains all combinations of the
    # letters in the matrix on base of the value of directions
    # the i index refers to the loop going over rows
    # the index j refers to the loop going over columns
    words_in_matrix = []
    current_str = ""
    matrix = matrix_without_marks(matrix) # from two dimensions to one
    m_length = len(matrix)  # matrix length of each row
    m_width = len(matrix[0][0])  # number of rows in matrix
    if 'r' in directions:  # right
        # we use the strings in matrix without marks (already left to right )
        i = 0
        while i < len(matrix):
            words_in_matrix.append(matrix[i][0])
            i += 1
    if 'l' in directions:  # left
        # we mirror the matrix without marks
        i = 0
        while i < m_length:
            current_str = matrix[i][0][::-1]
            words_in_matrix.append(current_str)
            current_str = ""
            i += 1
    if 'd' in directions:  # down
        # two loops - columns --> rows
        i = 0  # we start from the index of first row first column
        j = 0
        while j < m_width:
            while i < m_length:
                current_str += matrix[i][0][j]
                i += 1
            words_in_matrix.append(current_str)
            current_str = ""
            i = 0
            j += 1
    if 'u' in directions:  # up
        # two loops - columns --> rows
        # we start from the index of first column and last row
        i = m_length - 1
        j = 0
        while j < m_width:
            while i >= 0:
                current_str += matrix[i][0][j]
                i -= 1
            words_in_matrix.append(current_str)
            current_str = ""
            i = m_length - 1
            j += 1
    if 'y' in directions:  # down and right
        # two separate loops - the first one going through the diagonals
        # of matrix
        i = m_length - 1
        # starting from the index of first column last row
        # ending in the index of first column first row
        while i >= 0:
            n = i
            q = 0
            while n < m_length and q < m_width:
                current_str += matrix[n][0][q]
                n += 1
                q += 1
            words_in_matrix.append(current_str)
            current_str = ""
            i -= 1
        j = 1
        # starting from the index of first row second column
        # ending in the index of first row last column
        while j < m_width:
            q = j
            n = 0
            while q < m_width and n < m_length:
                current_str += matrix[n][0][q]
                n += 1
                q += 1
            words_in_matrix.append(current_str)
            current_str = ""
            j += 1
    if 'z' in directions:  # down and left
        # two separate loops - the first one going through the diagonals
        # of matrix
        i = m_length - 1
        j = m_width - 1
        # starting from the index of last column last row
        # ending in the index of first column last row
        while i >= 0:
            n = i
            q = j
            while n < m_length and q >= 0:
                current_str += matrix[n][0][q]
                n += 1
                q -= 1
            words_in_matrix.append(current_str)
            current_str = ""
            i -= 1
        j = m_width - 2
        # starting from the index one before last column and first row
        # ending in the index of first column first row
        while j >= 0:
            q = j
            n = 0
            while q >= 0 and n < m_length:
                current_str += matrix[n][0][q]
                n += 1
                q -= 1
            words_in_matrix.append(current_str)
            current_str = ""
            j -= 1
    if 'w' in directions:  # up and right
        # two separate loops - the first one going through the diagonals
        # of matrix
        i = m_length - 1
        j = m_width - 1
        # starting from the index last column and last row
        # ending in the index of first column last row
        while j >= 0:
            n = i
            q = j
            while n >= 0 and q < m_width:
                current_str += matrix[n][0][q]
                n -= 1
                q += 1
            words_in_matrix.append(current_str)
            current_str = ""
            j -= 1
        i = m_length - 2
        j = 0
        # starting from the index first column and one before  last row
        # ending in the index of first column first row
        while i >= 0:
            q = j
            n = i
            while q < m_width and n >= 0:
                current_str += matrix[n][0][q]
                n -= 1
                q += 1
            words_in_matrix.append(current_str)
            current_str = ""
            i -= 1
    if 'x' in directions:  # up and left
        # two separate loops - the first one going through the diagonals
        # of matrix
        i = m_length - 1
        j = 0
        # starting from the index first column and last row
        # ending in the index of last column last row
        while j < m_width:
            n = i
            q = j
            while n >= 0 and q >= 0:
                current_str += matrix[n][0][q]
                n -= 1
                q -= 1
            words_in_matrix.append(current_str)
            current_str = ""
            j += 1
        i = m_length - 2
        j = m_width - 1
        # starting from the index last column and one before last row
        # ending in the index of last column first row
        while i >= 0:
            q = j
            n = i
            while q >= 0 and n >= 0:
                current_str += matrix[n][0][q]
                n -= 1
                q -= 1
            words_in_matrix.append(current_str)
            current_str = ""
            i -= 1
    return words_in_matrix  # we return the list of all word combos in matrix


def find_words(word_list, matrix, directions):
    # this function gets the word list, the two dimensional list of matrix
    # and the string of directions and returns a list of tuples that each
    # contain a word found in the matrix and the number of times it was found
    mat_word_combo = matrix_to_letter_combinations(matrix, directions)
    # we get the word combo based on the given directions
    result = []  # the list of results
    counter = 0  # the counter of times the word was found
    word_lst_len = len(word_list)  # length of word list
    mat_combo_lst_len = len(mat_word_combo)  # length of list of word combos
    for i in range(word_lst_len):  # going through the word list
        if len(word_list[i]) == 1:  # if the word is a letter
            for j in range(mat_combo_lst_len):  # go through list of word combo
                # and add to counter the amount of times the letter is in the
                # word list
                counter += mat_word_combo[j].count(str(word_list[i]))
        else:  # if the word in word list is not a letter
            for j in range(mat_combo_lst_len):  # go through list of word combo
                w = 0
                # go through the indexes of each word combo and check how many
                # times the word is inside it
                for w in range(len(mat_word_combo[j])-w):
                    if mat_word_combo[j][w:w+len(word_list[i])] == \
                            word_list[i]:
                        counter += 1  # we add each time it appears in combo
        if counter > 0:  # if the word was found at least once
            result.append((word_list[i], counter))  # we append its tuple
        counter = 0  # we restart the counter for the next word in list
    return result  # we return the list of tuples


def write_output(result_lst, filename):
    # this function gets the list of tuples and inserts the results in the
    # output file. overrides the file or creates a new one.
    with open(filename, 'w') as our_open_file:
        i = 0
        while i < len(result_lst):
            our_open_file.write(str(result_lst[i][0]))
            our_open_file.write(','+str(result_lst[i][1]))
            our_open_file.write("\n")
            i += 1


def main():
    # this function wraps the whole program together
    msg = check_input_args()  # we check if one of the inputs from the command
    # line is not correct
    if msg:  # if so, we print it and end the program
        print(msg)
    else:  # else, the inputs are correct and we use the arguments values
        word_list = read_wordlist(sys.argv[1])
        m_list = read_matrix(sys.argv[2])
        results_filename = sys.argv[3]
        directions = sys.argv[4]
        if word_list == [] or m_list == []:  # if one of the files is empty
            m_result = ""  # the result is an empty file
        else:  # else, we get the list of tuples from the find_words function
            m_result = find_words(word_list, m_list, directions)
        # and we write the output in the file
        write_output(m_result, results_filename)


if __name__ == '__main__':
    main()
