"""
Create a function args_count, that returns the count of passed arguments

args_count(1, 2, 3) -> 3
args_count(1, 2, 3, 10) -> 4
"""



# Create a function args_count, that returns count of passed arguments
def args_count(*args, **kwargs):
    return len(kwargs) + len(args)
