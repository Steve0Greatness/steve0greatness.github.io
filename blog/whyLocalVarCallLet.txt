title: Why local variables are called "let"
date: 2022 Jan 10
updated: 2024 Feb 2

In JavaScript there are 3 different kinds of variables, global variables(using `var`), constants(`const`, and local variables`let`). All of the act a little differently from each other. Allow me to explain what they do.

Global variables, made using `var`, are as they sound, global variables. Once defined, they can be used, edited, or redefined anywhere.

Constants, defined with `const`, are constant, they cannot change, at all.

Local variables, defined with `let`, are variables that can only be used in the place that it is defined, like a function, and it's children.

Now that we has that established, *let*'s talk about how local variables got their name.

Turns out "let" is a mathematical term.

> The **"let" expression** may also be defined in mathematics, where it associates a Boolean condition with a restricted scope.
> <cite>Quote from [Wikipedia "Let expression"](https://en.wikipedia.org/w/index.php?title=Let_expression&oldid=1187985658) as of <time>2024 Feb 2</time></cite>

It was first used in programming in early languages like Basic.

In case you're wondering, the main source is an answer on Stack Overflow: *"Why was the name 'let' chosen for block-scoped variable declarations in JavaScript?"*, answer by [exebook](https://stackoverflow.com/users/1968972), edited by [Pikamander2](https://stackoverflow.com/users/1741346); [link](https://stackoverflow.com/a/37917071).
