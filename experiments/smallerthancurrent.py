from typing import List


def smallerNumbersThanCurrent_slow(nums: List[int]) -> List[int]:
    output = []
    for a in nums:
        counter = 0
        for b in nums:
            if a > b:
                counter += 1
        output.append(counter)
    return output


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    counts = [0 for i in range(101)]
    for num in nums:
        counts[num] += 1
    sums = []
    summa = 0
    for number in counts:
        sums.append(summa)
        summa = summa + number
    output = []
    for x in nums:
        output.append(sums[x])
    return output


def counting_sort(nums):
    counts = [0 for i in range(100)]
    for num in nums:
        counts[num] += 1
    output = []
    for value, count in enumerate(counts):
        while count > 0:
            output.append(value)
            count -= 1
    return output
