## Binary Search

- Array should be sorted (either increasing or decreasing)

- Steps:
    - Find the middle element [start + (end - start) / 2]
    - If target_element > middle_element then search in the right part of array after middle_element else search left part
    - If middle_element == target_element then element found
    - If start > end, target_element not found<br/><br/>

- Why mid = start + (end - start ) / 2 and not (start + end) / 2?
    > If we take start and end as very large numbers, it is possible for the sum start + end to exceed the maximun allowed value for integer. In that case our code will throw some exception.<br/><br/>
    > Every language, C#, Python, Java etc. has some higher limit on integer value.<br/><br/>
    > Hence, to overcome that integer value exceeding its maximum allowed value, we go for start + (end - start) / 2.

- Example 1:
    > nums = [2, 4, 6, 9, 11, 13, 14, 19, 20, 27, 38, 40]<br/>
    > target_element = 38<br/>
    > <br/>
    > First iteration:<br/>
    >> start = 0, end = len(nums) - 1 = 11<br/>
    >> mid = (0 + (11 - 0) // 2) = 5; hence, middle_element = nums[5] = 13<br/>
    >> target_element (38) > middle_element (13); hence, start = mid + 1 = 5 + 1 = 6<br/>
    >
    > Second iteration:<br/>
    >> start = 6, end = 11<br/>
    >> mid = (6 + (11 - 6) // 2) = 8; henmce, middle_element = nums[8] = 20<br/>
    >> target_element (38) > middle_element (20); hence, start = mid + 1 = 8 + 1 = 9<br/>
    >
    > Third ietration:<br/>
    >> start = 9, end = 11<br/>
    >> mid = (9 + (11 - 9) // 2) = 10; hence, middle_element = nums[10] = 38<br/>
    >> target_element (38) == middle_element (38); hence, element found at index 10

- Example 2:
    > nums = [2, 4, 6, 9, 11, 13, 14, 19, 20, 27, 38, 40]<br/>
    > target_element = 14<br/>
    > <br/>
    > First iteration:<br/>
    >> start = 0, end = len(nums) - 1 = 11<br/>
    >> mid = (0 + (11 - 0) // 2) = 5; hence, middle_element = nums[5] = 13<br/>
    >> target_element (14) > middle_element (13); hence, start = mid + 1 = 5 + 1 = 6<br/>
    >
    > Second iteration:<br/>
    >> start = 6, end = 11<br/>
    >> mid = (6 + (11 - 6) // 2) = 8; henmce, middle_element = nums[8] = 20<br/>
    >> target_element (14) < middle_element (20); hence, end = mid - 1 = 8 - 1 = 7<br/>
    >
    > Third ietration:<br/>
    >> start = 6, end = 7<br/>
    >> mid = (6 + (7 - 6) // 2) = 6; hence, middle_element = nums[6] = 14<br/>
    >> target_element (14) == middle_element (14); hence, element found at index 6

- Time Complexity:
    > Best Case:<br/>
    >> target_element found as first middle element<br/>
    >> Hence, O(1)
    >
    > Worst Case:<br/>
    >> At Level = 0, we have N elements i.e. N/2<sup>0</sup><br/>
    >> At Level = 1, we have N/2 elemets i.e. N/2<sup>1</sup><br/>
    >> At Level = 2, we have N/4 elements i.e. N/2<sup>2</sup><br/>
    >> At Level = 3, we have N/8 elements i.e. N/2<sup>3</sup><br/>
    >> Similarly, when only one block is left in search with final element say at Level = k, we will have 1 element only i.e. N/2<sup>k</sup><br/>
    >>
    >> 1 = N/$2^{k}$<br/>
    >> N = $2^{k}$<br/>
    >> log N = log ($2^{k}$)<br/>
    >> log N = k log 2<br/>
    >> k = log N/log 2<br/>
    >> k = $log_2N$<br/>
    >> Total number of comparisons in worst case is log(N); where N is the size of array<br/>
    >> Hence, O(log N)