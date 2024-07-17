== Website Source Code ==

All of my site is generated using a small Python script.
This script is build.py. Keep in mind that you may need
to install requirements (and also download Renderers.py
from this repo):

* Jinja2
* Markdown2
* PyYAML

This is all that is required. This script is licensed
under the LGPL, as I don't currently want to license my
site.

If you plan to base your website on my own, I ask that
you simply copy the script, and not my entire site (IE:
Please only download build.py and Renderers.py). From
there, you will need to create a few folders:

* views
* blog-posts
* lists
* static

The following few sections will explain these
directories.

---

views includes all of your HTML templates which will be
used to render all pages on your site. It uses Jinja
syntax. You can find a reference for Jinja's syntax on
the project's website:

https://jinja.palletsprojects.com/en/3.1.x/templates/

---

blog-posts contains all the markdown source files for
your blog-posts. These are written using a somewhat
unique format:

```
title: <Title of the article>
date: <Initial publication date>
updated: <Last modification date (optional)>

<Article body>
```

Also, I've enabled a bunch of extensions in MD2. Some
that matter include:

* header-ids
* markdown-in-html
* footnotes
* strike

You can read MD2's Wiki* for more information on these:

github.com/trentm/python-markdown2/wiki/Extras

---

lists includes all lists you may want to make. Lists
are a YAML based format.

To begin with, there's the root list, which includes
its title and a starting paragragh, before denoting the
rest of the list using the list keyword.

```
title: <Title of list>
paragraph: <Starting paragraph>
list:
```

The list must be formated as a YAML list. Each element
in this list starts with a type. One such type is text.
Text is a small section of HTML. It requires there be a
text parameter.

```
- type: text
  text: <text>
  comment: <additional text>
```

text may also have a comment, which is formated as
being in parenthesis. Here's a list of other available
types:

* ```
  - type: link
    text: <link text>
    href: <link link>
    comment: <additional text>
  ```
* ```
  - type: category
    title: <category title>
    id: <id used for the category's header>
    list:
      <sub elements>
  ```
  Note that category can also have other categories.

---

static is all static content, it's dumped into the base
directory of the output directory.

---

Speaking of the output directory: by default, it's at
build. build can be deployed to whatever hosting
service you are using, such as GitHub Pages.
