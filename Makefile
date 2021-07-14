PYTHON = python3

.PHONY = install

.DEFAULT_GOAL = install

install:
	touch ~/.android_usb_detector
	[ -f ".env" ] && cp .env ~/.android_usb_detector;
	mkdir -p ~/.config/systemd/user
	${PYTHON} -m pip install --user .
	cp src/scrcpy.service ~/.config/systemd/user/
	sed -i "s|{EXEC_START}|${HOME}/.local/bin/android_usb_detector|g" ~/.config/systemd/user/scrcpy.service
	sed -i "s|{ENV}|${HOME}/.android_usb_detector|g" ~/.config/systemd/user/scrcpy.service
	systemctl --user daemon-reload
	systemctl --user start scrcpy.service