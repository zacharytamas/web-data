---
layout: post
title: 'How I Work: Coding'
subtitle: "A look into the tools and tricks I use to get work done."
---

My primary development tool is none other than [Sublime Text 2](http://www.sublimetext.com/2). It is my goto text editor for most everything. For programming, I use it exclusively. I have a [PyCharm](http://www.jetbrains.com/pycharm/) license [my employer](/portfolio/lights-on/) bought my team but I could never get into it. Aside from programming, I use Sublime Text for basically everything else as well, including taking notes, drafting letters, making on-the-spot todo lists, etc. I'm even writing this post in Sublime Text right now using the Markdown format.

### Plugins I Use

I use several plugins for Sublime Text to work better. A few of my favorites are:

* **[Package Control](https://sublime.wbond.net/)**. Of course I have this. This allows for easily adding/removing plugins to Sublime Text. It's the first thing you should add to a fresh Sublime installation.
* **Backbone.js**. I've installed the Backbone.js plugin which has a lot of handy completions and snippets for writing `Backbone.js` code faster. Includes both JavaScript and CoffeeScript!
* **[CoffeeScript](https://github.com/Xavura/CoffeeScript-Sublime-Plugin)**. I really love [CoffeeScript](http://coffeescript.org) and so adding Coffee support to Sublime Text is a must-have item. Primarily I use it for the syntax highlighting and a small portion of the completions that I actually use.
* **[CoffeeLint](https://github.com/clutchski/coffeelint)**. For linting the aforementioned Coffee.
* **[CSScomb](https://github.com/csscomb/CSScomb-for-Sublime)**. This handy gadget will "comb" your CSS (and also at least LESS, but probably SASS, too) files, reordering your style properties into a consistent ordering. I like to run this occasionally to keep things neat.
* **[Djaneiro](https://github.com/squ1b3r/Djaneiro)**. This is a must-have for [Django](https://www.djangoproject.com/) developers using Sublime. It adds a TON of completions, snippets, and syntaxes to Sublime. These make it really easy to rapidly write boilerplate Django things like model fields, form fields, and Django template tags/filters.
* **[DocBlockr](https://github.com/spadgos/sublime-jsdocs)**. DocBlockr makes it really easy to write JavaDoc-style documentation as comments for various languages. I've lately been fond of the lightweight [Docco](http://jashkenas.github.io/docco/) for generating JavaScript documentation (my primary language these days), but on occasion at work on legacy code I'll use JSDoc format. DocBlockr is handy for that.
* **[Emmet](https://github.com/sergeche/emmet-sublime)**. Your HTML markup writing shotgun. Lets you rapidly generate HTML markup with minimal keystrokes. If you're not using it you're not productive.
* **Jasmine**. I like writing tests for my JavaScript using [Jasmine](http://jasmine.github.io/) and this plugin just adds common completions to expedite the process of writing all the nested functions that Jasmine is known for.
* **[LESS](https://github.com/danro/LESS-sublime)**. I'm not particularly against [SASS](http://sass-lang.com/), but I've just always used [LESS](http://www.lesscss.org/) and so that's what I prefer to write in since I'm familiar.
* **[SublimeLinter](https://github.com/SublimeLinter/SublimeLinter)**. Probably the most important plugin I have. This helps identify bad/questionable code throughout a whole bunch of languages. You should never professionally develop software these days without a linter.

### My Sublime workspace

I'm currently using the [Spacegray theme](http://kkga.github.io/spacegray/) for Sublime, which I really like quite a bit. I'm going through this minimalism phase lately and it's quite pleasing to that end.

<div class="pullout image">
  <img src="/public/posts/how-i-work-part-1/sublime-screenshot.jpg" alt="My window writing this post. Recursion?" width="100%">
  <p class="caption">My window writing this post. Recursion?</p>
</div>

When I'm really in the zone and familiar with the codebase, I'll hide the sidebar altogether and work with just the currently open file. Using Sublime's *awesome* `Goto Anything...` feature you can easily hop between files in the codebase if you're familiar enough. I like doing this as it's faster than searching through the sidebar manually.
