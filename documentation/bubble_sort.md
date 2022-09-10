## Bubble Sort

- Also know as Sinking sort or Exchange sort.

- Unsorted array e.g. [3, 1, 5, 4, 2]

- Steps:
    - In every pass, compare the adjacent items.
    - If nums[j] < nums[j - 1], swap the items.
    - At the end of every pass, largest element of that pass will be positioned at its correct position.<br/><br/>

- Example 1:
    > **nums = [3, 1, 5, 4, 2]**<br/>
    >
    > First pass: i = 0 and j = 1 to n - 1, i.e., i = 1 to 4<br/>
    >> *j = 1*<br/>
    >> nums[j] = nums[1] = 1 and nums[j - 1] = nums[0] = 3<br/>
    >> nums[1] (1) < nums[0] (3), hence swap nums[1] and nums[0]<br/>
    >> *nums = [1, 3, 5, 4, 2]*<br/><br/>
    >> *j = 2*<br/>
    >> nums[j] = nums[2] = 5 and nums[j - 1] = nums[1] = 3<br/>
    >> nums[2] (5) > nums[1] (3), do nothing<br/>
    >> *nums = [1, 3, 5, 4, 2]*<br/><br/>
    >> *j = 3*<br/>
    >> nums[j] = nums[3] = 4 and nums[j - 1] = nums[2] = 5<br/>
    >> nums[3] (4) < nums[2] (5), hence swap nums[3] and nums[2]<br/>
    >> *nums = [1, 3, 4, 5, 2]*<br/><br/>
    >> *j = 4*<br/>
    >> nums[j] = nums[4] = 2 and nums[j - 1] = nums[3] = 5<br/>
    >> nums[4] (2) < nums[3] (5), hence swap nums[4] and nums[3]<br/>
    >> *nums = [1, 3, 4, 2, 5]*<br/>
    >
    > Second pass: i = 1 and j = 1 to n - 2, i.e. i = 1 to 3<br/>
    >> *j = 1*<br/>
    >> nums[j] = nums[1] = 3 and nums[j - 1] = nums[0] = 1<br/>
    >> nums[1] (3) > nums[0] (1), do nothing<br/>
    >> *nums = [1, 3, 4, 2, 5]*<br/><br/>
    >> *j = 2*<br/>
    >> nums[j] = nums[2] = 4 and nums[j - 1] = nums[1] = 3<br/>
    >> nums[2] (4) > nums[1] (3), do nothing<br/>
    >> *nums = [1, 3, 4, 2, 5]*<br/><br/>
    >> *j = 3*<br/>
    >> nums[j] = nums[3] = 2 and nums[j - 1] = nums[2] = 4<br/>
    >> nums[3] (2) < nums[2] (4), swap nums[3] and nums[2]<br/>
    >> *nums = [1, 3, 2, 4, 5]*<br/>
    >
    > Third pass: i = 2 and j = 1 to n - 3, i.e. j = 1 to 2<br/>
    >> *j = 1*<br/>
    >> nums[j] = nums[1] = 3 and nums[j - 1] = nums[0] = 1<br/>
    >> nums[1] (3) > nums[0] (1), do nothing<br/>
    >> *nums = [1, 3, 2, 4, 5]*<br/><br/>
    >> *j = 2*<br/>
    >> nums[j] = nums[2] = 2 and nums[j - 1] = nums[1] = 3<br/>
    >> nums[2] (2) < nums[1] (3), swap nums[2] and nums[1]<br/>
    >> *nums = [1, 2, 3, 4, 5]*<br/>

- Time Complexity:
