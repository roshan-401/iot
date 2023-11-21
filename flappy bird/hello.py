import serial
import time

arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1)

while True:
    value = arduino.readline().decode().strip()
    if value:
        print(value)
    else:
        print("nothing")
    time.sleep(0.1)
 


# int x = 10;

# void setup() {
#   Serial.begin(115200);
#   Serial.setTimeout(2000);
# }

# void loop() {
#   Serial.println(x);  // Print x with a newline character
#   delay(100);  // Add a delay to control the rate of communication
# }
