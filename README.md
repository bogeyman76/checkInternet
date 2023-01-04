# checkInternet
This Python script checks for internet connectivity

This script is useful for cron jobs or scripts that are ran on boot in linux via rc.local etc.
Particularly useful to be ran before MQTT connections that maintain reconnects once the network device is up and running on the host

To use just invoke the class with a declaration such as internet=checkInternet()

