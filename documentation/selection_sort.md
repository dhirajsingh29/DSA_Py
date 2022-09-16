## Selection Sort

- Unsorted array e.g. [4, 5, 1, 2, 3]

- Steps:
    - In every pass, take the largest (in case of ascending sort) or the smallest (in case of descending sort).
    - If nums[j] > nums[j - 1], then max = nums[j]. Do this untill all elements are compared.
    - The swap the max element with the last index element of that pass.

- It is not a stable sort.

- Complexity:
    > Worst case / Best case:<br/>
    >> First pass: n - 1 comparisions<br/>
    >> Second pass: n - 2 comparisions<br/>
    >> Third pass: n - 3 comparisions<br/>
    >> Similarly, at last we will have to make 0 comparisions.<br/>
    >> Total comparisions = 0 + 1 + 2 + 3 + .... + (n - 1) = (n * (n - 1)) // 2<br/>
    >> Hence, $O(n^{2})$