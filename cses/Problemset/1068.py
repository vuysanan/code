// Problem: Task
// Platform: cses
// Language: unknown
// Verdict: ACCEPTED
// URL: https://cses.fi/problemset/result/19393936/
// Solved on: 2026-11-19T01:10:04.584Z

n = int(input()) result = [n] while n != 1:    if n % 2 == 0:        n = n // 2    else:        n = 3 * n + 1    result.append(n) print(*result)