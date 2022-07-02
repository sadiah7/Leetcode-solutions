**Java Solution Explained | Greedy Approach Explained | Optimal Solution
Intuition :
Imagine the cake having only horizontal cuts and find out the maximum height of the cake you can get. Now imagine that piece of cake having vertical cuts and find out the maximum width of the cake you can get.
Algorithm : **
​
*Sort both the array to get the cuts in sequential way
Find the max Height
Find the max Width
Return the area as (max Height  max Width)
Please upvote if this solution helps you to learn better. Thanks in Advance.*
​
```
class Solution {
public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
// sort both cuts array
Arrays.sort(horizontalCuts);
Arrays.sort(verticalCuts);
// find the cake with maximum height and maximum width after cuts
long maxHeight = 0;
long maxWidth = 0;
int prev = 0;
for(int index = 0;index < horizontalCuts.length;index++){
maxHeight = Math.max(maxHeight, horizontalCuts[index] - prev);
prev = horizontalCuts[index];
}
maxHeight = Math.max(maxHeight, h - prev);
prev = 0;
for(int index = 0;index < verticalCuts.length;index++){
maxWidth = Math.max(maxWidth, verticalCuts[index] - prev);
prev = verticalCuts[index];
}
maxWidth = Math.max(maxWidth, w - prev);
return (int)((maxHeight * maxWidth) % 1000000007);
}
}
```