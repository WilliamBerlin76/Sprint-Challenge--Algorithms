#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    n^3 / n^2 = n, so a is always incremented by the same fraction of n*n*n regardless of the input size, so the time complexity is linear

b) O(n^2)
    nested loop requires an additional loop for each increment of i. As the input increases, the time increases at a faster rate


c) O(n)
    single recursion call that decrements the input by one until base case is met

## Exercise II
    Start by dropping an egg at the middle floor.
    if it breaks:
        test if the egg breaks at a drop from the middle between the middle and bottom floor
    if it doesnt break:
        test if the egg breakes in the middle between the middle and top floor
    
    continue the above steps untill the lowest floor is found where the egg breaks, this floor is 'f'
        halves of the bulding that are 'halved' out, will not be tested again

    
    Time complexity of above: O(log n)

