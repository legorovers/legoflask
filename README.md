# WebRover1

A web server controller for Mindstorms EV3 that allows you to remote control,
and program, a Mars Rover-like robot.


## Running

    ssh robot@ev3dev.local
    sudo service webrover1 stop; workon webrover1; cd webrover1
    python app/app.py

Setup a mobile phone to connect to:

    https://legorover.space/camera/

Connect tablet to:

    https://legorover.space/

Or local PC (you'll need to ignore the certificate errors or add an /etc/hosts entry):

    https://ev3dev.local/


## Developing via the USB Cable

sshpass -pmaker rsync -avz -e ssh legoflask/ robot@ev3dev.local:/home/robot/webrover1/


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

Add delay back to camera images
Add different CSS wash depending on Mars/Moon/Aus/etc.
Audio sensing via phone
CSS Styling of rule builder!
Action feedback on display


# The Lego Model

Educator Vehicle
http://robotsquare.com/wp-content/uploads/2013/10/45544_educator.pdf

Riley Rover
http://www.damienkee.com/storage/rileyrover/RileyRover_BI.pdf

The ‘RetailRover’…
http://www.damienkee.com/storage/rileyrover/RetailRover.pdf

## Connections

B - Large Motor (Left)
C - Medium Motor (Camera)
D - Large Motor (Right)

n - Touch Sensor (Collision)
n - Colour Sensor (Reflected Light)
n - Gyro Sensor (optional)

