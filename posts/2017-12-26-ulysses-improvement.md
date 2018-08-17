---
title: 'An improvement I would make to Ulysses'
date: '2017-12-26T23:46:37.121Z'
layout: post
draft: false
path: '/posts/ulysses-improvement/'
category: 'Thoughts'
description:
  'In the Ulysses writing app, you cannot have glued sheets inside a group that is not sorted as Manual. It gets all messy if you switch the group to any other sort order because the glued sheets get re-ordered as well.'
---

In the [Ulysses writing app](https://ulyssesapp.com/), you cannot have glued sheets inside a group that is not sorted as Manual. It gets all messy if you switch the group to any other sort order because the glued sheets get re-ordered as well.

I think this could be solved by treating glued sheets as effectively one sheet for sorting purposes and its collective "creation date" would be the _earliest_ creation date of the sheets inside. The "modification date" would likewise be the _latest_ modification date of the sheets inside.

When shown in a sorted Group the glued sheets would appear in the list among other non-glued sheets in the appropriate spot given those derived values. Inside the glued sheets they would maintain their original order (which inside a glued sheet is always explicitly manual).

This idea seems really obvious to me, which makes me suspect it has some consequence that I'm not thinking of which is the reason the developers have not already done this.

This odd restriction of Ulysses has me having Groups to contain a single instance of glued sheets. This is kind of annoying because the groups themselves are of course ordered manually and I'd like them to be somewhat ordered. I guess though I can easily do an insertion sort where just every time I make a new one I specifically put it at the top in its subgroup and this would keep the list ordered in reverse chronological order.

Since the particular case I'm thinking of is my Book Notes I am somewhat concerned that this list of groups could get extremely long and cumbersome. Maybe that's okay, though, because I could just search for whatever I needed.
