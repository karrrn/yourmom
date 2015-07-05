
# DIY prank phone 

That document is supssed to give a brief documentation what to do to build a voice transformer into an old telephone for prank calls. 
(I am sure what I have been doing is an overkill anyways)

## You need:

* an old digital telephone
* rasberry pi
* 2 jacks
* the cheapest soundcard you can find

## Instructions

### Step 1: speaker and mic to soundcard to raspberry

First we wonna hook up the telephone speaker and mic to some old jacks. Next, jacks go into sound-card, goes into Raspberry.
Finally, checking functionality and setting up the sound card. Never forget testing at any stage eg. with stereo/ other computer
If you know the speaker/mic work with the sound card on your unbuntu install all on raspberry like this:

	lsusb ...you should see soundcard
	sudo nano /etc/modprobe.d/alsa-base.conf
	->options snd-usbaudio index=0

reboot the system and test with 
	
	speaker-test -c2 -D hw:0,0 


## Step 2: Voice transformation

I choose to believe **pyo** is a good choice for real time audio signal processing. A description of how to install pyo on the Raspberry is in the voice transform folder.
A script for pitch transformation is in the same one. More transformations on its way.

## Step 3: Hooking up the key pad

Key pads usually come in a matrix style. 

(That's how they work)[]

## Step 4: Hooking up the old lcd screen (optional)

## Step 5: Tetecting that somebody got hte phone (abheben/SChalter)

## Step 6: Skype in bash

## Step 8: Store Audio stream somewhere?? Server from jobim?:)

## Step 7: Bringing it all together

