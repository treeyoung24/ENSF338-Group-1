Exercise 2/1:

1. One aspect that makes interpolation search better than binary search is that by dividing the data to find a better position then searching amongst them, a uniformly distributed data would greatly benefit from using interpolation search. Another aspect that makes interpolation more beneficial than binary search is that it performs better if the dataset is dynamic.

2. When the dataset is not uniformly distributed, then interpolation will not perform as well, becuase the formula used to estimate the position of the item could give inaccurate positions, causing it to take more time to search the dataset, decreasing the performance of the search.

3. The part of the code that would have to be modified is this line: pos = low + int(((float(high - low) / (arr[high] - arr[low])) \* (x - arr[low]))). This formula would be changed to something that would fit the new distribution.

Exercise 2/2:

4. Linear search becomes the only option left for saerch data when the dataset is not sorted. Binary and interpolation search requires the data to be sorted, so unsorted data cannot be searched through using those methods.

5. Linear search will outperform both binary and interpolation search when the item being searched for is right at the beginning or near the beginning of the dataset. Becuase linear search starts from the first value and moves on to each successive item until the match. Compared to binary and interpolation search that divides the dataset, linear will perform much better if the item trying to be found is located near the beginning of the dataset.

6. To solve this issue, one idea that could be implemented is that the first few values could be passed to the binary and interpolation search, so if the item matches the first few values, linear search can be used instead to give a better performance overall.
