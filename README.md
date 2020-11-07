The algorithm finds distance between closest pair of points
in the given n points. Here, I have generated 100 random pairs and found the
shortest distance among those .
The Approach I used here is Divide and Conquer.
The points are sorted based on X coordinates  and then based on Y coordinates separately, and  by applying divide and conquer approach, minimum distance is obtained  using recursion .
Initially, we split the total no of points present into two halves by finding
the median . We find the shortest distance between the points in the left half dl and also in the right half ,dr. Let d be the min(dl , dr). The minimum of these two distances(dl ,dr )  i.e d can be the shortest distance, but we should also consider the fact the there might be  pairs such that one pair lies on right side and the other lies on left side .
Hence ,  Closest points can lie on different sides of partition.
This case handled by forming a strip of points whose X coordinates distance is less than closest pair distance from mid-point's x-coordinates . Points sorted based on Y co-ordinates are used in this step to reduce sorting time.
Closest pair distance is found in the strip of points.
min(closest pair in dis, closest in strip) would be the final answer.
Time complexity: O(n * log n)
