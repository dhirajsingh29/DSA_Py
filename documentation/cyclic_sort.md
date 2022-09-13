## Cyclic Sort

### **$Note$: For any question, if array contains number in range 1 to N => use cyclic sort. Range can also be 0 to N - 1 or anything, but it should be continuous**

- Unsorted array e.g. $[3, 5, 2, 1, 4]$

- Steps:
    - Move each element to its correct index, which is number - 1. [This will work only if above property hold. It is important.]
    - take the element at index $0$, and move the element at index $0$ to its correct index by swapping it with element at its index, i.e.,
    $nums[nums[i] - 1] = nums[i]$.
    - once, 0th index has element which should be there, move the loop to index $1$.
    - repeat above steps, till loop exhausts.

- Complexity:
    - Worst Case: $O(n)$
