---
title: Creating a Switch in HTML and CSS
date: 2022 Feb 11
---
<p>A switch is something that is basically just a nicer checkbox. Here, I'll be showing you how to make one.</p>The first step is to create checkbox with any classname; I'll be using <span class="code">switch</span>.<div class="code">&lt;style&gt;<div style="margin-left:1em;">input[type=checkbox].switch {}</div>&lt;/style&gt;<br>&lt;input type="checkbox" class="switch"&gt;</div><p>Next step is to add an appearance of none to the CSS--make sure to add <span class="code">-moz-</span> and <span class="code">-webkit-</span>. After that, you're going to want to set it so that the checkbox a rectangle--make sure it's in <span class="code">px</span>. We also want to set the position to relative</p><div class="code">&lt;style&gt;<div style="margin-left:1em;">input[type=checkbox].switch {<div style="margin-left:1em;">-webkit-appearance: none;<br>-moz-appearance: none;<br>appearance: none;<br>position: relative;<br>width: 30px;<br>height: 16px;</div>}</div>&lt;/style&gt;<br>&lt;input type="checkbox" class="switch"&gt;</div><p>Next we want to create a <span class="code">::before</span> pseudo. In there we want to make it have a position of relative, a width and height that are abit less than the height of the main switch, a display of inline-block, a top and left of 0, a content of anything, color of transparent, and a background color that's different from the one in the main switch.</p><div class="code">&lt;style&gt;<div style="margin-left:1em;">input[type=checkbox].switch {<div style="margin-left:1em;">-webkit-appearance: none;<br>-moz-appearance: none;<br>appearance: none;<br>position: relative;<br>width: 30px;<br>height: 16px;</div>}<br>input[type=checkbox].switch::before {<div style="margin-left:1em;">top: 0;<br>left: 0;<br>position: relative;<br>background: red;<br>content: ".";<br>color: transparent;<br>width: 14px;<br>height: 14px;</div>}</div>&lt;/style&gt;<br>&lt;input type="checkbox" class="switch"&gt;</div><p>Finally add a pseudo called <span class="code">:checked</span> which checks if a checkbox, or a radio, was checked; you'll want to change the before pseudo if the the checkbox is checked. You need to set the left to a bit less than the width of the checkbox; you can adjust it until it looks right to you.</p>Now, let's look at what it looks like<br><iframe style="background:#fff;border:none" srcdoc='<style>input[type=checkbox].switch {-webkit-appearance: none;-moz-appearance: none;appearance: none;background: #efefef;position: relative;border: 1px black solid;width: 30px;height: 16px;border-radius: 0;}input[type=checkbox].switch::before {top: 0;left: 0.24px;position: relative;background: red;content: ".";color: transparent;width: 20px;height: 14px;}input[type=checkbox].switch:checked::before {left: 25px;}</style><input type="checkbox" class="switch">'></iframe>