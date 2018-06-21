def cutRod(price_list ,size, c):
    val = [0 for x in range(size+1)]

    #Define the minimum value to stop undeflow.
    INT_MIN = -32767

    for i in range(1,size+1):
        max_val = INT_MIN

        for j in range(i):
            if max_val < price_list[j] + val[i-j-1] - c:
                max_val = price_list[j] + val[i-j-1] - c
                optlen[i] = j+1

        val[i] = max_val

    #print optlen[size]
    print val
    return val[size]


def PrintRodCutOptimalSolution(n):
    while n>0:
        print optlen[n]
        n = n - optlen[n]


price_list = [3, 4.5, 8, 9, 10, 17, 17, 20]
cost_to_cut = 1
size = len(price_list)
optlen = [0 for x in range(size+1)]
if cost_to_cut == 0:
    print("Maximum Profit is " + str(cutRod(price_list, size, cost_to_cut)))
else:
    print("Maximum Profit is " + str(cutRod(price_list, size, cost_to_cut) + cost_to_cut))

print "Length of pieces:"
PrintRodCutOptimalSolution(size)



