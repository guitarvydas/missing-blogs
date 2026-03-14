# 2022-06-07-Mind Virus of Over-Synchronization
I think that our approach to programming stems from culture.

The cultural mind-virus begins in the over-use of low-level synchronization.

You can't have "physical objects" if they are all joined at the hip.  Most programming languages over-use synchrony and make all programs into big gearboxes.  Humans learn to intuit the other way around - everything is independent and not joined at the hip.

Over-use of low-level synchrony makes all apps into gear-boxes, rife with dependencies.  Tweak an item over here and that thing, over there, starts working differently.

If you build apps that are gearboxes, the apps are brittle.  If you build IDEs that are gearboxes, the IDEs are brittle.  If you build type systems that are gearboxes, the type systems are brittle.

Analysis of programming might need gearboxes, but gearboxes are less good as UXs for non-analysis-oriented programming.

Can we get rid of dependencies?  I argue: yes.

