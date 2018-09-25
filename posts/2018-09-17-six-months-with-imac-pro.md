---
title: 'Six months with the iMac Pro'
layout: post
category: 'Technology'
tags:
  - Apple
---

I’ve had the iMac Pro for about six months now so I figured I should collect some brief thoughts on it. This is not a full, detailed review because there are plenty of those online, but instead this is my subjective experience.

## Why I decided to try out an iMac Pro

For a laptop I use a 2016 MacBook Pro 15”, the first edition with the Touch Bar (and yes, I’ve had to have the keyboard replaced). Performance-wise it worked alright for me for my usual work but I knew that I was becoming interested in more processing-intensive tasks such as Machine Learning and I’d likely want more, or at least a powerful-enough always-on and properly ventilated machine.

I also wanted more screen real estate and since I spent the majority of my time at my desk, I wasn’t exactly getting a lot of the portability benefits anyway. A natural stopgap for this issue was to buy an external display, which I happened to already have from a previous Hackintosh build anyway<sup>[1](#foot1)</sup>. I found this frustrating after a while because macOS would get confused quite a bit with me plugging and unplugging the display. Sometimes it would just stop working altogether until I rebooted. It still didn’t solve my issue of wanting an always-on machine I could use easily if needed.

I had had an iMac previously and knew that I’d really liked it but it had gotten old and I’d replaced it with a Hackintosh build because I figured it would be cheaper to own because I could upgrade and repair it over time, which is actually true, but it was stress- and time-wise very expensive to maintain.

I started looking at the 27” iMac with the lens of “get a machine that is more than I need now so that hopefully it can last several years without becoming an issue”. Comparing the prices of a totally maxed out 27” iMac to the iMac Pro still had about a MacBook’s price worth of difference, though.

I agonized over this for several days but I found a local computer store that was having a $1000 off sale on all iMac Pros but then also had one that was open-box for $500 less than the sale price. This made the price difference low enough to take a chance on.

## Performance

Unless you’re one of those super wealthy people who want an iMac Pro just because its Space Grey appearance is unique and a status symbol, you probably bought an iMac Pro for its supposed performance.

I’m pleased to say that the performance of it has been exceptional when applications are able to take advantage of its cores. I don’t do much of the typical multi-core stuff you see advertised, such as 4K video rendering or VR development.

Unfortunately I do a lot of Node.js development, and unless the code is very specifically written to run multithreaded I will run into cases where a single core is maxed out and slow while the rest are idle. This can be very annoying when running tools like `tslint` or `prettier` on large codebases in VS Code, which can completely seize the app or make scrolling impossible with strange artifacts like linting warnings rendered in VS Code on ranges that make no sense. These are engineering problems and not iMac Pro specific, but I had hoped that the iMac Pro might be so over-powered it could compensate for it anyway.

Outside of tricky single-threaded things like Node, the performance is pretty much insane. It’s almost annoying sometimes: it’s like you don’t get a break. On previous computers I’d sort of subconsciously know that when I started some app or ran some command I’d have a brief pause where I could do something else (take a drink of water, perhaps) but on this machine it will be basically instant and then I feel like I _must_ continue on immediately without taking that moment to pause.

Launching apps is mostly instant and I am never annoyed at the machine. Ironically, the iMac Pro is kind of unremarkable in a good way: it never gets in my way and I commonly forget that it’s not, in fact, limitless. I just do what I need to do and it does it easily. I can hear its fans if the room is quiet enough (though I am very sensitive to sound: Autism) but usually it’s easy to not even realize when I’m working it pretty hard.

> Ironically, the iMac Pro is kind of unremarkable in a good way: it never gets in my way and I commonly forget that it’s not, in fact, limitless.

Compiling code is ridiculously fast and effortless (as effortless as compiling code can be anyway). I can become spoiled at times when I don’t realize how much work it’s doing at a given time: such as syncing iCloud Drive, compiling and installing a complex Node project, watching source and rebuilding with Webpack, and watching a 4K YouTube video all at the same time. Usually any time there is a noticeable performance problem it’s related to my ISP bandwidth.

I use an external 4K display with it and have never had any graphics problems. I’m a heavy user of Spaces and full-screening apps so there are very frequent whole-screen animations (though I realize they are relatively simple compositing renders rather than complete re-renders) as I’m moving around rapidly and I’ve never seen it stutter while rendering its 5K display and the 4K external.

As I am starting to get more into ML experiments, I feel pretty confident that I have a lot of computational runway for experimenting in future years, but even if I don’t continue that interest, I feel like this machine will serve my existing needs for years and resist slowdowns from future macOS features pretty well.

## Value

I’m very pleased with it. Whether I would have been just as pleased with a maxed out non-Pro iMac, I cannot be sure. But as I didn’t pay anywhere near full price for it, I feel pretty good about my purchase. It’s a powerful machine that enables me to do whatever I want to right now without feeling limited. I haven’t done the math but I’m certain it’s easily paid for itself months ago from client work alone without even considering any wellbeing and workflow benefits. Though with that said, I don’t really see myself upgrading to the latest iMac Pro regularly: I think I’ll be sticking with this machine for many years to come.

---

<sup>1</sup> I liked this Hackintosh machine a lot but it was bulky, noisy, and very inconvenient at times due to missing so many things I had to supplement with bulky/messy alternatives such as speakers, webcams, etc. It was also annoying dealing with software glitches and upgrading macOS to find my whole machine was broken and spending a whole day digging in kext files trying to figure out esoteric driver issues.
