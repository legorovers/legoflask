LegoFlask
===========

A Flask server that can be run on the Raspberry Pi, to interface with Lego Mindstorms.


## Setup

Run the command:

```
make install
```

To install the server and all dependencies.

## Run the server

Run the command:

```
make run
```


## Uninstall

You can remove the installation using the command:

```
make clean
```



## Developing via the USB Cable

rsync -avz -e ssh legoflask/ robot@ev3dev.local:/home/robot/webrover1/


## Creating the Self-signed Certificate

openssl req  -nodes -new -x509 -subj "/C=UK/ST=Devon/L=Exeter/O=WebRover1/CN=10.0.0.1" -keyout server.key -out server.cert
