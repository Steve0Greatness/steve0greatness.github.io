---
title: Why local variables are called "let"
date: 2022 Jan 10
---
<p>In JavaScript there are 3 different kinds of variables, global variables(using <span class="code">var</span>), constants(<span class="code">const</span>, and local variables(<span class="code">let</span>). All of the act allittle differently from eachother. Allow me to explain what they do.</p><p>Global variables, made using <span class="code">var</span>, are as they sound, global variables. Once defined, they can be used, edited, or redefind anywhere.</p><p>Constants, defined with <span class="code">const</span>, are constant, they cannot change, at all.</p><p>Local variables, defined with <span class="code">let</span>, are variables that can only be used in the place that it is defined, like a function, and it's children.</p>Now that we has that established, <em>let</em>'s talk about how local variables got their name.<p>Turns out "let" is a mathematical term. <span class="quote">The <b>"let" expression</b> may also be defined in mathematics, where it associates a Boolean condition with a restricted scope.</span> <a href="https://en.m.wikipedia.org/wiki/Let_expression" class="source">[source]</a>. It was first used in programming in early languages like Basic.</p>In case you're wondering, the main source is <a href="https://stackoverflow.com/a/37917071">this answer on Stack Overflow</a>.