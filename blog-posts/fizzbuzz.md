---
title: The FizzBuzz Program
date: 2022 Feb 20
updated: 2024 Jan 17
---
A FizzBuzz Program is a program used in many job interviews to see if a programmer is good at problem solving. There are many ways to make one.

First let me tell you why I write these programs. These programs, at least in my opinion, are good when you're learning a new programming language. It gives you a problem to solve, and all you need to do to solve it. Incase you're wondering, the problem is to make a program that counts from 1 to 100 and replaces all multiples of 3 with Fizz, all multiples of 5 with Buzz, and multiples of both with FizzBuzz. Generally in interviews, they also ask you to add on more multiples, such as multiples of 7 are replaced with Fuzz, and multiples of 11 are replaced with Bizz.

Now that I've told you what a FizzBuzz Program is, let me show you how I make them in Python.

```python
for i in range(1, 100):
    toPrint = ""
    print(toPrint)
```

The first thing I do is I create a for loop, and within it I put a print statement and a variable named toPrint.

```python
def check(checktomulti, multi, toreturn):
    if checktomulti % multi == 0:
        return toreturn
    return ""

def checkEmpty(string, number):
    if string == "":
        return number
    return string
    
for i in range(1, 100):
    toPrint = checkEmpty(check(i, 3, "Fizz") + check(i, 5, "Buzz"), i)
    print(toPrint)
```
The next thing I do is I define a function that checks if one number is a multiple of another, and if it is, then it returns the string, otherwise, it returns an empty string.

Then I make a function that checks if a string is an empty one, if it is, then it returns a number.

Once I have these 2 functions, I go back into the for loop and make the `toPrint` variable have the variable for checking if a string is empty(and if it is replace it with a number) check if 2 of the other function that check if one number is a multiple of another(and if it is, return a string). Finally, it prints the output.

I've tried this method many times. Below are some examples of this method in action!

* [Kotlin](https://replit.com/@StevesGreatness/FizzBuzzKotlin)
* [Lua](https://replit.com/@StevesGreatness/FizzBuzzlua)
* [Python](https://replit.com/@StevesGreatness/FizzBuzzpython)
* [Ruby](https://replit.com/@StevesGreatness/FizzBuzzRuby)