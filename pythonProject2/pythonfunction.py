def tri_recursion(k):
    if k>0:
     result=k+tri_recursion(k-1)
    else:
        result=0
    print(result)
    return result


tri_recursion(4)