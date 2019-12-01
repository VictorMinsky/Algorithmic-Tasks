"""
Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, function should returns 0

Examples

sequenceSum(2,2,2) === 2
sequenceSum(2,6,2) === 12 // 2 + 4 + 6
sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
sequenceSum(1,5,3) === 5 // 1 + 4
This is the first kata in the series:

1) Sum of a sequence (this kata)
2) Sum of a Sequence [Hard-Core Version]
"""



def sequence_sum(begin_number, end_number, step):
    n = (end_number - begin_number) // step + 1
    if (n - 1) * step + begin_number > end_number:
        n -= 1
    end_number = begin_number + step * (n - 1)
    ans = (begin_number + end_number) * n // 2
    return ans if ans >= 0 else 0
