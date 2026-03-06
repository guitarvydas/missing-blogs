# 2022-07-08-Working Paper Thinking About Building A DemoI don't know how to do this, if you do, tell me:
I want to embed draw.io diagrams in a web page, then suck their output into Javascript (and process the output using Javascript).

background: I've got a way to compile draw.io diagrams to JSON, I've got a way to compile text-based components (Leaf/Container/State-Machine) to Python.  I want to consolidate these pieces into one demo page.

easy: if this isn't easy, tell me, but don't waste time on it. I'm just trying to avoid a learning curve for me on the assumption that this is easy if you already know some background details.  What I've got mostly works on the command line, but, I want to lift this stuff into a webpage for a demo (and to continue development).

more background: git clone https://github.com/guitarvydas/pypm.git, then open pypm/tbx/index.html in a browser.  Click on "Test".  I want to replace the yellow ("old lace") windows with draw.io diagrams of the code.

more more background: I'm "testing" my diagram stuff by building a real program to copy a bunch of files (I could do this with a shell script, but I want to eat my own dogfood)

more more more background: Composability doesn't come from diagrams, it comes from 0D (zero dependencies).  If you have 0D, you get diagrams "for free".  You, also, get concurrency "for free" if you have 0D.  0D is easy to do in text programming if you know that you want it.  I see how to do 0D in Python, JS, etc.  Thinking about diagrams and concurrency backed me into 0D.