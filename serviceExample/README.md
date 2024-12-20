# Example Raspberry Pi Service

Here is an example of how to enable the server script on boot. This example assumes:
1. You are using a raspberry pi.
2. You have a user called "pi".
3. The the script is located in the 'home' directory and dependencies are in the 'home/py_envs/bin/activate'

You can modifiy the service file if any these assumptions are not met

## How To Use

1. Copy the service file to '/etc/systemd/system/main_py.service' (or do 'sudo nano /etc/systemd/system/main_py.service' to copy the contents).
2. Run 'sudo systemctl daemon-reload'to load the service.
3. Run 'sudo systemctl enable main_py.service' to enable it at boot.
4. Run 'sudo systemctl start main_py.service' to start the service.
5. Run 'sudo systemctl status main_py.service' to ensure the service has boot correctly.
