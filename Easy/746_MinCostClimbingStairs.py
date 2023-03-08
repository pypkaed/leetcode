def minCostClimbingStairs(cost):
    min_cost = [0, cost[0]]
    for i in range(2, len(cost) + 1):
        min_cost.append(min(min_cost[i-1], min_cost[i-2]) + cost[i-1])
    return min(min_cost[len(cost)-1], min_cost[len(cost)])


print(minCostClimbingStairs([10, 15, 20]))
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
