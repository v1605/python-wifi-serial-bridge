import serial
import configparser
from time import sleep
from flask import Flask, request

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')
baudrate = config.getint('SerialConfig', 'baudrate')
port = int(config.get('SerialConfig', 'port'))
device = config.get('SerialConfig', 'device')

# Initialize Flask Server
app = Flask(__name__)
ser = serial.Serial(port=device,baudrate=baudrate,parity=serial.PARITY_NONE,xonxoff=True,timeout=1,dsrdtr=False)

# Consts
delay_key='delay'
ending_key='ending'

# Handle Serial Writing
def send_to_serial(data):
    delay = 0
    ending = ""
    if delay_key in data and data[delay_key] is not None:
        delay = int(data[delay_key]) / 1000
    if ending_key in data and data[ending_key] is not None:
        ending = data[ending_key]
    if ser.is_open:
        commands = data['commands']
        for command in commands:
            ser.write((command + ending).encode())
            ser.flush()
            sleep(delay)
        print("Sent commands to serial")
    else:
        print("Serial port is not open!")

# Route
@app.route('/', methods=['POST'])
def write():
    data = request.get_json()
    send_to_serial(data)  # Send data to serial
    return "Wrote Commands", 200


# Start the server
if __name__ == '__main__':
    try:
        # Ensure the serial connection is open
        if not ser.is_open:
            ser.open()

        print("Server started, listening for POST requests...")
        app.run(host='0.0.0.0', port=port)
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
