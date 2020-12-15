# Word-Wrangler
template https://github.com/Doraemon-star/Word-Wrangler/edit/main/README.md

# Phase One
You should first write the function remove_duplicates(list1) and intersect(list1, list2). These functions van both be written iteratively(using loops, not recursion). All of the arguments to these functions are lists in ascending order. Both function should return new sorted lists

remove_duplicates should return a new sorted list with the same elements asn the input, list1, but without andy duplicate elements.

intesect should return a new sorted list that contains only the elements that are in both input lists, list1 and list 2.

Remember that the input lists will already be sorted. You should exploit this fact to make these functions simpler to write thatn if you had to handle arbitrary lists.

# Phase Two
You should next implemment merge sorting. To do so, you will need to write two functions, merge(list1, list2) and merge_sort(list1). The input lists to merge will both be lists in ascending order. The input to merge_sort wiil be an unsorted list. While you could write merge recursively, you should write it iteratively because it will generate too many recursive calls fro reasonably sized lists. However, you must write merge_sort recursively.

merge should retrun a new sorted list that contains all of the elements in either list1 and list2.

merge_sort should return a new sorted list that contains all of the elements in list1 sorted in ascending order.

Again, remember that the input lists to merge will already be sorted. You should exploit this fact to make it simpler to  write. Further, merge_sort should use merge to help sort the list!
# Phase Three

Now, you should implement gen_all_string(word). This function is the heart of the word wrangler game. It takes a string as input and retruns a list of strings. It should return all possible strings that can be constructed from the letters in the input word. More formally, it should return all strings of length 0 to len(word) that can be composed of the letters that occur in owrd, in any order. Further, each letter should be considered distinct, so if the same letter appears twice in the word, then the output will have duplicate strings.

For example, if word is "aab", gen_all_strings would return ["", "b", "a", "ab", "ba", "a", "ab", "ba", "aa", "aa", "aab", "aab", "aba", "aba", "baa", "baa"]. Notice that the string "aa" appears twice in the output. This is because each a is considered distinct, so these two strings correspond to the two different orderings of the two a letters in the input word. Note that it does not matter in what order the strings appear in the list. The functions you have already written will be used afterwards to sort and remove duplicated from the final list.

Note this funciton is similar to something that you have previously written in this course. This time, however, ordering of the output list is not important, duplicates are allowed, and you must write it recursively. The basic idea is  as follows:
1. Split the input word into two parts: the first character and the remaining part
2. Use gen_all_strings to fenerate all appropriate strings for rest. Call this list rest_strings.
3. for each string in rest_strings, generate new strings by inserting the initial character, first, in all possible position with the string.
4. Return a list containing the strings in the rest_strings as well as the new strings generated in step 3
