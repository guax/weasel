Dawkins Weasel
==============

This program is an implementation of the
[Richard Dawkins _weasel_ program](http://en.wikipedia.org/wiki/Weasel_program).

It is designed to simulate selection of the fittest using strings. Its
algorithm is quite simple and pretty nice to see working.

The program run in the following steps:

1. Make a random string with the size of the target string
2. Make a hundred copies of that string with a chance of "mutation"
of each character of 5%
3. Select the string with the highest number of matching characters as
the fittest
4. Repeat step 2 with the fittest until you get the target phrase

The result is a staggering low number of iterations (generations) to
get to the final string. If you run the program by just generating
random strings you will probably never see the target string getting
formed.

Interesting Stuff
=================

Two things caught my attention on playing with this algorithm. The first
one is the incredibly low number of generations necessary to get to the
desired string. At first I forgot to breed the next generation with
the fittest creating a very small chance of getting the right string.
Those big numbers increased my surprise when I fixed the bug
and in a lot of times fewer then 50 generations where enough to
get the desired result.

The second thing that caught my attention was the fact that characters
changing from the right to the wrong letter is not enough to deter
the result from being achieved very quickly. Curiously I found that
changing the mutation chance alters drastically the outcome.

Chance of Mutation
------------------

Playing with the variables I found the existance of a threshold when
the mutation helps you to get to the desired output faster. Any lower
or higher will turn the mutations not fast enough or too destructive
to achieve any result. As you increase the chance of mutation more generations
are needed because a lot of "reverse" evolution happens. That remembered me of a
[TEDx talk](http://www.youtube.com/watch?v=BBao3D6sBto) I saw last year
that presents this threshold as one of the factors that allow life to thrive.
