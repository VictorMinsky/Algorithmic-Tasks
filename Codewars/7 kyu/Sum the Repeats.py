"""
Write a function that takes a list comprised of other lists of integers and returns the sum of all numbers that appear in two or more lists in the input list. Now that might have sounded confusing, it isn't:

repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]])
>>> sum of [2, 8]
return 10

repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]])
>>> sum of []
return 0

repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]])
sum of [1,8]
return 9
"""



def repeat_sum(l):
    all_lists = set([x for b in l for x in b])
    ans = 0
    for i in all_lists:
        flag = 0
        for z in l:
            if i in z:
                flag += 1
            if flag == 2:
                ans += i
                break
    return ans
