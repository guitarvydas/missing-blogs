# 2022-06-07-Parts of Programming
I think of programming in terms of *divide and conquer*.  Very roughly, programming breaks down into two (2) steps:

1. grok
2. re-format


Step (1) consists of understanding the input, whatever it is.  
- For websites, the input is data sent in by users.  In some cases, the input comes from a browser-based *form* while in other cases the input is less-organized and results from users pushing buttons in their browsers.  The button pushes are translated into arbitrary actions usually programmed-in as Javascript code attached to the buttons.  (See below, computer-to-computer input). 
- For spreadsheets, the input is a grid containing numbers and formulae.
- For internet-based computers, the input is information sent in by other computers.  Often this data is formatted as a stream of text usually called a *request*.
- For compilers, the input is usually a text file containing textual instructions that are meant to control the machine (an electronic computer), and, simlutaneously document the intentions of the original programmer so that other programmers could understand what is being done.

In step (2), programmers write scripts ("code") that send commands to the computer or requests for more information, based on the information contained in step (1).

Step (1) is often tangled up with the concepts of UX (User-eXperience) and break down into two parts, too:

3. Presenting data to users.  This should be the job of graphic designers and artists, but is usually tangled up with programming and tends to depend on the UX skills of technical programmers.
4. Accepting data from users in the form of modifications to the presentations (e.g. button pushes, arrow keys on the spreadsheets, keyboard inputs in text boxes) and then attempting to comb through it and organize it and pattern-match it in ways that make step (2) easier.  This step is, also, tangled up with what we call *programming*, and tends to depend on the engineering skills of programmers.  Usually if a programmer is a good Engineer, then the programmer's skills tend to be shallow in the UX department and vice versa.  What we currently call *programming* tends to involve all of the above, tangled up together.  The lack of separation between the various parts of programming results in uneven results.  Usually an app ("application") is either better in the UX department or better in the niggly-details department, but, usually not both.  Sometimes, programmers are generalists who have honed their skills in both departments, resulting in apps that are satisfying to users and to implementors of step (2).  Such balanced apps are rare and tend to become "overnight successes".

Note that the film and television industry has learned how to divide up work between graphic artists and programmers.

The gaming industry seems to have learned some orgnizational lessons from film and TV and seems to have advanced further into dividing the steps for programming games, than most other realms of programming.

The website-building industry is, also, learning to divide work up.  We see .html files for creating websites an we see .css files added to websites to "paint" them and allow for improved graphic-design of websites separated from the niggly details of simply making the websites function.