# Android USB Detector

A test script to run [scrcpy](https://github.com/Genymobile/scrcpy) and send a message to a local MQTT broker

It's a test to setup scrcpy and send some commands to a local IoT devices when an android phone is connected to the computer

Some commands might be added when disconnecting the device too (like an unplug setup)

# Install and run

There is a make file to help installing the script as a systemd service

Run to install and start the systemd service (the service will not be enabled on boot)

```bash
make install
```

To enable service on boot you can run:

```bash
systemctl --user enable scrcpy.service
```

# A cat

![a cat](./assets/cat.jpg)