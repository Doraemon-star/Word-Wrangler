"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    update_list = []
    for num_i in list1:
        if num_i not in update_list:
            update_list.append(num_i)
    return update_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    new_list = []
    for num_i in list1:
        for num_j in list2:
            if num_i == num_j:
                new_list.append(num_i)
    return new_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
    list1 = list1[::-1]
    list2 = list2[::-1]
    new_list = []
    while list1 and list2:
        if list1[-1] < list2[-1]:
            new_list.append(list1[-1])
            list1.pop()
        elif list1[-1] > list2[-1]:
            new_list.append(list2[-1])
            list2.pop()
        else:
            new_list.append(list1[-1])
            new_list.append(list1[-1])
            list1.pop()
            list2.pop()
    if list1:
        new_list.extend(list1[::-1])
    else:
        new_list.extend(list2[::-1])
    return new_list
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    unsorted1 = list1[: len(list1)/2]
    unsorted2 = list1[len(list1)/2 :]
    if len(list1) == 0 or len(list1) == 1:
        return list1
    elif len(list1) ==2:        
        return merge(unsorted1, unsorted2)
    else:
        unsorted1 = merge_sort(unsorted1)
        unsorted2 = merge_sort(unsorted2)
        return merge(unsorted1, unsorted2)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word)==0:
        return ['']
    else:
        new_list = []
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        for string in rest_strings:
            for idx in range(len(string)+1 ):
                new_string = string[:idx] + first + string[idx:]
                new_list.append(new_string)
        return rest_strings + new_list

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    

    print netfile.read()

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()


    
    
