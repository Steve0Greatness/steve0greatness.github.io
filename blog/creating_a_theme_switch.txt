title: Create a Theme Switch
date: 2021 Dec 08
updated: 2024 Jun 15

This is a simple tutorial on how to make a simple theme switcher.

First step is to create the themes you'll want on your site. You may just want a light and dark mode, however, you may also want other themes. As an example: a clown theme that makes the page absurdly colorful, like a GeoCities site in the early 2000s. For these themes, you can use CSS variables set on the `html` parent tag(all other elements are considered children of `html`). Variables can be set in CSS using double hyphens followed by a sequence of text that can use numbers(but not at the start), letters(capital or lowercase), underscores, and hyphens; these variables can then be accessed within your text using the `var()` function with the name of the variable(including the starting hyphens). You can change out the CSS variables using different selectors on the `html` tag within the CSS, for me: I'm using the `[data-theme]` attribute; however, you can use classes if you want. Here is the CSS I wrote:

```css
html[data-theme=light] {
    background: #fff;
    color: #000;
    --buttonBackground: #fefefe;
    --buttonBorder: #ccc;
    --buttonColor: #001;
}
html[data-theme=dark] {
    background: #000;
    color: #fff;
    --buttonBackground: #101010;
    --buttonBorder: #333;
    --buttonColor: #fff;
}
html[data-theme=hotdogstand] {
    background: #f00;
    color: #fff;
    --buttonBackground: #ff0;
    --buttonBorder: #000;
    --buttonColor: #000;
}
button {
    background: var(--buttonBackground);
    border: var(--buttonBorder) solid 3px;
    color: var(--buttonColor);
}
```

Now we need to create a button that we will use to change the `[data-theme]` attribute. You (probably) already know what buttons are, so I won't go in depth about then. However: you will need to add an `[id]` to the button, this will come in play shortly.

```html
<button id="theme-switch">Switch Theme</button>
```

Now, it is time to write the JavaScript. First, you'll want to make a constant with the themes you filled into your CSS, for me, that was `dark`, `light`, and `clown`. I'll name this `themes`.

```javascript
const themes = ["light", "dark", "hotdogstand"];
```

We now need to query the <abbr title="Document Object Model">DOM</abbr> for our theme switch button. This can be done in 2 ways: `document.querySelector` or `document.getElementById`; personally, I prefer `querySelector`, as it allows you to write a CSS selector to get an element from the DOM, allowing for shorter, more digestible, code.

We have to add a click event to the button. This can be done in 2 ways within JavaScript: `addEventListener("click", ...)` and `onclick`. I personally like `addEventListener` more, so I'll use that. Within the `addEventListener` function, you need to put a function. This function will control the logic of our theme switch. I'll call this function `SwitchTheme`, to reflect it's functionality.

```javascript
const ThemeSwitchButton = document.querySelector("#theme-switch");
ThemeSwitchButton.addEventListener("click", SwitchTheme());
function SwitchTheme() {}
```

Explaining each part of this function as it's written out would take awhile, so instead, I'll add comments to the ends of each line giving a short explanation. Also, for the sake of shortness, I've placed `document.documentElement` inside the constant `HTML`, giving us access to the root element in the DOM(`html`).

```javascript
let CurrentTheme = themes.indexOf(HTML.dataset.theme); // Gets how far in the current theme is into the "themes" constant.
if (CurrentTheme + 1 >= themes.length) { // Checks if it's at the end of the array,
    HTML.dataset.theme = themes[0]; // If so, reset at the start.
    return; // Ends the function here, preventing next bit of code from running.
}
HTML.dataset.theme = themes[CurrentTheme + 1]; // Goes to the next theme.
```

Now we have a finished product. Here's the expected output:

<iframe id="finalProduct" src="/blog-files/theme-change-final.html" style="border:none"></iframe>
[See Code](/blog-files/theme-change-final.txt)
