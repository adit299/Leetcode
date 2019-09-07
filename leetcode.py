from linked_lists import _Node, LinkedList
from typing import Any, List, Optional, Tuple


def longestCommonPrefix(strs: list) -> str:
    """
    :type strs: List[str]
    :rtype: str
    """
    i = 0
    new_str = strs[1:]
    pref = strs[0]

    while i < len(new_str):
        pref = common_letters(pref, new_str[i])
        i += 1
    return pref


def common_letters(comp: str, word: str) -> str:
    """
    Given a word and a comparison word, returns a str containing the largest
    number of uninterrupted letters common to both words. If no letters are
    common, returns the empty string
    >>> common_letters("flower", "flow")
    "flow"
    >>> common_letters("dog", "racecar")
    ""
    """
    i = 0
    pref = ""

    while i < min(len(comp), len(word)):
        if comp[i] == word[i]:
            pref += comp[i]
            i += 1
        else:
            break
    return pref


# def addTwoNumbers(l1: LinkedList, l2: LinkedList) -> LinkedList:
#     """
#     You are given two non-empty linked lists representing two non-negative
#     integers. The digits are stored in reverse order and each of their nodes
#     contain a single digit. Add the two numbers and return it as a linked list.
#     You may assume the two numbers do not contain any leading zero,
#     except the number 0 itself.
#     >>> l1 = LinkedList([1, 2, 3])
#     >>> l2 = LinkedList([5, 6, 4])
#     >>> addTwoNumbers(l1, l2) == LinkedList([7, 0, 8])
#     True
#     """
#     while


