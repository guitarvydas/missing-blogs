# 2022-11-18-Simple Example for HSMs
> I think the next step for me would be to build a small application with py0d. What's a good simple use case to play with? 

Simple example:
1. a Lamp
2. it has 2 toggle buttons
	1. power ON/OFF
	2. intensity (low, medium, high)

When you hit the power button, it turns the lamp on.  When you hit the power button again, it turns the lamp off.

When the lamp is ON, hitting the INTENSITY button cycles between LOW-MEDIUM-HIGH intensity.

When the lamp turns OFF, the inner INTENSITY state is reset (to the "default").  You can imagine more than this, e.g. Harel's History notation, but this is enough for a simple example.
