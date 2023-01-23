## BlinkStick Advanced Firmware

BlinkStick is a DIY open source USB RGB LED Controller. It's small, the 
size of a credit card and supports both popular types of RGB LEDs. 

You can find more details about it here:

http://www.blinkstick.com

This branch contains the firmware required for the Atmega8 chip.

## How to build the firmware

### Windows:
* You'll need to install and add to system path [AVR-GCC toolchain](https://www.microchip.com/en-us/tools-resources/develop/microchip-studio/gcc-compilers)
* [Python3](https://www.python.org/downloads/)
* And [Make](https://www.gnu.org/software/make/#download) on you system. 

### Linux:
##### AVR-GCC toolchain: 
`sudo apt-get update`
`sudo apt-get upgrade all`
`sudo apt-get install gcc-avr binutils-avr avr-libc`
##### Python:
`sudo apt install python3 python3-pip`
##### Make:
`sudo apt install make`


### Mac-OS
##### AVR-GCC toolchain
First, you need to install HomeBrew:
`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

Then you can install avr toolchain, by typing two following commands:
First tap the repository:
`brew tap osx-cross/avr`

Then install the latest version of avr-libc (version 4.9.2 at the time of writing):
`brew install avr-libc`

##### Python
You can download it from [python official site](https://www.python.org/downloads/macos/).

##### Make 
If you allready installed brew, paste this command in the terminal:
`brew install make`

### Compiling
After installing all nessecery software, you can run make in project folder and choose one of the options that you need:
```
"This Makefile has no default rule. Use one of the following:"
"make hex ....... to build main.hex"
"make program ... to flash fuses and firmware"
"make fuse ...... to flash the fuses"
"make flash ..... to flash the firmware (use this on metaboard)"
"make dump ...... dump eeprom"
"make dumpflash . dump flash"
"make defaults .. write default eeprom"
"make clean ..... to delete objects and hex file"
"make deploy .... program, increment serial, defaults"
```
## License

Released under CC-BY-NC-SA 3.0 license:

http://creativecommons.org/licenses/by-nc-sa/3.0/

(c) 2013 by Agile Innovative Ltd
(c) 2022 by Foxdogface