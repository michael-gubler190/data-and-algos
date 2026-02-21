# Algorithms & Data Structures Practice

## Overview

This repository contains my implementations of fundamental algorithmic problems and common data structure patterns.

The goal of this repository is not just to solve problems, but to:

- Analyze time and space complexity
- Explore tradeoffs between approaches
- Implement optimal solutions
- Demonstrate clean, readable code

Each solution includes:
- Problem summary
- Complexity analysis
- Notes on constraints and assumptions

---

## Topics Covered

### Hashing & Frequency Patterns
- Contains Duplicate
- Two Sum
- Valid Anagram
- Group Anagrams
- Top K Frequent Elements
- Product of Array Except Self

### Patterns Demonstrated
- Hash maps for constant-time lookup
- Frequency counting techniques
- Bucket sort optimization
- Early exit strategies
- Time–space tradeoffs
- Avoiding unnecessary sorting

---

## Complexity Summary

| Problem | Time Complexity | Space Complexity | Approach |
|----------|----------------|-----------------|----------|
| Contains Duplicate | O(n) | O(n) | Set |
| Two Sum | O(n) | O(n) | Hash Map |
| Valid Anagram | O(n) | O(1) | Fixed Frequency Array |
| Group Anagrams | O(n * m) | O(n) | Frequency Signature Hashing |
| Top K Frequent | O(n) | O(n) | Bucket Sort |
| Product of Array Except Self | O(n) | O(n) | Prefix/postfix pass through |

Where:
- `n` = number of elements
- `m` = length of string

---

## Design Principles

- Prefer optimal asymptotic complexity
- Avoid unnecessary sorting when a linear solution exists
- Make constraints explicit
- Keep implementations clean and readable
- Use Pythonic patterns where appropriate

---

## Why This Repository Exists

In professional environments, much of the code I work on is confidential.  
This repository demonstrates:

- Problem-solving ability
- Understanding of algorithmic fundamentals
- Tradeoff reasoning
- Code clarity
- Complexity analysis skills

---

## How to Run

All solutions are implemented in Python 3.

Example:

```bash
python two_sum.py