def is_valid(s: str) -> bool:
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and
    ']', determine if the input string is valid. An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.
    """
    brack_dict = {'(': ')', '{': '}', '[': ']'}
    open_char = ['(', '{', '[']
    stack = []

    for ch in s:
        if ch in open_char:
            stack.append(ch)
        elif len(stack) > 0 and ch == brack_dict[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0


def strStr(haystack: str, needle: str) -> int:
    """
    Implement strStr().
    Return the index of the first occurrence of needle in haystack, or -1 if
    needle is not part of haystack.
    """
    for i in range(len(haystack) - (len(needle) - 1)):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


def longest_palindrome(s: str) -> str:
    """
    Given a string s, find the longest palindromic substring in s.
    You may assume that the maximum length of s is 1000.
    >>> longest_palindrome("babad")
    "bab"
    >>> longest_palindrome("cbbd")
    "bb"
    """
    i = 0
    pal_lst = []

    if len(s) == 1:
        return s

    while i < len(s):
        pal_lst.extend(generate_palindrome(s[i], s[i:]))
        i += 1

    if len(pal_lst) > 0:
        return str(max(pal_lst, key=len))
    else:
        return ""


def generate_palindrome(s: str, sub: str) -> list:
    """
    Given a string s, create a substring by starting from the particular letter,
    and iterating until that same letter is reached.
    """
    i = 1
    lst = []

    while i < len(sub):
        if sub[i] == s:
            if sub[0:i+1] == sub[0:i+1][::-1]:
                lst.append(sub[0:i+1])
                i += 1
            else:
                i += 1
        else:
            i += 1
    return lst


def max_Area(height: list) -> int:
    """
    Given n non-negative integers a1, a2, ..., an , where each represents a
    point at coordinate (i, ai). n vertical lines are drawn such that the two
    endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
    with x-axis forms a container, such that the container contains
    the most water.
    """
    dim_lst = create_dimension(height)

    i = 0
    j = len(dim_lst)-1
    max_area = calc_dimension(dim_lst[i], dim_lst[j])

    while i < j:
        if dim_lst[i][0] < dim_lst[j][0]:
            i += 1
            if calc_dimension(dim_lst[i], dim_lst[j]) > max_area:
                max_area = calc_dimension(dim_lst[i], dim_lst[j])
        else:
            j -= 1
            if calc_dimension(dim_lst[i], dim_lst[j]) > max_area:
                max_area = calc_dimension(dim_lst[i], dim_lst[j])

    return max_area


def create_dimension(height: list) -> list:
    """
    Given n non-negative integers a1, a2, ..., an , creates the corresponding
    coordinates with these integers and stores them in a list.
    """
    lst = []

    for n in range(len(height)):
        lst.append((height[n], n+1))
    return lst


def calc_dimension(dim_1: tuple, dim_2: tuple) -> int:
    """
    Given two coordinates, calculates the dimension of a container created
    by connecting the two points
    """
    if dim_1[0] <= dim_2[0]:
        return dim_1[0] * (dim_2[1] - dim_1[1])
    else:
        return dim_2[0] * (dim_2[1] - dim_1[1])


def threeSumClosest(self, nums: list, target: int) -> int:
    """
    Given an array nums of n integers and an integer target,
    find three integers in nums such that the sum is closest to target.
    Return the sum of the three integers.
    You may assume that each input would have exactly one solution.
    """
    pass


def three_sum(nums: list, target: int) -> list:
    """
    Given a list of integers, and a target integer, finds three nums from the
    list that add up to the target

    """
    pass


def generate_parens(n):
    """
    Given n pairs of parentheses,
    write a function to generate all combinations of well-formed parentheses.
    For example, given n = 3, a solution set is:
    [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
    ]
    """
    if n == 0:
        return []
    return generate_parens_helper('', n, 0)


def generate_parens_helper(curr, num_available, num_unclosed):
    """
    Helper function for the main function generate_parens

    """
    # If there are no available opening parenthesis, we must
    # close all of them, thus we simply concatenate that amount
    # of closed brackets
    if num_available == 0:
        return [curr + ')' * num_unclosed]
    # if the number of unclosed parenthesis are 0, then we can deduce
    # that we can only add an opening bracket
    elif num_unclosed == 0:
        return generate_parens_helper(curr + '(', num_available - 1,
                                      num_unclosed + 1)
    # if we don't have any unclosed parenthesis, we can add either an opening
    # or closing bracket
    return generate_parens_helper(curr + '(', num_available - 1,
           num_unclosed + 1) + generate_parens_helper(curr + ')', num_available,
        num_unclosed - 1)


def length_of_longest_substring(s: str) -> int:
    """
    Given a string, find the length of the longest
    substring without repeating characters.

    """
    pass

    # start = 0
    # max_length = 0
    # used_char = {}
    #
    #
    # for i in range(len(s)):


def search_insert(nums: List[int], target: int) -> int:
    """
    Given a sorted array and a target value,
    return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

    """
    try:
        return nums.index(target)
    except:
        try:
            i = 0
            while nums[i] < target:
                i += 1
            return i
        except:
            return len(nums)


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Given two sorted integer arrays nums1 and nums2,
    merge nums2 into nums1 as one sorted array.

    Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    Output: [1,2,2,3,5,6]

    """
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            nums1.insert(i+1, nums2[j])
            print(nums1)
            i += 1
            j += 1
        else:
            i += 1


def is_row_valid(board):
    # Checking if the rows are valid
    for row in board:
        lst_1 = []
        for val in row:
            if val.isdigit():
                lst_1.append(val)
            if len(lst_1) != len(set(lst_1)):
                return False
    return True


def is_col_valid(board):
    # Checking if the columns are valid
    # i = 0
    # j = 0
    # lst = []
    #
    # if (board[i][j]).isdigit():
    #     lst.append(board[i][j])
    #     i += 1
    #     if len(lst) != len(set(lst)):
    #         return False
    #     else:
    #         lst.clear()
    #         j += 1

    return is_row_valid(zip(*board))


def is_square_valid(board):
    # Checking if the 3x3 boxes are valid
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3)
                      for y in range(j, j + 3)]
            res = [i for i in square if i != "."]
            if len(set(res)) != len(res):
                return False
    return True


def is_valid_sudoku(board: List[List[str]]) -> bool:
    """
    Input:
        [
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
    Output: true
    """
    return is_row_valid(board) and is_col_valid(board) and is_square_valid(board)


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def swap(i, j, nums):
        new_nums = list(nums)
        new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
        return new_nums


    result = [nums]

    for i in range(len(nums) - 1):
        for one in result[:]:
            for j in range(i + 1, len(nums)):
                print("one:", one)
                result.append(swap(i, j, one))

    return result


