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

sshpass -pmaker rsync -avz -e ssh legoflask/ robot@ev3dev.local:/home/robot/webrover1/


## Running

    ssh robot@ev3dev.local
    workon webrover1
    cd webrover1
    python app/app.py

The port 80 redirect script:

    sudo python redirect.py
    <CTRL-Z>
    bg

Setup a mobile phone to connect to:

    https://legorover.space:5443/camera/

Connect tablet to:

    https://10.0.0.1:5443/

Or local PC (you'll need to ignore the certificate errors or add an /etc/hosts entry):

    https://ev3dev.local:5443/


## Creating the Certificate Signing Request

openssl req  -nodeopenssl req -nodes -newkey rsa:2048 -sha256 -keyout legorover.key -out legorover.csr

Country Name (2 letter code) [AU]:UK
State or Province Name (full name) [Some-State]:Devon
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Lego Rovers Devon
Common Name (e.g. server FQDN or YOUR name) []:legorover.space
Email Address []:4ba21db849491781b943df4d1cd45ada-4639958@contact.gandi.net

## Bundle Certificate with the Intermediates

cat GandiStandardSSLCA2.pem >> legorover.crt


# TODO

Make the jpeg snapshots the same size as the display (400x300)
