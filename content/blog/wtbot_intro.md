Title: War Thunder bot : Intro
Date: 2016-02-07 17:24
Modified: 2016-02-07 17:24
Category: Misc
Tags: warthunder, python
Slug: wtbot_intro
Authors: Jason Hamilton-Smith
Summary: An introduction to my project to build a bot for the game War Thunder.

Today I am going to talk about a project I started a short while ago. This post
is just an overview, and I will continue with a series about the project in
greater depth, probably I will have the next post up later this week.

The project in question is a bot (a program that automates playing) for the
game [War Thunder](https://warthunder.com/). I initially became interested in
this when I flew bombers for a few missions and noticed how "robotic" it is to
do so, following the same set of actions each match with little ability to
react to changing situations: flying a bomber is exactly what this bot will do.
But first:


Disclaimer
==========

Because of the issues arising around the War Thunder terms of service and the
general moral ramifications of such a piece of software, I will only be
running this bot in practice mode and/or offline custom missions where they
will not interfere with the War Thunder service or game experience.

Furthermore I will **not** be releasing any substantiate code or material
that would enable others to create their own bots, this blog series will only
contain general overviews of the techniques used.

This project is solely for research and educational purposes, not for cheating.


Design Goals
============

Of course, I say "flying a bomber" and that could mean many things. When I
say this I am referring to the large four engine bombers. And, given a large
bomber, the tactic I will be using is high altitude level bombing. The mission
will be as follows:

1. Take off from the runway.
2. Find a safe corner of the battlefield and fly to it.
3. Fly in a helix, ascending until at some desired altitude.
4. Fly to the bomb site, and drop bombs.
5. Fly back to base, descending in altitude.
6. Land.

A lot of this isn't possible in a "normal" War Thunder game, for example most
maps have bombers begin already in the air rather than on a runway, also most
matches of War Thunder don't last nearly long enough for this mission. Because
of these factors I will be flying in practice mode, and be using the single
truck that spawns in the middle of the map as a bomb target.

Requirements
============

There are some factors that would make doing the above easier. In order to
better learn, I will be restricting myself out of some of them.

* No or minimal use of the readout the game provides on port 8111, I will fall
  back to using it if absolutely necessary, but I want to do as much as I can
  through computer vision, and for the purposes of this project I consider
  using the data exposed here "cheating".
* No looking at the graphics buffer or network traffic. As with the above I
  consider it "cheating". Also, I have no idea how to do one of these things
  and the other is too similar to my day job to be anything but tedious.
* Difficulty set to "Realistic Battles", respecting proper aerodynamics and
  having planes that can actually stall is important. I might consider
  extending the bot towards "Simulator Battles" a stretch goal.
* Big planes, I want the bot to fly a plane that can't just turn on a dime
  and needs the controls to be handled carefully. A manoeuvrable fighter would
  be too easy to steer.
* Practice mode only, possibly an offline custom map if practice mode proves
  unsuitable.


Next Post
=========

I will be posting my first update, hopefully later this week. It will be about
using OpenCV in Python to read the plane instruments from the glass cockpit
view. Keep tuned!
