# python-wifi-serial-bridge
A python based web server to write serial commands to a connected device (such as the Retrotink 4k).

##Required Libaries
* pySerial
* flask


## Usage

The web server responds to a post request. The body of the request is a json object with the following parameters:
1. commands: A array of string values to print out to the serial interface.
2. delay: (Optional) The amount of time in milliseconds to wait in between serial commands. Default value is 0.
3. ending: (Optional) A string to append after every command (convience to avoid terminating every command). Default value is blank.

## Examples

This request will print out "HelloWorld" with no new lines.
```json
{
  "comands": ["Hello", "World"]
}
```

This request will print out "Hello\nWorld\n", waiting two seconds after each line.
```json
{
  "comands": ["Hello", "World"],
  "delay": 2000,
  "ending": "\n"
}
```

##Configurtation 
The following values are updateable via the config.ini
* baudrate: The baudrate the serial device is exepcting
* device: The serial device to write to. On Linux, this will be something like "/dev/ttyUSB0". On Windows, it will be something like "COM8".
* port: The web port the server is running on

