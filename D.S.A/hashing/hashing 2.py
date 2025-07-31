n = [5, 3, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# Recursively count how many times `target` appears in list `lst`
def count_occurrences(lst, target):
    if not lst:
        return 0
    if lst[0] == target:
        return 1 + count_occurrences(lst[1:], target)
    else:
        return count_occurrences(lst[1:], target)

# Recursively iterate over `m` and print counts from `n`
def process_list(m_list, n_list):
    if not m_list:
        return
    count = count_occurrences(n_list, m_list[0])
    print(count)
    process_list(m_list[1:], n_list)

# Run the recursive function
process_list(m, n)
