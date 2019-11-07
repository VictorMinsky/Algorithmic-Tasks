# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a, b = map(str, input().split())
    try:
        print(int(a) // int(b))
    except Exception as e:
        print("Error Code:", e)
