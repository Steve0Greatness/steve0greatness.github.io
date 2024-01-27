---
title: Creating a HTML drop-down list
date: 2021 Oct 01
updated: 2024 Jan 26
---
In order to create a drop-down selection list in HTML, we must first understand why they are important.

Drop-down lists can be used in lots of ways, from creating a way for people to chose from a strict set of options, to making an on-off switch(even though you should use buttons for that).

Before we start, here is an example:

**Select Image:** <select id="select" onchange="document.getElementById('img').src = document.getElementById('select').value"><option value="https://upload.wikimedia.org/wikipedia/commons/a/a2/Paul_von_Hindenburg_%281914%29_von_Nicola_Perscheid.jpg" selected="true">Img 1</option><option value="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Wilfried_Gruhn.jpg/121px-Wilfried_Gruhn.jpg">Img 2</option><option value="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Blackcap_%28Sylvia_atricapilla%29_male.jpg/129px-Blackcap_%28Sylvia_atricapilla%29_male.jpg">Img 3</option><option value="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Lt._Gen._Nguy%E1%BB%85n_V%C4%83n_Thi%E1%BB%87u_at_Cam_Ranh_Base%2C_October_26%2C_1966.jpg/116px-Lt._Gen._Nguy%E1%BB%85n_V%C4%83n_Thi%E1%BB%87u_at_Cam_Ranh_Base%2C_October_26%2C_1966.jpg">Img 3</option><option value="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Steve_Stricker.jpg/157px-Steve_Stricker.jpg">Img 4</option><option value="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Aegotheles_chrisoptus_-_Catlereigh_Nature_Reserve.jpg/350px-Aegotheles_chrisoptus_-_Catlereigh_Nature_Reserve.jpg">Img 5</option><option value="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Michael_Whelan_-_Lucca_2017.jpg/118px-Michael_Whelan_-_Lucca_2017.jpg">Img 6</option><option value="https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/St_Pancras_Railway_Station_2012-06-23.jpg/152px-St_Pancras_Railway_Station_2012-06-23.jpg">Img 7</option><option value="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Mae_La_refugee_camp_TFA.jpg/162px-Mae_La_refugee_camp_TFA.jpg">Img 8</option><option value="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/JimmyCarterPortrait_%28cropped%29.jpg/121px-JimmyCarterPortrait_%28cropped%29.jpg">Img 9</option></select>

<img id="img" src="https://upload.wikimedia.org/wikipedia/commons/a/a2/Paul_von_Hindenburg_%281914%29_von_Nicola_Perscheid.jpg" style="width: auto; height: 10em;" />

<small>Images from <a href="https://en.wikipedia.org">Wikipedia</a>, on <a href="https://web.archive.org/web/20211001135954/https://en.wikipedia.org/wiki/Main_Page">Oct. 2nd</a> & <a href="https://web.archive.org/web/20211002095505/https://en.wikipedia.org/wiki/Main_Page">1st, 2021</a></small>

For some weird reason, it's not in `<input>`, it has it's own tags: `<select>` and `<option>`. Using these is a little like making a list, if you've ever made one. Here's an example bit of HTML:

```html
<select>
    <option>op 1</option>
    <option>op 2</option>
</select>
```

Like all `input`s, `select` can have an id and name, and like `input[type=radio]`, `option` can have a value.

However, you may not know some things that could be useful here, such as defaulting, or making things update upon being changed, well, you can do defaulting with `selected` in the `<option>` that you want to be preselected. Changes done the page upon the change of the selection in the drop-down(or anything else that can be changed by the user) is `onchange="submitFunction()"` being placed in the `<select>`.

Let's check back on the code that we made at the code example:

```html
<select onchange="submitFunction()" id="selection">
    <option value="op1" selected>op 1</option>
    <option value="op2">op 2</option>
</select>
```

Inorder to access the selected option with JavaScript, use `document.getElementById("selection").value`.

That's basically it, feel free to `CTRL + C` `CTRL + V` it. /s