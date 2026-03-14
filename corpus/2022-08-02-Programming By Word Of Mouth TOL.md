# 2022-08-02-Programming By Word Of Mouth TOL
# Programming By Word Of Mouth

Thinking out loud (TOL):

- speak a program
- transcribe the speech to text via AI (e.g. MacOS Dictation)
- parse phrases in the transcribed text and compile
	- in 
## 2022-08-02-Game Creation DSL Screencast

[Game Creation DSL](https://share.descript.com/view/zkWE3JedKb5)
, I show how to use Ohm-JS to parse a variety of phrases and transpile them to JSON

# Research Questions
- "um"
	- remove "um"s (like in Descript)?
	- write an Ohm rule that considers "um" to be whitespace?
- edit transcription errors
	- Descript allows you to edit the transcribed text in a word-processor-like app
	- reduce transciption errors by training the AI in programming language
		- make a cheat sheet of acceptable phrases (like a programming language reference document)
- do we "relax" the idea of a programming language to allow multiple ways of saying / accomplishing the same action?
- what is an IDE for this?
- new kind of game - visual D&D, based on Descript storyboard ideas?
- no need to parse all kinds of prose, restrict allowable phrases (just like textual programming languages of today)


# Notes
- synthesizing a variant of storyboard game
	- speech-to-text
	- allow only certain phrases
		- e.g. "turn right"
		- e.g. "turn left"
		- e.g. "open door"
		- e.g. "pick up"
	- text transpilation
	- baby steps
		- speech-to-Lisp
			- speech-to-text (Apple Dictation, Descript)
			- text-to-code - Ohm-JS
				- e.g. [2022-08-02-Game Creation DSL Screencast](#2022-08-02-game-creation-dsl-screencast)
- synthesizing a variant of storyboard game
	- speech-to-text
	- text-to-action
	- break whole problem down into small pieces, first
	- Descript-like storyboard to create many visual assets
		- string assets together into a live story
- speech recognition games:
	- https://www.thegamer.com/games-with-voice-commands-speech-recognition/

---

strange thoughts: All of pieces to do a Visual/VoiceRecognition version of Adventure are on my laughtop: Apple Dictation converts Speech To Text, Ohm-JS can recognize a certain set of phrases and convert them to code (JSON, Lisp, JS, Python, C++, etc., etc.). Discord / iMovie / Davinci for making visual scenes.  Programmers could use voice-recog to specify rooms.  Gamers could use voice-recog for wandering inside the game ("turn left", "turn right", "open door", "pick up", etc.).  Torlisp is next Tuesday,speech-to-lisp would make an interesting demo...