# thanks-giver

Install the Raspbian image onto your Pi if you've yet to do so.

Next, open terminal and use the following to install the PaPiRus library.

<pre>curl -sSL https://goo.gl/i1Imel | sudo bash</pre>

You'll need to set the screen size for the ePaper. The longer screen for the PaPiRus Zero is 2". By using the following code, you can set the size and have a look at other options for the HAT

<pre>sudo papirus-config</pre>

Reboot for the changes to take effect

<pre>sudo reboot</pre>

These next steps will install the library and driver

<pre>git clone https://github.com/PiSupply/PaPiRus.git</pre>

<pre>cd PaPiRus</pre>

<pre>sudo python setup.py install</pre>

<pre>sudo papirus-setup</pre>

Next, you'll need to install the thanksgiver.py file. We'll edit the contents in a minute.

<pre>sudo git clone https://github.com/AlexJrassic/thanks-giver.git</pre>

If you open this file up, you'll see a list of things to be thankful for. Here is where you can change the contents. Just make sure you don't lose any of the code when you do. Save the file and close it.

You may need to rotate the screen. I had to in order to fit in the box. This explains the papirus-write code within the thanksgiver.py file. If you don't need to rotate the screen, ignore it. If you do, follow this step.

Open /home/pi/papirus/somethingsomethingsomething and add the following line to the bottom.

Lastly, you'll need to open terminal and tell the Pi to run the script on reboot. To do this, type:

<pre>nano ~/.config/lxsession/LXDE-pi/autostart</pre>

At end of the file, add this line:

<pre>@python /home/pi/thanks-giver/thanks-giver.py</pre>

Save and reboot.
