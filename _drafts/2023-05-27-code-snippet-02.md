---
layout: post
title:  "Code Snippet #2"
date:   2023-05-27
categories: rust leetcode programming dynamic code coding 
---


In todays Code Snippet, we will tackle LeetCode #[1406](https://leetcode.com/problems/stone-game-iii/).



## Problem

There are stones arranged in a row each stone had an associated value in the array `stoneValue`. Alice and Bob alternate turns and on each turn, may take 1 2 or 3 stones from the first remaining stones in the row.

![stones](/assets/img/stones-diagram.png)


The score of each player, Alice and Bob, is the sum of the values of the stones taken. The score of each player is 0 to start. The most points, you win!

_Assume Alice and Bob player optimally_

In LeetCode, the values we need to return are `"Alice"` if Alice wins and `"Bob"` if Bob wins and finally a `"Tie"` option.


## Analysis


On first glance, it looks like we will be using recursion is this. The "play optimally" means that during whomever's turn it is, they will make a winning move if possible. As an example, if the stone values array is `stoneValue = [1, 2, 3, 8,]`. Alice always goes first so she cannot win this match, she must make the best move stones 1,2 and 3, while Bob takes the stone worth 8.

So to get an idea of all the options that are available for turns;

![stones-set](/assets/img/stone-diagram-set.png)

For every move that Alice opens with, there is either an obious win or a win by pattern (like the first set wouldn't really ever happen in a game, Bob would just take all 3 to win immediately.)

On that note, we have to make sure that each player is playing ___optimally___ ??

Each move must either 