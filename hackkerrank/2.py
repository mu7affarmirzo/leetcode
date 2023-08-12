def findSum(numbers, queries):
    n = len(numbers)
    prefix_sum = [0]
    zero_count = [0]

    # Calculate cumulative sum and zero count
    for num in numbers:
        prefix_sum.append(prefix_sum[-1] + num)
        zero_count.append(zero_count[-1] + (num == 0))

    arr = []

    for q in queries:
        I, r, x = q
        sum_result = prefix_sum[r] - prefix_sum[I - 1] + (zero_count[r] - zero_count[I - 1]) * x
        arr.append(sum_result)

    return arr

# Example usage
numbers = [20, 30, 0, 10]
queries = [(1, 3, 10)]
print(findSum(numbers, queries))  # Output: [60]
