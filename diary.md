## 5-29-2018 (retrospect from 5-30-2018)

Got the damn thing working.  This has been a lesson (and probably a standard practice in the professional world) of amplifying pulse from ~50mA to a logic-worthy voltage to be read with an SR latch.

My two options I considered were using a transistor or an analog comparitor.

I wound up creating a reference voltage that was offset by about 10mV and feeding it to the comparitor.  After figuring out that I needed to pull the pins on the SR latch high by default and drain them to set the latch, I finally got a steady pulse.

R1 = 4k
R2 = 50
R3 = 6K

<Hopefully insert a schematic here>

I am reading the pulse into an sr latch because... it makes sense to me.

## 5-30-2018
The next problem in the line to tackle is the fact that what goes up must come down.  When sending a pulse through a core currently, I am expecting data to come in the form of a pulse in a certain direction.  To be perfectly honest, I don't even remember if that's positive or negative... positive I think, but that's beside the point.  However, when disabling the pulse, the change in current will cause a negative pulse in the opposite direction.

When addressing a single core, this isn't a problem at all.  The comparitor that converts the analog signal to digital will not be triggered, as the read voltage drops further beneath the reference voltage instead of crossing it.  However, when scaling this up to multiple cores, they will be addressed by sending inhibit pulses against a guranteed driving pulse.  These inhibit pulses should be at least as much as the driving pulse, but will likely be much greater.  The kickback from these inhibit signals returning to neutral will cancel out the fact that it's a negative pulse, meaning we get a positive signal and read a bit where there is none.

I considered a few options to resolve this:

* Careful timing of the read pulse and the write pulse.  I disregarded this as it put some restriction on the timing of this memory and also would likely cause a great deal of power consumption at the same time
* Logic diode between the sense line's two ends.  I shoved one in and it didn't work.
* Logic mumbo jumbo crap to ignore a pulse. I went with this option, opting to use an "or" gate driven by the logic pulse and the arduino.  I can set a pin in code to block any pulses from reaching the sr latch.  

<Hopefully insert a schematic with additional hardware here>

I tried to set this pin without any delay just to see what would happen, and the 74HC32AP seemed to take the tempo of everything without problem.

```
void readAddress(){

  digitalWrite(P_ADDRESS_0, PULSE_START);

  delay(PULSE_WIDTH);

  //Setting this high means the sense pulse is blocked before setting the latch
  digitalWrite(DONTREAD_PIN, HIGH);      

  digitalWrite(P_ADDRESS_0, PULSE_END);

  digitalWrite(DONTREAD_PIN, LOW);   

}
```

I made a few tweeks to clean up the code and bump up the 'supposed' frequency to about an attempt of 1KHz.  Reading the output bit on my DS0138 official oscilliscope, I wound up with something closer to 20KHz.  I wasn't expecting the timing to be this far off, but I had expected it to be pretty inaccurate since I'm timing this with vanilla delays instead of anything legit like a PMW or interrupt.

To play around with this further, I adjusted the number to get as close to 59Hz as possible according to my osc.  The magic number was actually 1000/52 ms, quite a bit off once again, and it reads 62Hz on the osc.  Still, that little offset from 60Hz is enough for me to pull out my cellphone and record the strobing this is causing.  I don't know if this confirms that the osc is more accurate in this reading or whatever, but it sure it cool to watch.

<Hopefully insert that gif here>
