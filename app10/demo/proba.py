    
A = [3, 8, 9, 7, 6]

K = 1

result = []
for i in range(len(A)):
    
    shift = -K+i
    print('shift :', shift)
    print('len_A :', len(A))
    if abs(shift) <= len(A):
        print('if goes')
        pass
    else: 
        print('else goes')
        shift = shift % len(A)
    
    result.append(A[shift])

print(result)
    

# Dominator
// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
// 3,4,3,2,3,-1,3,3
// 4,2,3,3,-1,3,3,3

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int dom = -1;
        int idx = 0;
        for (int i = 1; i < A.length; i=i+2) {
            if (A[i] != A[i-1]) {
                A[i] = A[i-1] = 0;
                // System.out.println("If: " + Arrays.toString(A));
            } else dom = A[i];
        }
        for (int j = 0; j < A.length; j++) {
            if (A[j] == dom) idx = j;
        }
        return idx;
    }
}