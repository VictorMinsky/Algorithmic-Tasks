"""
Story
The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!

Kata Task
How many deaf rats are there?

Legend
P = The Pied Piper
O~ = Rat going left
~O = Rat going right
Example
ex1 ~O~O~O~O P has 0 deaf rats
ex2 P O~ O~ ~O O~ has 1 deaf rat
ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats
Series
The deaf rats of Hamelin (2D)
"""



def count_deaf_rats(town):
    town = town.replace(' ', '')
    P_pos = town.count('~', 0, town.index('P'))
    town = town.replace('P', '')
    ans = 0
    for index, rat in enumerate([town[i:i + 2] for i in range(0, len(town), 2)]):
        if index < P_pos:
            if rat != '~O':
                ans += 1
        elif index >= P_pos:
            if rat != 'O~':
                ans += 1
    return ans
