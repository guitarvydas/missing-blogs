# 2022-06-07-Language Theory vs PEG ParsingThe gear-box effect of over-use of low-level synchronization is seen, in microcosm, in the Language Theory vs. PEG Parsing technologies.

They *look* the same, but lead to wildly different approaches to thinking about solutions.

Example: Let's say that you want to instrument a C program.  You want to find every block enclosed in braces `{ ... }` and insert a line of code (say, a printf())/

This sounds like a simple bulk-edit operation.

If you only have gear-boxes at your disposal, you have to write a Language specification that covers every millimeter of *all* C programs in the world.

If you have a parser-builder DSL, like PEG, then you can write a much simpler grammar that matches balanced brace-brackets and skips over "everything else".

Here's an example of a simple PEG-ish grammar (done in Ohm-JS, which is a better PEG, IMO):

```
balanced {
  main = matched main?
  matched =
    | "{" main "}" -- nested
    | anythingelse+ -- bottom
  anythingelse = !"{" !"}" any
}
```

The above grammar recognizes the first example, "Snake game", in https://ssiddique.info/20-c-game-projects-for-beginners-with-source-code.html.

The above grammar doesn't *do* anything with the matches, it simply captures them.  

Other PEG libraries should be able to do the same kind of thing.

LR(k), though, requires that a full grammar for C be written.  This turns what should be a simple batch-edit into a mega-project.

I wouldn't use the above Ohm-JS grammar for Production Engineering, but, I might use it to make my life easier during development.

To *do* something (like insert printf()s), you have to write a bit more code.  Not a lot of code, just a bit.

A full-blown Ohm-JS app to insert `printf ()`s after every `{` and before every `}` is shown below


## Inserting Printfs

# Grammar
```
balanced {
  main = matched main?
  matched =
    | "{" main "}" -- nested
    | anythingelse+ -- bottom
  anythingelse = !"{" !"}" any
}
```

