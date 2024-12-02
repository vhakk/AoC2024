# Part 1
with open('reports.txt', 'r') as file:
    reports = [line.strip() for line in file.readlines()]

    safeCount = 0

    def isSafe(levels):
        nums = [int(x) for x in levels.split()]
        isIncreasing = None

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]

            if abs(diff) < 1 or abs(diff) > 3:
                return False

            if isIncreasing is None:
                isIncreasing = diff > 0
            elif (diff > 0) != isIncreasing:
                return False

            if diff == 0:
                return False
        return True

    safeCount = sum(1 for report in reports if isSafe(report))
    print(f"number of safe reports: {safeCount}")

    # Part 2
    def isSafeWithDampener(levels):
        nums = [int(x) for x in levels.split()]

        if isSafe(levels):
            return True

        for i in range(len(nums)):
            dampened = nums[:i] + nums[i+1:]
            dampened_str = ' '.join(map(str, dampened))
            if isSafe(dampened_str):
                return True
        return False

    safeCountWithDampener = sum(1 for report in reports if isSafeWithDampener(report))
    print(f"number of safe reports with dampener: {safeCountWithDampener}")