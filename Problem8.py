##The four adjacent digits in the 1000-digit number that have
##the greatest product are 9 × 9 × 8 × 9 = 5832.
##
##Find the thirteen adjacent digits in the 1000-digit number that
##have the greatest product. What is the value of this product?


import time

s = time.time()
n =str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)

currentLargest = 0
ndx = []

#indicates the position of the group of numbers being considered
for i in range(0,len(n) - 12):

    #resets the values
    adjacentProduct = 1
    ndxTemp = []

    # multiplies the numbers being considered, stores the numbers and their product
    for j in range(i, i + 13):
        adjacentProduct = (int(n[j]) * adjacentProduct)
        ndxTemp.append(n[j])
        
    #checks at the end to see if it found a larger sequence, stores the sequence and its product
    if adjacentProduct > currentLargest:
        currentLargest = adjacentProduct
        ndx = ndxTemp
        pos = i


#changes the list into a string of the       
joiner = ' x '
ndx = joiner.join(ndx)

#prints in the form the question was given in
print('The thirteen adjacent digits in the 1000-digit number that have the greatest product are ' + ndx + ' = ' + str(currentLargest) + '.')
print('\nFound starting at digit: ' + str(pos))
print(time.time()-s)

##Non-functional first attempt: was going to divide by the previous digit as it
##multiplied by the next digit
##essentialy moving through the sequence as the product of 13 numbers and storing the largest value it found
##for i in range(0,13):
##    adjacentProduct = int(n[i]) * adjacentProduct
##
##for i in range(14, len(n)-12):
##    adjacentProduct = adjacentProduct * int(n[i]) / int(n[i-13])
##    if ValueError: adjacentProduct = ?
##    if adjacentProduct > currentLargest: currentLargest = adjacentProduct
##print(currentLargest)
