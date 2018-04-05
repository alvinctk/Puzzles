# speed = O(n)
def seq_nth_term(n):
    if n:
        term = n
        for x in range(1, n+1):
            term = term * x
        return term
    else:
        return 0

if __name__ == "__main__":
    for n in range(10):
        print("f({}) = {}".format(n, seq_nth_term(n)))
