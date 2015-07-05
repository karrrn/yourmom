# How to install Python PYO on Raspberry Pi (Raspian Debian Wheezy)

An old version of PYO is installable via apt-get on Raspian. But, we want the latest, don't we...

## Dependencies

```
sudo apt-get install python-dev libjack-jackd2-dev libportmidi-dev portaudio19-dev liblo-dev libsndfile-dev python-dev python-tk python-imaging-tk python-wxgtk2.8
```

## Checkout PYO

```
# go somewhere you want to pull the sources into
cd /home/pi
# pull the sources
svn checkout http://pyo.googlecode.com/svn/trunk/ pyosrc
# run the install script
cd pyosrc
sudo python setup.py install --install-layout=deb --use-jack --use-double
```

## Run a jack server

```
jackd -m -p 32 -d dummy
```