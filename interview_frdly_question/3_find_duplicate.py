nums = [1, 2, 3, 4, 5, 1, 2, 6, 7]
def find_duplicates(nums):
    seen = set()
    dups = set()
    for n in nums:
        if n in seen:
            dups.add(n)
        seen.add(n)
    return list(dups)
print(find_duplicates(nums))
