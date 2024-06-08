## Tricks
### Sliding Window for Fixed Size:
* Initialize the window sum or properties for the first window of size k.
* Slide the window by adding the next element and removing the first element of the previous window.
* Track the desired result (e.g., maximum sum, minimum sum). 

### Sliding Window for Variable Size:
* Use the right pointer to expand the window.
* Use the left pointer to contract the window when a condition is violated.
* Update the result whenever the condition is satisfied.

### Using Sets for Unique Characters:
* For problems like finding the longest substring without repeating characters, use a set to track unique characters.
* When a duplicate character is found, move the left pointer until the window becomes valid again.

### Using Counters or Dictionaries:
For problems involving counts of elements (e.g., at most two occurrences of each character), use a dictionary to track counts.
Adjust the window when counts exceed the allowed limits.