# def permute(nums: List[int]) -> List[List[int]]:
#     """
#     Given a collection of distinct integers, return all possible permutations.
#     >>> permute([1, 2, 3])
#     [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
#
#     """
#     lst = []
#     for n in nums:
#         lst.extend(permute_helper(nums, n))
#     for o in lst:
#         lst.extend(permute_helper(o, 1))
#
#     return lst
#
#
#
# def permute_helper(nums: List[int], num: int) -> List[List[int]]:
#     """
#     Given a num in list of nums, return all possible permutations created
#     by swapping the num within the list.
#     >>> permute_helper([1, 2, 3], 1)
#     [[1, 2, 3], [2, 1, 3], [2, 3, 1]]
#     """
#     nums_copy = nums[:]
#     lst = []
#
#     for n in nums[nums.index(num):]:
#         print("n: ", n)
#         # nums_copy[nums_copy.index(num)], nums_copy[nums_copy.index(n)] = \
#         #     nums_copy[nums_copy.index(n)], nums_copy[nums_copy.index(num)]
#         # print("nums_copy.index(num): ", nums_copy.index(num))
#         # print("nums_copy[nums_copy.index(n)]: ", nums_copy[nums_copy.index(n)])
#         # print("nums_copy: ", nums_copy)
#         lst.append(swap(nums_copy.index(num), nums_copy.index(n), nums_copy))
#         print("lst: ", lst)
#     for n in nums[:nums.index(num)]:
#         lst.append(swap(nums_copy.index(num), nums_copy.index(n), nums_copy))
#     # if nums.index(num) > 0:
#     #     for n in nums[:nums.index(num)]:
#     #         lst.append(swap(nums_copy.index(num), nums_copy.index(n), nums_copy)
#     #                    )
#     return lst
#
#
# def swap(i, j, nums):
#     """
#     Given two indices, swaps the elements associated with them in list <nums>
#
#     """
#     new_nums = list(nums)
#     new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
#     return new_nums


# The following solution makes use of an algorithm known as "backtracking",
# which basically works by looking down a particular solution set, and if a
# condition is not met, breaks out of this set and tries another value and
# continues down this solution set, making it a more efficient algorithm than
# the naive approach of looking at all particular solutions.

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Given a set of candidate numbers (candidates) (without duplicates) and a
    target number (target), find all unique combinations in candidates where the
    candidate numbers sums to target. The same repeated number may be chosen
    from candidates unlimited number of times.

    >>> combination_sum([2, 3, 6, 7], 7)
    [[7], [2, 2, 3]]
    >>> combination_sum([2, 3, 5], 8)
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    """
    results = []

    if len(candidates) == 0:
        return results
    # This code tests for the edge case of the candidates list being empty, if
    # not we sort the list

    candidates_copy = candidates.copy()
    candidates_copy.sort()

    combination = []

    to_find_combination(results, combination, candidates_copy, target, 0)

    return results


def to_find_combination(results: List[List[int]], combination: List[int],
                        candidates: List[int], target: int, start_index: int):

    if target == 0:
        combination_copy_2 = combination.copy()
        print("Combination: ", combination_copy_2)
        results.append(combination_copy_2)
        return results
    # Target is essentially a remainder variable that keeps track of the
    # remaining value to the target with each consecutive cycle (ex. with the
    # value 2, target becomes 5, etc.)

    i = start_index
    # starts at 0 in the beginning, and target is set to 7
    for j in range(i, len(candidates)):
        if candidates[j] > target:
            break
        # What we are saying here is that if a value is encountered that is
        # greater than the target, "break" out of the loop and go up one
        # level and keep searching
        print("i: ", i)
        print("j: ", j)
        print("candidates: ", candidates)
        print("target: ", target)
        print("combination: ", combination)
        # If the above condition is not met, we recursively call the function
        # once more, but with whichever candidate value that we encountered
        # subtracted from the target
        combination.append(candidates[j])
        to_find_combination(results, combination, candidates,
                            target-candidates[j], j)
        combination.remove(combination[-1])


if __name__ == '__main__':
    # board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
    #          [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #          ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    #
    #          [".", ".", ".", "5", "6", ".", ".", ".", "."],
    #          ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    #          [".", ".", ".", "7", ".", ".", ".", ".", "."],
    #
    #          [".", ".", ".", "5", ".", ".", ".", ".", "."],
    #          [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #          [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    #
    # print(is_valid_sudoku(board))
    print(combination_sum([2, 3, 6, 7], 7))
