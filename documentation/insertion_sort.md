## Insertion Sort

- Sort array partially i.e. in parts.
    - Sort till index 1.
    - Then sort till index 2.
    - Then sort till index 3.
    - And similarly, sort till last index.<br/>
<br/>

- Unsorted array e.g. $[5, 3, 4, 1, 2]$

- Steps:
    - for every index, put the element at that index at the correct index of LHS (left hand side).
    - If $nums[j] < nums[j - 1]$, swap the items.

- Example:
    > $nums = [5, 3, 4, 1, 2]$<br/>
    >
    > First pass: *i = 0* and j = i + 1 to 1 (not including 0) i.e., j = 1 to 1<br/>
    >> *j = 1*<br/>
    >> nums[j] = nums [1] = 3 and nums[j - 1] = nums[0] = 5<br/>
    >> nums[1] (3) < nums[0] (5), hence swap nums[1] and nums[0]<br/>
    >> $nums = [3, 5, 4, 1, 2]$<br/>
    >
    > Second pass: *i = 1* and j = i + 1 to 1 i.e., j = 2 to 1<br/>
    >> *j = 2*<br/>
    >> nums[j] = nums[2] = 4 and nums[j - 1] = nums[1] = 5<br/>
    >> nums[2] (4) < nums[1] (5), hence swap nums[2] and nums[1]<br/>
    >> $nums = [3, 4, 5, 1, 2]$<br/><br/>
    >> *j = 1*<br/>
    >> nums[j] = nums[1] = 4 and nums[j - 1] = nums[0] = 3<br/>
    >> nums[1] (4) > nums[0] (3), do nothing<br/>
    >> $nums = [3, 4, 5, 1, 2]$<br/>
    >
    >Third pass: *i = 2* and j = i + 1 to 1 i.e., j = 3 to 1<br/>
    >> *j = 3*<br/>
    >> nums[j] = nums[3] = 1 and nums[j - 1] = nums[2] = 5<br/>
    >> nums[3] (1) < nums[2] (5), swap nums[3] and nums[2]<br/>
    >> $nums = [3, 4, 1, 5, 2]$<br/><br/>
    >> *j = 2*<br/>
    >> nums[j] = nums[2] = 1 and nums[j - 1] = nums[1] = 4<br/>
    >> nums[2] (1) < nums[1] (4), swap nums[2] and nums[1]<br/>
    >> $nums = [3, 1, 4, 5, 2]$<br/><br/>
    >> *j = 1*<br/>
    >> nums[j] = nums[1] = 1 and nums[j - 1] = nums[0] = 3<br/>
    >> nums[1] (1) < nums[0] (3), swap nums[1] and nums[0]<br/>
    >> $nums = [1, 3, 4, 5, 2]$<br/>
    >
    > Fourth pass: *i = 3* and j = i + 1 to 1 i.e., j = 4 to 1<br/>
    >> *j = 4*<br/>
    >> nums[j] = nums[4] = 2 and nums[j - 1] = nums[3] = 5<br/>
    >> nums[4] (2) < nums[3] (5), swap nums[4] and nums[3]<br/>
    >> $nums = [1, 3, 4, 2, 5]$<br/><br/>
    >> *j = 3*<br/>
    >> nums[j] = nums[3] = 2 and nums[j - 1] = nums[2] = 4<br/>
    >> nums[3] (2) < nums[2] (4), swap nums[3] and nums[2]<br/>
    >> $nums = [1, 3, 2, 4, 5]$<br/><br/>
    >> *j = 2*<br/>
    >> nums[j] = nums[2] = 2 and nums[j - 1] = nums[1] = 3<br/>
    >> nums[2] (2) < nums[1] (3), swap nums[2] and nums[1]<br/>
    >> $nums = [1, 2, 3, 4, 5]$<br/><br/>
    >> *j = 1*<br/>
    >> nums[j] = nums[1] = 2 and nums[j - 1] = nums[0] = 1<br/>
    >> nums[1] (2) > nums[0] (1), do nothing<br/>
    >> $nums = [1, 2, 3, 4, 5]$<br/>

- Complexity Analysis
    > Worst Case: $O(n^{2})$
    >> In first pass, one comparison<br/>
    >> In second pass, two comparisons<br/>
    >> In third pass, three comparisons<br/> 
    >> Similarly, in final pass, n-1 comparisons<br/>
    >> 1 + 2 + 3 + ... + n - 1  = (n * (n - 1)) // 2
    >
    > Best Case: $O(n)$
    >> Only outer loop will run till last, as array is already sorted. Hence, only 1 comparison at each stage.