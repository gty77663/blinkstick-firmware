#!/usr/bin/python3

from intelhex import IntelHex
import codecs

# Get the current serial number
with open("serial.txt", "r") as f:
    serial_number = int(f.read())
    f.close()

# Increment it
serial_number = str(serial_number + 1)

# Fill empty 
serial_number2string = "0" * (6 - len(serial_number)) + serial_number

# Build serial number string
serial_string = f"BS{serial_number2string}-4.0"

# Encode serial string as Ascii, and not Unicode used in python
serial_string = codecs.encode(serial_string, encoding="ascii")

print(serial_string.decode())


ih = IntelHex()

# This byte is required for oscillator
ih[0] = 0x00;

# Fill in the serial number
for i in range(0, len(serial_string)):
    ih[i+1] = serial_string[i]

# Write the hex file with Intel format    
ih.write_hex_file("eeprom.hex");

# Write the new serial number    
with open("serial.txt", "w") as f:
    f.write(serial_number);
    f.close();