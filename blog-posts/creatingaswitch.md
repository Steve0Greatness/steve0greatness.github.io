---
title: Creating a Switch in HTML and CSS
date: 2022 Feb 11
updated: 2023 Feb 1
---
A switch is something that is basically just a nicer checkbox. Here, I'll be showing you how to make one.

The first step is to create checkbox with any classname; I'll be using `switch`.

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

Next we want to create `::before` pseudo. In there we want to make it have a position of relative, a width and height that are abit less than the height of the main switch, a display of inline-block, a top and left of 0, a content of anything, color of transparent, and a background color that's different from the one in the main switch.

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
        color: transparent;
        width: 14px;
        height: 14px;
    }
</style>
<input type="checkbox" class="switch" />
```

Finally add a pseudo called `:checked` which checks if a checkbox, or a radio, was checked; you'll want to change the before pseudo if the the checkbox is checked. You need to set the left to a bit less than the width of the checkbox; you can adjust it until it looks right to you.

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
        color: transparent;
        width: 14px;
        height: 14px;
    }
    input[type=checkbox].switch:checked::before {
        left: unset !important;
        right: 1px;
    }
</style>
<input type="checkbox" class="switch" />
```

Now, let's look at what it looks like:

<iframe style="background: #fff; border: none" src="/blog-files/switch-final.html"></iframe>

[See Code](/blog-files/switch-final.txt)