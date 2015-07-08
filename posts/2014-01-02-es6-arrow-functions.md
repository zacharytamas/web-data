---
layout: post
title: ES6 Arrow Functions
---

Just noticed earlier today that in Firefox version 22 and above ECMASCript 6's [CoffeeScript]()-style arrow functions are available:

<img src="/public/posts/arrow-functions-firefox/console.png" width="100%">

It's interesting seeing how they're fitting this Coffee concept into the confines of the JavaScript spec.

Of course Coffee uses indentation to denote blocks and JavaScript explicitly requires braces for blocks of longer than one statement, so although we are getting the arrow syntax in ES6 we'll never get this:

{% highlight coffeescript %}
  sayHello = (person) =>
    output = 'Hello ' + person
    return output
{% endhighlight %}

But this current compromise is enough to not fight too much over:

{% highlight javascript %}
  var sayHello = (person) => {
    var output = 'Hello ' + person;
    return output;
  }
{% endhighlight %}

They are only taking the fat-arrow functionality from Coffee, however, so these arrow functions are always using lexical `this` which is nice in cases where you need `this` in your function to refer to the `this` in scope when the function was defined&mdash;not where it was called.

{% highlight javascript %}

// Old way:
(function () {
  this.foo = 'bar';
  var _this = this;
  return function () {
    // If we said just `this` below it would not necessary
    // refer to what we expected. By making a closed over
    // variable called `_this` we can specifically state
    // what we want.
    return _this.foo;
  }
})();

// New way:
(function () {
  this.foo = 'bar';
  return () => this.foo;
})();

{% endhighlight %}

CoffeeScript has two different arrow operators for this purpose: `->` which is the standard way where `this` is dependent on calling context, and the "fat arrow" `=>` version which provides lexical `this`.

### Optional parenthesis

In Coffee, the parenthesis are optional if-and-only-if the function requires no arguments. This style is convenient because combined with Coffee's optional parenthesis on function invocation you can very lightweight syntax for common things like:

{% highlight coffeescript %}
$(document).ready ->
  doStuff()
{% endhighlight %}

If the function you're defining accepts named arguments at all, you must provide the parens:

{% highlight coffeescript %}
add = (a, b) -> a + b
{% endhighlight %}

In ECMAScript 6 arrow functions, for some reason, the parens are optional when the function accepts *only one* named argument, and are required for all other cases&mdash;including when no arguments are declared.

{% highlight javascript %}
// Parens required.
var add = (a, b) => a + b

// Parens not required because only one argument is declared.
var sayHello = name => console.log('Hello ' + name + '!');

// Parens required for no arguments
var bark = () => console.log('Ruff!');
{% endhighlight %}

This seems odd and error-prone. By making the parens optional only on the case of one named argument, you really aren't saving me much at all. In fact, I think without them there makes it even more confusing looking: *why is this identifier here? Where did I declare this? Oh, I'm declaring it right now.* On the other side, having a pair of empty parens makes me feel like I have leftover cruft from a refactor until I look after it and see the `=>` and think *Ah, this is a function.*

### Implicit return

Another slight quirk: you may have noticed the case where my ES6 arrow-function didn't have a return statement. If you're familiar with Ruby, Coffee, or other such languages, you may be familiar with this implicit return of the last expression evaluated. Don't be fooled however, this rule only applies to arrow functions that are only one expression.

{% highlight javascript %}
  var sayHello = (person) => {
    var output = 'Hello ' + person;
    return output;  // this return is required
  }

  // no return required
  var sayHello = (person) => 'Hello ' + person;
{% endhighlight %}

---

## We So Excited

All in all, though, I'm excited to see some of the things coming in ES6. [Mozilla seems to be leading the pack](https://developer.mozilla.org/en-US/docs/Web/JavaScript/ECMAScript_6_support_in_Mozilla) of implementing features as soon as they reach [TC39](http://www.ecma-international.org/memento/TC39.htm) consensus which is very exciting. It feels like there's a pretty bright future ahead for JavaScript as the community is finally starting to take it seriously in the past several years.

**Update:** If you'd like to use ES6 arrow functions now you can play around with Square's `es6-arrow-function` [project from Github](https://github.com/square/es6-arrow-function). Seems like you could include it in your Grunt build process to extrapolate arrow functions you write in your code into their ES5 equivalents.