# Rewrite Rules
```
  const rewriteRules = {
      main: function (_matched, _optmain) {
	  var matched = _matched.walk (this.args.depth);
	  var optmain = _optmain.walk (this.args.depth);
	  return matched + optmain;
      },
      matched_nested: function (_lb,_block_in, _rb) {
          // "lb" means "left brace", "rb" means "right brace"
          var depth = this.args.depth;
          var block_in = _block_in.walk (depth + 1);
          return `\{\nprintf(">> enter depth ${depth}");\n${block_in}\nprintf("<< exit depth ${depth}");\}`;
      },
      matched_bottom: function (anythingelse) {
          return anythingelse.walk (this.args.depth).join ('');
      },
      anythingelse: function (c) { return c.walk (this.args.depth); },
      
      // required by Ohm-JS...
      _terminal: function () { return this.sourceString; },
      _iter: function (...children) {
	  var n = this.args.depth;
	  var r = children.map(c => {
	      var mapr = c.walk (n);
	      return mapr;
	  });
	  return r;
      }
  };
```
# Source Text
see [Snake Game](https://ssiddique.info/20-c-game-projects-for-beginners-with-source-code.html)

```
// taken from https://ssiddique.info/20-c-game-projects-for-beginners-with-source-code.html snake game
// C program to build the complete
// snake game
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int i, j, height = 20, width = 20;
int gameover, score;
int x, y, fruitx, fruity, flag;

// Function to generate the fruit
// within the boundary
void setup()
{
  gameover = 0;

  // Stores height and width
  x = height / 2;
  y = width / 2;
 label1:
  fruitx = rand() % 20;
  if (fruitx == 0)
    goto label1;
 label2:
  fruity = rand() % 20;
  if (fruity == 0)
    goto label2;
  score = 0;
}

// Function to draw the boundaries
void draw()
{
  system("cls");
  for (i = 0; i < height; i++) {
    for (j = 0; j < width; j++) {
      if (i == 0 || i == width - 1
          || j == 0
          || j == height - 1) {
        printf("#");
      }
      else {
        if (i == x && j == y)
          printf("0");
        else if (i == fruitx
                 && j == fruity)
          printf("*");
        else
          printf(" ");
      }
    }
    printf("\n");
  }

  // Print the score after the
  // game ends
  printf("score = %d", score);
  printf("\n");
  printf("press X to quit the game");
}

// Function to take the input
void input()
{
  if (kbhit()) {
    switch (getch()) {
    case 'a':
      flag = 1;
      break;
    case 's':
      flag = 2;
      break;
    case 'd':
      flag = 3;
      break;
    case 'w':
      flag = 4;
      break;
    case 'x':
      gameover = 1;
      break;
    }
  }
}

// Function for the logic behind
// each movement
void logic()
{
  sleep(0.01);
  switch (flag) {
  case 1:
    y--;
    break;
  case 2:
    x++;
    break;
  case 3:
    y++;
    break;
  case 4:
    x--;
    break;
  default:
    break;
  }

  // If the game is over
  if (x < 0 || x > height
      || y < 0 || y > width)
    gameover = 1;

  // If snake reaches the fruit
  // then update the score
  if (x == fruitx && y == fruity) {
  label3:
    fruitx = rand() % 20;
    if (fruitx == 0)
      goto label3;

    // After eating the above fruit
    // generate new fruit
  label4:
    fruity = rand() % 20;
    if (fruity == 0)
      goto label4;
    score += 10;
  }
}

// Driver Code
void main()
{
  int m, n;

  // Generate boundary
  setup();

  // Until the game is over
  while (!gameover) {

    // Function Call
    draw();
    input();
    logic();
  }
}

```
# Final Code
Load this into a browser and hit the "Insert Printfs" button.

```
<!DOCTYPE html>
<html>
<head>
<style>
textarea {
}
</style>
</head>
<body>

<h1>Example PRINTF Inserter</h1>

<p>source:</p>
<textarea id="src" rows="5" cols="90" placeholder="markdown" style="background-color:oldlace;">
// taken from https://ssiddique.info/20-c-game-projects-for-beginners-with-source-code.html snake game
// C program to build the complete
// snake game
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int i, j, height = 20, width = 20;
int gameover, score;
int x, y, fruitx, fruity, flag;

// Function to generate the fruit
// within the boundary
void setup()
{
  gameover = 0;

  // Stores height and width
  x = height / 2;
  y = width / 2;
 label1:
  fruitx = rand() % 20;
  if (fruitx == 0)
    goto label1;
 label2:
  fruity = rand() % 20;
  if (fruity == 0)
    goto label2;
  score = 0;
}

// Function to draw the boundaries
void draw()
{
  system("cls");
  for (i = 0; i < height; i++) {
    for (j = 0; j < width; j++) {
      if (i == 0 || i == width - 1
          || j == 0
          || j == height - 1) {
        printf("#");
      }
      else {
        if (i == x && j == y)
          printf("0");
        else if (i == fruitx
                 && j == fruity)
          printf("*");
        else
          printf(" ");
      }
    }
    printf("\n");
  }

  // Print the score after the
  // game ends
  printf("score = %d", score);
  printf("\n");
  printf("press X to quit the game");
}

// Function to take the input
void input()
{
  if (kbhit()) {
    switch (getch()) {
    case 'a':
      flag = 1;
      break;
    case 's':
      flag = 2;
      break;
    case 'd':
      flag = 3;
      break;
    case 'w':
      flag = 4;
      break;
    case 'x':
      gameover = 1;
      break;
    }
  }
}

// Function for the logic behind
// each movement
void logic()
{
  sleep(0.01);
  switch (flag) {
  case 1:
    y--;
    break;
  case 2:
    x++;
    break;
  case 3:
    y++;
    break;
  case 4:
    x--;
    break;
  default:
    break;
  }

  // If the game is over
  if (x < 0 || x > height
      || y < 0 || y > width)
    gameover = 1;

  // If snake reaches the fruit
  // then update the score
  if (x == fruitx && y == fruity) {
  label3:
    fruitx = rand() % 20;
    if (fruitx == 0)
      goto label3;

    // After eating the above fruit
    // generate new fruit
  label4:
    fruity = rand() % 20;
    if (fruity == 0)
      goto label4;
    score += 10;
  }
}

// Driver Code
void main()
{
  int m, n;

  // Generate boundary
  setup();

  // Until the game is over
  while (!gameover) {

    // Function Call
    draw();
    input();
    logic();
  }
}
</textarea>


<p>modified:</p>
<textarea id="output" rows="27" cols="90" placeholder="transpiled"  readonly style="background-color:whitesmoke;">
</textarea>
<br>
<br>
<p id="status" > READY </p>

<!-- Ohm-JS -->
<script src="https://unpkg.com/ohm-js@16/dist/ohm.min.js"></script>


<br>
<button onclick="insert ()">Insert Printfs</button>
<script>

const grammar = ohm.grammar(String.raw`
balanced {
  main = matched main?
  matched =
    | "{" main "}" -- nested
    | anythingelse+ -- bottom
  anythingelse = !"{" !"}" any
}
`);

  const rewriteRules = {
      main: function (_matched, _optmain) {
	  var matched = _matched.walk (this.args.depth);
	  var optmain = _optmain.walk (this.args.depth);
	  return matched + optmain;
      },
      matched_nested: function (_lb,_block_in, _rb) {
          // "lb" means "left brace", "rb" means "right brace"
          var depth = this.args.depth;
          var block_in = _block_in.walk (depth + 1);
          return `\{\nprintf(">> enter depth ${depth}");\n${block_in}\nprintf("<< exit depth ${depth}");\}`;
      },
      matched_bottom: function (anythingelse) {
          return anythingelse.walk (this.args.depth).join ('');
      },
      anythingelse: function (c) { return c.walk (this.args.depth); },
      
      // required by Ohm-JS...
      _terminal: function () { return this.sourceString; },
      _iter: function (...children) {
	  var n = this.args.depth;
	  var r = children.map(c => {
	      var mapr = c.walk (n);
	      return mapr;
	  });
	  return r;
      }
  };

  function insert () {
      let src = document.getElementById('src').value;
      let matchResult = grammar.match (src);
      if (matchResult.succeeded ()) {
          document.getElementById('status').innerHTML = "OK";
          let sem = grammar.createSemantics ();
          sem.addOperation ('walk (depth)', rewriteRules);
          let treeWalker = sem (matchResult);
          let text = treeWalker.walk (0);
          var s = text.toString ();
          document.getElementById('output').value = s;
      } else {
          document.getElementById('status').innerHTML = "parse FAILED";
      }
  }
  </script>
</body>
</html>

```
# Github
[cparse](https://github.com/guitarvydas/cparse)