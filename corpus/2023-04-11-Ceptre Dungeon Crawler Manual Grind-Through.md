# 2023-04-11-Ceptre Dungeon Crawler Manual Grind-Through
Ceptre:
```
max_hp 10. damage sword 4. cost sword 10.

context init_ctx = {init_tok}.
```
Fact base is now
```
max_hp (10 _)
damage (sword 4)
cost (sword 10)
init_tok
stage (init _)
```

The first stage in the source code becomes the default stage.

---

Ceptre:
```
stage init = {
  i : init_tok * max_hp N  -o  health N * treasure z * ndays z * weapon_damage 4.
}
```

Factbase is now:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
stage (init _)
```

Facts `init_tok` and `max_hp (10 _)` were retracted from the factbase because they were used to create a successful left-hand-side pattern match.

---

When *stage init* matches nothing more, it creates a `qui` fact in the factbase.  We have:

Factbase:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
stage (init _)
qui
```
---
Ceptre (top level rule)
```
qui * stage init  -o  stage main * main_screen.
```

Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
stage (main _)
main_screen
```

---
Ceptre: stage *main* is interactive, so the user is asked for 1 of 4 choices
1. rest
2. adventure
3. shop
4. quit

---

Let's say that the user selects *adventure*.

This selection fires the Ceptre rule:
```
stage main = {
  ...
    do/adventure : main_screen  -o  adventure_screen.
  ...
}
```

Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
stage (main _)_
adventure_screen
```

---

The stage *main* is run again, but this time matches nothing, producing a `qui`.

Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
stage (main _)
adventure_screen
qui
```
---

Ceptre top level rule then applies
```
qui * stage main * $adventure_screen  -o  stage adventure.
```

Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
adventure_screen
stage (adventure _)
```

---

Cepter now fires rules in stage *adventure*...
```
stage adventure = {
  init : adventure_screen  -o  spoils z.
}
```
Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
spoils (z _)
stage (adventure _)
```

---

Ceptre: stage *adventure* matches nothing more -> `qui`
Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
spoils (z _)
stage (adventure _)
qui
```

---

Ceptre top level rule fires
```
qui * stage adventure  -o  stage fight_init * fight_screen.
```
Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
spoils (z _)
stage (fight_init _)
fight_screen
```

---
Ceptre fight_init rule, *init* fires
```
stage fight_init = {
  init : fight_screen  -o  gen_monster * fight_in_progress.
  gen_a_monster : gen_monster * monster_size Size
    -o monster Size * monster_hp Size.
}
```
Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
spoils (z _)
stage (fight_init _)
gen_monster
fight_in_progress
```

---
stage fight_init exhausted -> `qui`

Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
spoils (z _)
stage (fight_init _)
gen_monster
fight_in_progress
qui
```

---
Ceptre top level rule
```
qui * stage fight_init  -o  stage fight * choice.
```
Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
spoils (z _)
gen_monster
fight_in_progress
stage (fight _)
choice
```
`Choice` is Boolean that says that the human player must make a decision, dynamically.

Ceptre
```
stage fight = {
  do_fight : choice * $fight_in_progress  -o  try_fight. 
  do_flee  : choice *  fight_in_progress  -o  flee_screen.
}
#interactive fight.
```
An interactive stage displays all rules that could match and allows the user to pick one.  

The matches are made, but no right-hand sides are fired.

Once the user make a choice, the RHS of the chosen rule is executed. 

In this example, both `choice` and `fight_in_progress` are in the FB.  Both rules match for those two facts, hence, both rules are displayed as choices to the user. e.g.

Choose:
1. do_fight
2. do_flee

Let's assume that `do_fight` is chosen by the user.  In this case, `choice` is retracted, `fight_in_progress` is retracted and put back in, and, `try_fight` is put into the factbase
Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
spoils (z _)
gen_monster
stage (fight _)
fight_in_progress
try_fight
```

---

Stage is still `stage (fight _)` so we try `stage fight` again.

This time, neither rule matches - because the `choice` boolean has be retracted, so the stage generates `qui`.

Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
spoils (z _)
gen_monster
stage (fight _)
fight_in_progress
try_fight
qui
```
---

Now, the top rule fires
```
qui * stage fight * $fight_in_progress -o stage fight_auto.
```
Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
spoils (z _)
gen_monster
fight_in_progress
try_fight
stage (fight_auto _)
```
---

