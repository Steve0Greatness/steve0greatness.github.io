title: The FizzBuzz Program
date: 2022 Feb 20
updated: 2024 Feb 2

A FizzBuzz Program is a program used in many job interviews to see if a programmer is good at problem solving. There are many ways to make one.

First let me tell you why I write these programs. These programs, at least in my opinion, are good when you're learning a new programming language. It gives you a problem to solve, and all you need to do to solve it. Incase you're wondering, the problem is to make a program that counts from 1 to 100 and replaces all multiples of 3 with Fizz, all multiples of 5 with Buzz, and multiples of both with FizzBuzz. Generally in interviews, they also ask you to add on more multiples, such as multiples of 7 are replaced with Fuzz, and multiples of 11 are replaced with Bizz.

Now that I've told you what a FizzBuzz Program is, let me show you how I make them in Python.

```python
for Index in range(1, 100):
    Response = ""
    print(Response)
```

The first thing I do is I create a for loop, and within it I put a print statement and a variable named toPrint.

```python
def FizzCompute(Number, Divisor, String):
    return String if Number % Divisor == 0 else ""

def SubstituteEmpty(String, Number):
    return String if String != "" else Number
    
for Index in range(1, 100):
    Response = SubstituteEmpty(FizzCompute(Index, 3, "Fizz") + FizzCompute(Index, 5, "Buzz"), Index)
    print(Response)
```
<details>
    <summary>Output</summary>
<samp>1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz</samp>
</details>

The next thing I do is I define a function that checks if one number is a multiple of another, and if it is, then it returns the string, otherwise, it returns an empty string.

Then I make a function that checks if a string is an empty one, if it is, then it returns a number.

Once I have these 2 functions, I go back into the for loop and make the `Response` variable have the variable for checking if a string is empty(and if it is replace it with a number) check if 2 of the other function that check if one number is a multiple of another(and if it is, return a string). Finally, it prints the output.

I've tried this method many times. Below are some examples of this method in action!

* [Kotlin](https://replit.com/@StevesGreatness/FizzBuzzKotlin)
* [Lua](https://replit.com/@StevesGreatness/FizzBuzzlua)
* [Python](https://replit.com/@StevesGreatness/FizzBuzzpython)
* [Ruby](https://replit.com/@StevesGreatness/FizzBuzzRuby)
