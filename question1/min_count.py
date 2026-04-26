# Algorithm to solve question 1:
# Given min heap H with n numbers, int k, and int x
# - finds if there's at least k numbers smaller than x, runs in O(k) time (doesn't depend on n)

import heapq

# main algorithm, doesn't have n as input
def has_k_smaller(H, x, k):
    count = 0

    # recursive depth first search to explore the heap/tree
    def dfs(i):
        nonlocal count
        # base cases: found enough > x, out of bounds, or node too large
        if count >= k or i >= len(H) or H[i] >= x:
            return
        
        count += 1      # made it past, add to count

        # recursively check next nodes
        dfs(2 * i + 1)  # left child
        dfs(2 * 1 + 2)  # right child

    dfs(0)      # start at root

    return count >= k

print("--------------\nFinding k numbers smaller than x in heap H")

# run through a couple examples to test

ex_H_false = [11, 25, 34, 65, 84, 7, 3, 49]
ex_H_true = [11, 25, 34, 65, 8, 7, 3, 4]
ex_k = 3
print("k = " + str(ex_k))
ex_x = 10
print("x = " + str(ex_x) + "\n")

print("example false data: " + str(ex_H_false))
heapq.heapify(ex_H_false)
print("data sorted as min-heap: " + str(ex_H_false))
ex_ret_false = has_k_smaller(ex_H_false, ex_x, ex_k)
print(">> has_k_smaller() run on example false heap\nresult = " + str(ex_ret_false))

print("")

print("example true data: " + str(ex_H_true))
heapq.heapify(ex_H_true)
print("data sorted as min-heap: " + str(ex_H_true))
ex_ret_true = has_k_smaller(ex_H_true, ex_x, ex_k)
print(">> has_k_smaller() run on example true heap\nresult = " + str(ex_ret_true))

print("-------------")