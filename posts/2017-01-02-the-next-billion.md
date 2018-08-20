---
title: "Progressive Web Apps and The Next Billion"
category: "Software"
layout: 'post'
tags:
  - Web Development
---

The Next Billion people coming online will be more diverse than the last billion. Their geographic location, familiarity with technology, use contexts, types of devices, and quality of connections will all be different. Additionally, nearly all of them will be using the Web from a mobile device.<!-- more -->

Now is the time to be transitioning from merely “mobile first” to a comprehensive “mobile by default” approach to developing for the Web. This change in thinking requires a web product to be more considerate of the user’s situation and to adapt itself to provide value to the user in a way aligned with their interests.

Some of the challenges faced by The Next Billion are not commonly accounted for when deciding how to create a web product, including:

## Poor connectivity

Many people accessing the web do so with very poor connections, often 2G speeds, that may also be intermittent and unreliable. A person may have cellular connectivity at their workplace but none at home, for example. This is far more common than most would think, even in the USA.

Creators of web products should prioritize creating web products that can provide meaningful value even when connectivity is only available part-time. Think carefully about throwing away downloaded data that might be valuable to the user later. Always keep as much value available offline as possible and do what the user expects. Try not to tease intermittent connectivity users with information they can’t access at the time.

## Expensive connectivity

On top of poor connectivity, often users of the mobile web are highly conscious of the cost of their data usage. Often this is for good reason, as mobile data is generally expensive worldwide, not just in the emerging markets we tend to think of.

Creators of web products should consider this challenge frequently when making decisions. Every byte your application needs costs something. How can you provide more value as cheaply as possible? Use tools like [What Does My Site Cost](https://whatdoesmysitecost.com/) to understand what your users trade to use your product.

## Energy constraints

Mobile devices have finite battery lives. Even in countries with abundant electricity available for recharging, mobile users can often be as conscious and anxious of their available battery as they are of their mobile data usage. In parts of the world with less available (or more expensive) electricity this feeling is even more present.

Creators of web products should understand that users of their product are choosing to _spend_ battery to use it. Creators should be mindful of that fact and develop their products to be efficient as possible to make their battery footprint as small as possible. Avoid expensive animations. Does your web app really need to check the server for updates every 15 seconds?

## Device constraints

Mobile devices also have highly variable specifications. It’s easy to assume that the experience we have with our own smartphones are what the average mobile user experiences as well. This isn’t always true, as the average mobile user, and the Next Billion especially, are typically not using the latest flagship iPhone or Android device.

Creators of web products should be aware of the device constraints of their targeted users. If most of your users are using three-year-old devices with small amounts of memory, low CPU speed, and outdated software versions, you should develop with them in mind. It’s too easy to test our web products on the latest iPhone and not realize the poor performance on older devices.

# Progressive Web Applications

Progressive Web Applications (often abbreviated PWAs) are an up and coming philosophy of developing web products that are adaptive to the factors mentioned above and more. The term encapsulates a strategy of development where code is architected to be aware of the constraints and optimize themselves appropriately.

Generally this includes, at a minimum, using Service Workers to download a mostly-functional version of the app to the device, allowing it to work offline or in spotty connectivity (such as while riding a train, where Internet connectivity could go in and out). Newer technology also allows PWAs to incorporate features previously exclusive to native mobile apps, such as push notifications and the ability to save a PWA to your device’s home screen, where it can be accessed easily again. If the app also includes a Service Worker, that home screen shortcut may work without an Internet connection at all, much like a native application.

I believe that Progressive Web Applications are the future of web development and the best way to ensure that the Next Billion coming online have a fair and consistent Web experience. The Web has revolutionized the lives of billions already, it’s only right that the Next Billion have that same opportunity regardless of the devices and connections available to them.

That is the Web I hope to build: for everyone, everywhere.
