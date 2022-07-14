def fibonnaci(n) -> None:
    if n == 0 :
        return 0
    if n == 1 or n == 2:
        return 1    

    return fibonnaci(n-1) + fibonnaci(n-2)


n = 5
for i in range(n):
    print(fibonnaci(i))
