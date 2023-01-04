# checkInternet
This Python script checks for internet connectivity.

This script is useful for cron jobs or scripts that are ran on boot in linux via rc.local etc.
Is is particularly useful when run before MQTT connections that are able to reconnect on their own once the network device is up and running on the host.

To use just invoke the class with a declaration such as internet=checkInternet()

