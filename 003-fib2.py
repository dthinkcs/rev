# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    curr = t1
    nxt = t2
    for _ in range(n - 1):
        nxt_nxt = curr + nxt*nxt
        curr = nxt
        nxt = nxt_nxt
    return curr
        
