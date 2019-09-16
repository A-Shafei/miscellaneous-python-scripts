def tribonacci(signature, n):
    for i in range(0, n-3):
    	signature.append(signature[i]+signature[i+1]+signature[i+2])

    print(signature)






tribonacci([1,2,3], 10)
