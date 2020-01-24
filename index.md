---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: home
layout: default
permalink: / 
---


<h2>welcome</h2>

Hey! My name is Carter Tomlenovich, on the internet I go by Hyperlisk. I enjoy programming and
recording music. This website is all about my programming experience and contains a few things I need and
hopefully things that some other people might find cool. A tutorial for a few languages, some mistakes
I've made along the way and some interesting things I have encoutered will be on this site. 


<h2>programming experience</h2>

    |-------------------------|
    | Language --- Experience |
    |-----------|-------------|
    | Elixer    |      4      |
    | C++       |      6      |
    | Java      |      7      |
    | Python    |      7      |
    | Rust      |      3      |
    |-------------------------|

I have a very good understanding of Python and Java. Most of my projects are built in Java. Lighter things and math related projects are built in Python.

C++ and Rust are languages I learned because of a quick scourge into microelectronics and circuitry. 

Elixer was just something I tried because it was different. Not a whole lot of use cases for me personally.


<h2>projects</h2>

{% for project in site.data.projects %}
<a href="{{project.url}}">{{project.name}}</a><br>
<p> &emsp; - {{ project.desc }} </p>
{% endfor %}
<br>



