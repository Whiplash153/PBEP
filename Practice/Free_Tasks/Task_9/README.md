# Task: Customer Reviews Analysis

## Condition
The company collects customer feedback after purchases.  
Each review consists of a customer name and a rating (from 1 to 5).  
You need to:
1. Display the names of customers who rated **5**.
2. Calculate the average rating across all reviews.

## Solution
We stored all reviews in a **dictionary** with customer names as keys and ratings as values.  
Then used a **list comprehension** to extract names with a rating of 5.  
To calculate the average rating, we iterated through the dictionary using `.items()`,  
summed all the ratings, and divided by the total number of reviews.  
The result was rounded to the nearest integer for a clean output.

**Tools used:** dict, list comprehension, for-loop, len(), sum(), round(), print.