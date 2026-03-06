# 2023-03-25-StateChartsI think that all I did was read the paper.  It appears to be 50-ish pages long, but it's all pictures.

What I got from it:
- diagrams can be programs
- "parental authority" instead of "inheritance".

Harel doesn't point this out but his StateCharts make sense and aren't "too busy".  Children cannot override the operation of a parent, hence, every picture makes stand-alone sense.  "Inheritance" doesn't guarantee stand-alone-ness.  StateCharts do.  I'm using the term "Rule of 7" these days as a way to talk about programs that aren't "too busy" to understand at any level.

Harel - inadvertently? - figured out how to conquer the "state explosion" problem.  If you lay out a state machine on an infinite canvas, no one can understand it - too much detail - and, the amount of details becomes exponentially worse as you add states ("The State Explosion Problem").  

The trick is to find a way to lasso details and to suppress them.  Lambdas are one way to do this.  YACC and the Dragon Book are another way to do this.  StateCharts are yet another way to do this, in a way that you can confidently draw on a whiteboard.

The difference is subtle, yet, powerful.

# Appendix - StateCharts Paper

https://guitarvydas.github.io/2020/12/09/StateCharts.html
