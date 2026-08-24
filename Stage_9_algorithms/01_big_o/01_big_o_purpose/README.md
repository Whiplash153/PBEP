# Big O — Purpose of Complexity Analysis

## Goal

Understand why algorithm complexity analysis is needed and why algorithms are compared by growth of operations instead of execution time.

## Main Idea

Big O describes how the number of operations of an algorithm changes when the size of input data increases.

Big O does not measure:
- execution time in seconds;
- exact number of operations;
- performance of a specific computer.

Big O describes the growth pattern of algorithm complexity.

## Why Execution Time Is Not Enough

Execution time depends on many external factors:
- CPU;
- memory;
- operating system;
- programming language;
- implementation details.

The same algorithm can run with different speed in different environments.

For objective comparison, we analyze how the number of operations grows depending on the input size.

## Main Difference

The important thing is not how many operations an algorithm performs on a small amount of data.

The important thing is how quickly the number of operations grows when the input size increases.

Example:

5n
100n

These expressions have different numbers of operations, but the same growth pattern.

Both algorithms have:

O(n)

complexity.

## Key Takeaways

- Big O is a way to describe the growth of algorithm complexity.
- The main parameter of analysis is the input size n.
- Constant multipliers do not change the complexity class.
- Algorithms are compared by their behavior on large amounts of data.
- Complexity analysis helps choose more efficient solutions.

## New Terms

### n

The size of input data.

Example:

If we have a list with 100 elements:

n = 100

### Input Size

The amount of data that an algorithm receives for processing.

## Control Questions

### Why does Big O not measure seconds?

Because execution time depends on the environment, while Big O describes the algorithm itself independently of a specific computer.

### What does Big O show?

It shows how the number of operations grows when the input size increases.

### Why do 5n and 100n have the same Big O?

Because both algorithms grow linearly when n increases.