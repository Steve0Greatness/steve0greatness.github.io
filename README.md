# Steve0Greatness' Website

Note that whilst this repository is the official code of my website, the only offically support
depolyment of this code is [steve0greatness.nekoweb.org](https://steve0greatness.nekoweb.org).

This is the static site generator of my website! It's written completely in
Python, using the libraries Jinja2(templating), Markdown2(blog posts), and PyYAML(lists).

It's built to be runnable with a single command, and can be ran on multiple operating systems
and then dump its contents into the `build` directory(this can be configured); and from there,
you can pretty much do whatever you want with it:

* Deploy it to GitHub pages
* Zip it up using and upload it to Nekoweb.org

I mostly use this SSG so I don't have to over-complicate my pages with tons of JavaScript that
slows down the load time significantly.


It's licensed under GPL-v3, so don't go close-sourcing it :P
