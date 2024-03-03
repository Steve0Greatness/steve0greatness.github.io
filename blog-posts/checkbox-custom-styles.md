title: Customize an HTML Checkbox
date: 2022 Feb 19
updated: 2024 Feb 2

TL;DR: `appearance: none;`.

Checkboxes are hard to style. But when you're making a website, they may look ugly.

<input type="checkbox" style="all: revert;" />

As you can see here, this bland checkbox does not fit into my clearly great website(/s). But really, it does not fit in at all.

The first step toward styling it how we want it is to give it an appearance of none, and a width and height that are what you want.

```css
input[type="checkbox"] {
    appearance: none;
    width: 15px;
    height: 15px;
    background-color: grey;
}
```

<iframe src="/blog-files/checkbox-custom-styles-ex1.html" style="background: #000; border: none"></iframe>

Now we can do whatever we want to it. You're also able to add a `:checked` sudo to change certain elements(like the `background-color`) depending on if the checkbox is checked or not.

```css
input[type="checkbox"] {
    appearance: none;
    width: 15px;
    height: 15px;
    background: #000;
    border: 1px #fff solid;
    border-radius: 2px;
}

input[type="checkbox"]:checked {
    background: #ce5aff;
}
```

<iframe src="/blog-files/checkbox-custom-styles-ex2.html" style="background: #000; border: none"></iframe>
