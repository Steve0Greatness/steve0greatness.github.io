---
title: Creating a simple theme switcher
date: 2021 Dec 08
---
This is a simple tutorial on how to make a simple theme switcher.<h1 id="step1">Step 1: Creating the themes</h1><p>The first step is to create the themes in your stylesheet, you can have as many as you want. Just make sure to remeber all their names within your CSS.</p><h1 id="step2">Step 2: Making an array</h1><p>This is why you need to remeber all their names within the CSS. You need to add them all to an array in your JS. Below is an example of an array containing some themes.</p><div class="code">const themes = ["light", "dark", "gamer"]</div><h1 id="step3">Step 3: Switching themes</h1><p>This is the part you've been waiting for! The actual content switcher. It's surprisingly simple.</p><p>First, get the index of the current theme using <span class="code">let currentTheme = themes.indexOf(document.documentElement.className)</span>. Then, use an if statement to see if it's more than or equal to the length of the array containing your themes.</p><div class="code">if (currentTheme + 1 >= themes.length) {<div style="margin-left:1em">document.documentElement.className = themes[0]</div>} else {<div style="margin-left:1em">document.documentElement.className = themes[currentTheme + 1]</div>}</div>Now just add a listener to the button(using <a href="https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener">event listener</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onclick">getElement.onclick</a>, or <a href="https://www.w3schools.com/TAgs/att_onclick.asp">onclick</a>)<h1 id="finished">Final Product</h1>In the end, what you just made should look something like the iFrame below.<br><iframe id="finalProduct" srcdoc='<!doctype html><html class="light"><head><style>html.light {background: #fff;color: #000;--buttonBackground: #fefefe;--buttonBorder: #ccc;--buttonColor: #001;}html.dark {background: #000;color: #fff;--buttonBackground: #101010;--buttonBorder: #333;--buttonColor: #fff;}html.gamer {background: #f00;color: #00f;--buttonBackground: #050;--buttonBorder: #0a0;--buttonColor: #0f0;}button {background: var(--buttonBackground);border: var(--buttonBorder) solid 3px;color: var(--buttonColor);}</style></head><body><button id="themeSwitch">Switch Theme</button><br>This is epic!<script type="application/javascript">const themes = ["light", "dark", "gamer"];document.getElementById("themeSwitch").onclick = () => {let curTheme = themes.indexOf(document.documentElement.className);if (curTheme + 1 >= themes.length) {document.documentElement.className = themes[0]} else {document.documentElement.className = themes[curTheme + 1]}}</script></body></html>' style="border:none"></iframe>