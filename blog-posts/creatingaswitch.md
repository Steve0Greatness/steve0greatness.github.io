---
title: Creating a Switch in HTML and CSS
date: 2022 Feb 11
updated: 2023 Feb 2
---
A switch is something that is basically just a nicer looking checkbox. Here, I'll be showing you how to make one.

The first step is to create checkbox with any class; I'll be using `switch`, because it's a switch.

```html
<style>
    input[type=checkbox].switch {}
</style>
<input type="checkbox" class="switch" />
```

Next step is to add an appearance of none to the CSS--make sure to add `-moz-` and `-webkit-`. After that, you're going to want to set it so that the checkbox a rectangle--make sure it's in `px`. We also want to set the position to relative

```html
<style>
    input[type=checkbox].switch {
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        position: relative;
    }
</style>
<input type="checkbox" class="switch" />
```

Next we want to create `::before` pseudo. In there we want to make it have a position of relative, a width and height that are `-1px` less than the height of the main switch, a display of block, top and left set to `1px`, a content of `""`, and a background color that's different from the one in the main switch.

```html
<style>
    input[type=checkbox].switch {
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        position: relative;
        background: #000;
        width: 30px;
        height: 16px;
    }
    input[type=checkbox].switch::before {
        top: 1px;
        left: 1px;
        position: absolute;
        display: block;
        background: red;
        content: "";
        width: 14px;
        height: 14px;
    }
</style>
<input type="checkbox" class="switch" />
```

Finally add a pseudo called `:checked` which checks if a checkbox was checked, you'll want to change the before pseudo if the the checkbox is checked. You'll need to put it on the opposite side of where it started, for me, that's on the right-side.

```html
<style>
    input[type=checkbox].switch {
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        position: relative;
        background: #000;
        width: 30px;
        height: 16px;
    }
    input[type=checkbox].switch::before {
        top: 1px;
        left: 1px;
        position: absolute;
        display: block;
        background: red;
        content: "";
        width: 14px;
        height: 14px;
    }
    input[type=checkbox].switch:checked::before {
        left: 15px; /* .switch width - .switch::before width - 1px */
    }
</style>
<input type="checkbox" class="switch" />
```

I'm using the `left` property instead of the `right` property as it makes it easier to transition between the 2 positions. Here is the CSS with the transition added in, plus a background change(also dark mode):

```html
<style>
    :root {
        background: #000;
        color: #fff;
    }
    input[type=checkbox].switch {
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        position: relative;
        background: #fff;
        width: 30px;
        height: 16px;
    }
    input[type=checkbox].switch::before {
        top: 1px;
        left: 1px;
        position: absolute;
        display: block;
        background-color: #ff5c1c;
        content: "";
        width: 14px;
        height: 14px;
        transition: background-color .5s, left .5s;
    }
    input[type=checkbox].switch:checked::before {
        left: 15px; /* .switch width - .switch::before width - 1px */
        background-color: #3f9b00;
    }
</style>
<input type="checkbox" class="switch" />
```

All of this results in a final product that looks like:

<iframe style="background: #fff; border: none" src="/blog-files/switch-final.html"></iframe>

[See Code](/blog-files/switch-final.txt)