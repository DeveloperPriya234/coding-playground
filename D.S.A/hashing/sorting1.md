#SORTING

when we write any elements in sequence like ascending and descending order its called a sorting
its always write in o(n**2)
1.[3,4,2,1,5] 
ascending = 1,2,3,4,5
descending = 5,4,3,2,1

#BUBBLE SORT
[4,1,5,2,3]

(n-1)iteration

adj .element compare

larger element pushing in last  using swap

first iteration:

[4,1,5,2,3]
now compare 4,1 and larger element push in last 
so;
1,4,5,2,3
1,4,2,5,3
1,4,2,3,5
2nd iteration
1,2,4,3,5
1,2,3,4,5

#[4,1,2,3,5]
n-1 iteration loop(5-1) = 4

1st iteration:i = 0== 4
4,1,5,2,3
1,4,5,2,3
1,4,2,5,3
1,4,2,3,5
2nd iteration:i = 1 == 3
1,4,2,3,5
1,4,2,3,5
1,2,4,3,5
1,2,3,4,5
3rd iteration:i = 2== 2
1,2,3,4,5
1,2,3,4,5,
1,2,3,4,5
4th iteration:i = 3==1
1,2,3,4,5
1,2,3,4,5
