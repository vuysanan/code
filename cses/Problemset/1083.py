// Problem: Task
// Platform: cses
// Language: unknown
// Verdict: ACCEPTED
// URL: https://cses.fi/problemset/result/19394005/
// Solved on: 2026-11-19T01:47:26.459Z

n = int(input())numbers = list(map(int, input().split())) expectedInputSum = n * (n + 1) // 2actualInputSum = sum(numbers)missingNumber = expectedInputSum - actualInputSumprint(missingNumber)