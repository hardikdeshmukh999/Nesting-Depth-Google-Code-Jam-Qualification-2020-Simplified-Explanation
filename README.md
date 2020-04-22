# Nesting Depth Problem B | Google Code Jam Qualification Round 2020 [Simplified Explanation]

Nesting Depth Problem B | Google Code Jam Qualification Round 2020 - Simplified Explanation and Python code by Hardik Deshmukh.
<p align="center">
  <img  src="Code-Jam-Hub-Advertisement-Image.png">
</p>
The objective is to solve the problem statement with a minimum of time and space complexity.
I would recommend that you go through the problem statement and explanation once and try coding, or if you feel less confident, you can always refer to the optimized Python code that can be a bit difficult to understand.

## Nesting Depth Simplified Explanation

### Explanation: 
Traversing the Input elements one by one.

Depth is the number of open parenthesis.

Note: depth is the number of only those open parenthesis which do not have a closing parenthesis.
```
Example:

Case 1: S = ( ( ( ) ( ) )

depth = 1     Since S has only 1 open parenthesis with no closing parenthesis to it

Case 2: S = ( ( ) ) 

depth =0      Since all open parenthesis are closed 
```

Initiate with depth = 0
 
```
Input: 312

Output: (((3))1(2))
```

#### Step 1: Input is 3

If the number is 3 then then depth should be = 3

The number of open parenthesis should be 3

Append 3 opening parenthesis since depth = 0 and append the number

```
(((3
```
Now depth = 3

#### Step 2: Input is 1

If the number is 1 then then depth should be = 1

The number of open parenthesis should be 1

Append 2 closing parenthesis since depth = 3 and append the number
```
(((3))1
```
Now depth = 1

#### Step 3: Input is 2

If the number is 2 then then depth should be = 2

The number of open parenthesis should be 2

Append 1 opening parenthesis since depth = 1 and append the number
```
(((3))1(2
```
Now depth = 2

#### Step 4: End of list

Append closing parenthesis to close all opening parenthesis

Until depth = 0 keep appending closing parenthesis
```
(((3))1(2))
```









#
## Nesting Depth Problem B | Google Code Jam Problem statement

Given a string of digits  **S** , insert a minimum number of opening and closing parentheses into it such that the resulting string is balanced and each digit d is inside exactly d pairs of matching parentheses.

Let the _nesting_ of two parentheses within a string be the substring that occurs strictly between them. An opening parenthesis and a closing parenthesis that is further to its right are said to _match_ if their nesting is empty, or if every parenthesis in their nesting matches with another parenthesis in their nesting. The _nesting depth_ of a position p is the number of pairs of matching parentheses m such that p is included in the nesting of m.

For example, in the following strings, all digits match their nesting depth: 0((2)1), (((3))1(2)), ((((4)))), ((2))((2))(1). The first three strings have minimum length among those that have the same digits in the same order, but the last one does not since ((22)1) also has the digits 221 and is shorter.

Given a string of digits  **S** , find another string S&#39;, comprised of parentheses and digits, such that:

- all parentheses in S&#39; match some other parenthesis,
- removing any and all parentheses from S&#39; results in  **S** ,
- each digit in S&#39; is equal to its nesting depth, and
- S&#39; is of minimum length.

Input

The first line of the input gives the number of test cases,  **T**.  **T**  lines follow. Each line represents a test case and contains only the string  **S**.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the string S&#39; defined above.

Limits

Time limit: 20 seconds per test set.
 Memory limit: 1GB.
 1 =  **T**  = 100.
 1 = length of  **S**  = 100.

Test set 1 (Visible Verdict)

Each character in  **S**  is either 0 or 1.

Test set 2 (Visible Verdict)

Each character in  **S**  is a decimal digit between 0 and 9, inclusive.
```
Sample 1

Input
0000
101
111000
1

Output
Case #1: 0000
Case #2: (1)0(1)
Case #3: (111)000
Case #4: (1)

Sample 2

Input:
021
312
4
203


Output:
Case #1: 0((2)1)
Case #2: (((3))1(2))
Case #3: ((((4))))
Case #4: ((2))0(((3)))
```

The strings ()0000(), (1)0(((()))1) and (1)(11)000 are not valid solutions to Sample Cases #1, #2 and #3, respectively, only because they are not of minimum length. In addition, 1)( and )(1 are not valid solutions to Sample Case #4 because they contain unmatched parentheses and the nesting depth is 0 at the position where there is a 1.

You can create sample inputs that are valid only for Test Set 2 by removing the parentheses from the example strings mentioned in the problem statement.

