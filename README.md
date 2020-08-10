# Session 4 
---
## Objective
- Write a Qualean class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place.  
 
- It implements these functions (with exactly the same names) 

``` html 
    __and__,  __or__, __repr__, __str__, __add__, __eq__, __float__,
    __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, 
    __bool__

# '__repr__'
This method returns the representation of the Qualean object and the value it contains in a nicely formatted string.

# '__str__'
This method returns the str object of value of the Qualean object mentioned.

# '__and__'
This magic method implements the logical AND Operation for the user defined Qualean objects.

# '__or__'
This magic method implements the logical OR Operation for the user defined Qualean objects.

# '__bool__'
This magic method returns the bool value for the Qualean object.

# '__add__'
This magic method overrides the basic implementation of addition + operator for the Qualean class.

# '__eq__'
This method overrides the equality checking == for the user defined Qualean objects.

# '__float__'
This method returns the float conversion of the Qualean object.

# '__ge__'
This method overrides the greater than or equal to checking >= for the user defined Qualean objects.

# '__gt__'
This method overrides the greater than checking > for the user defined Qualean objects.

# '__invertsign__'
This method returns the opposite sign value of the calling Qualean object.

# '__le__'
This method overrides the lesser than or equal to checking <= for the user defined Qualean objects.

# '__lt__'
This method overrides the lesser than checking < for the user defined Qualean objects.

# '__mul__'
This method overrides the basic implementation of multiplication * operator for the Qualean class.

# '__sqrt__'
This method implements the mathematical Square root operation on the Qualean object.for negative numbers, it returns 
complex numbers
    
    
# 'ValueError'
Python provides a built in way to raise exceptions if there are any value errors i.e. user can raise this exception if 
the value does not match the expected range or anything else that a user want to enforce.

# 'math'
math is a module that provides access to the mathematical functions defined by the C standard.


```
- Write a test file, that tests all of the functions mentioned above + the other basic ones 
- Test file must contain at least 25 tests

---

## Test Cases Results

| Serial No  | Test Case | Result |
| ---------- | --------- | ------ |
| 1 | README File Exists | Pass |
| 2 | RREADME Words Counts | Pass |
| 3 | README proper description | Pass |
| 4 | RREADME Formatting | Pass |
| 5 | Proper identation and  PEP8 guidelines | Pass |
| 6 | Function name not defined with capital letters | Pass |
| 7 | __repr__ proper implementation | Pass |
| 8 | __str__ proper implementaton | Pass |
| 9 | __lt__ implementation check | Pass |
| 10 | __le__ implementation check | Pass | 

---
