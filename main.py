import os
from machine import Pin, SPI
import sdcard

# Initialize the shared hardware SPI bus on ESP32-C3 Super Mini
# Pins: SCK=4, MISO=5, MOSI=6
spi = SPI(0, baudrate=1000000, polarity=0, phase=0, sck=Pin(4), miso=Pin(5), mosi=Pin(6))

# Define independent Chip Select (CS) pins
cs1 = Pin(7, Pin.OUT, value=1)
cs2 = Pin(10, Pin.OUT, value=1)

print("Initializing SD Card modules...")

# --- Initialize and Mount Card 1 ---
try:
    sd1 = sdcard.SDCard(spi, cs1)
    os.mount(sd1, "/sd1")
    print("SD Card 1 mounted successfully at /sd1")
    
    # Write a test file to Card 1
    with open("/sd1/card1_test.txt", "w") as f:
        f.write("Hello from SD Card 1 in MicroPython!\n")
    print("Successfully wrote to Card 1.")
except Exception as e:
    print("Failed to initialize Card 1:", e)

# --- Initialize and Mount Card 2 ---
try:
    sd2 = sdcard.SDCard(spi, cs2)
    os.mount(sd2, "/sd2")
    print("SD Card 2 mounted successfully at /sd2")
    
    # Write a test file to Card 2
    with open("/sd2/card2_test.txt", "w") as f:
        f.write("Hello from SD Card 2 in MicroPython!\n")
    print("Successfully wrote to Card 2.")
except Exception as e:
    print("Failed to initialize Card 2:", e)

# --- Check root directory to confirm mount paths ---
print("Root directory content:", os.listdir("/"))
