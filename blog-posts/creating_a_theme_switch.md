---
title: Creating a simple theme switcher
date: 2021 Dec 08
updated: 2024 Feb 01
---
This is a simple tutorial on how to make a simple theme switcher.

## Step 1: Creating the themes

The first step is to create the themes in your stylesheet, you can have as many as you want. Just make sure to remeber all their names within your CSS.

## Step 2: Making an array

This is why you need to remeber all their names within the CSS. You need to add them all to an array in your JS. Below is an example of an array containing some themes.

```js
const themes = ["light", "dark", "gamer"]
```

## Step 3: Switching themes

This is the part you've been waiting for! The actual content switcher. It's surprisingly simple.

First, get the index of the current theme using 

```js
let currentTheme = themes.indexOf(document.documentElement.className).
```

Then, use an if statement to see if it's more than or equal to the length of the array containing your themes.

```js
if (currentTheme + 1 >= themes.length) {
    document.documentElement.className = themes[0];
} else {
    document.documentElement.className = themes[currentTheme + 1]
}
```

Now just add a listener to the button(using [event listener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener), [getElement.onclick](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onclick), or [onclick](https://www.w3schools.com/TAgs/att_onclick.asp))

## Final Product

In the end, what you just made should look something like the iFrame below.

<iframe id="finalProduct" src="/blog-files/theme-change-final.html" style="border:none"></iframe>
[See Code](/blog-files/theme-change-final.txt)