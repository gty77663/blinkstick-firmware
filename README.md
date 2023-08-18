# BlinkStick Firmware

BlinkStick is a DIY open source USB RGB LED Controller. It's small, the 
size of a credit card and supports both popular types of RGB LEDs - generic 12V ones and addressable WS2812. 

You can find more details about it here:

http://www.blinkstick.com

This branch contains the firmware required for the BlinkStick(original one), based around ATtiny45/85 chip.

- [BlinkStick Firmware](#blinkstick-firmware)
  - [BlinkStick types](#blinkstick-types)
  - [Serial number](#serial-number)
  - [BlinkStick communication protocol](#blinkstick-communication-protocol)
  - [EEPROM memory map](#eeprom-memory-map)
  - [How to build the firmware](#how-to-build-the-firmware)
    - [Windows](#windows)
    - [Linux](#linux)
    - [Mac-OS](#mac-os)
    - [Compiling](#compiling)
  - [TODO](#todo)
  - [License](#license)


## BlinkStick types
| Name                   | Description                                                                                                        | Link                                                          |
|------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| BlinkStick             | Small formfactor of a USB stick with one WS2812 LED onboard, comes as a DIY kit.                                   | [here](https://www.blinkstick.com/products/blinkstick)        |
| BlinkStick Pro         | USB stick-sized controller board for generic RGB and WS2812 LED strips.                                            | [here](https://www.blinkstick.com/products/blinkstick-pro)    |
| BlinkStick Square      | Little handy square with 8 WS2812 LEDs and a micro-USB port.                                                       | [here](https://www.blinkstick.com/products/blinkstick-square) |
| BlinkStick Strip(mini) | Eight(4 for the mini version) WS2812LEDs shaped in one line & a micro-USB port.                                    | [here](https://www.blinkstick.com/products/blinkstick-strip)  |
| BlinkStick Nano        | Just like normal BlinkStick, but smaller, comes preassembled and has two WS2812 LEDs instead of one.               | [here](https://www.blinkstick.com/products/blinkstick-nano)   |
| BlinkStick Flex        | Really small formfactor with a micro-USB port that supports up to 32 WS2812 LEDs in a strip.                       | [here](https://www.blinkstick.com/products/blinkstick-flex)   |
| BlinkStick L3          | Combines BlinkStick Pro and LED Adapter to control normal, 12V RGB strips.                                         | [here](https://www.blinkstick.com/products/blinkstick-l3)     |
| BlinkStick Advanced    | Combines both generic RGB and WS2812 controllers in a very small formfactor to act as a universal LED strips tool. | none for now                                                  |

## Serial number
Each BlinkStick has a unique serial number 12-byte long serial number, that consist of "BS" header, that stands for "BlinksStick",
followed by its index number, 6 symbols length. The footer is 4 bytes long, that signify the BlinkStick version it is.  
Ex: BS123456-1.0  
```
BSnnnnnn-1.0
||  |    | |- Software minor version
||  |    |--- Software major version
||  |-------- Denotes sequential number
||----------- Denotes BlinkStick device
```
Possible BlinkStick version are:  
* 1.x - BlinkStick
* 2.x - BlinkStick Pro
* 3.x - BlinkStick Square/Strip/Nano/Flex   
This are differentiate by the device version, aka firmware version.  

| Version | Description       | N. of LEDs |
|---------|-------------------|------------|
| 0x200   | BlinkStick Square | 8          |
| 0x201   | BlinkStick Strip  | 8          |
| 0x202   | BlinkStick Nano   | 2          |
| 0x203   | BlinkStick Flex   | ≤32        |
* 4.x - BlinkStick Advanced

## BlinkStick communication protocol

BlinkStick is controller via HID USB reports, each report has its unique id and is responsible for its specific purpose:  

| Report ID | Description                                                                                                    | Format                      |
|-----------|----------------------------------------------------------------------------------------------------------------|-----------------------------|
| 1         | Set\get RGB strip color or first ARGB LED color on first channel                                               | [R, G, B]                   |
| 2         | Set\read the name of the BlinkStick                                                                            | [Binary Data 0..32]         |
| 3         | Set\read custom data stored in BlinkStick's EEPROM                                                             | [Binary Data 0..32]         |
| 4         | Set\read current mode: 0 - RGB LED Strip, 1 - Inverse RGB LED Strip, 2 - WS2812, 3 - Advanced (WS2812 and RGB) | [MODE]                      |
| 5         | Set\read the value of one single ARGB LED on specified channel with INDEX                                      | [CHANNEL, INDEX, R, G, B]   |
| 6         | Set\read LED  from 0 to x (x≤7), on specified channel                                                          | [Channel, [G, R, B][0..7]]  |
| 7         | Set\read LED colors from 0 to x (x≤15), on specified channel                                                   | [Channel, [G, R, B][0..15]] |
| 8         | Set\read LED colors from 0 to x (x≤31), on specified channel                                                   | [Channel, [G, R, B][0..31]] |
| 9         | Set\read LED colors from 0 to x (x≤63), on specified channel                                                   | [Channel, [G, R, B][0..63]] |

## EEPROM memory map 
BlinkStick uses EEPROM to store some of power sensitive data, such as its Name, Serial, etc. 
  
| Address    | Use        |
|------------|------------|
| 0x00       | *unused*   |
| 0x01-0x0C  | **Serial** |
| 0x0D       | **Mode**   |
| 0x0F-0x1F  | *unused*   |
| 0x20-0x3F  | **Name**   |
| 0x40-0x5F  | **Data**   |
| 0x60-0x1FF | *unused*   |

## How to build the firmware

### Windows   
* You'll need to install and add to system path [AVR-GCC toolchain](https://www.microchip.com/en-us/tools-resources/develop/microchip-studio/gcc-compilers)
* [Python3](https://www.python.org/downloads/)
* And [Make](https://www.gnu.org/software/make/#download) on you system. 

### Linux  
#### AVR-GCC toolchain  
    sudo apt-get update  
    sudo apt-get upgrade all
    sudo apt-get install gcc-avr binutils-avr avr-libc  

#### Python  
    sudo apt install python3 python3-pip
#### Make    
    sudo apt install make


### Mac-OS
#### AVR-GCC toolchain
First, you need to install HomeBrew:  

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Then you can install avr toolchain, by typing two following commands:
First tap the repository:

    brew tap osx-cross/avr`

Then install the latest version of avr-libc (version 4.9.2 at the time of writing):

    brew install avr-libc

#### Python
You can download it from [python official site](https://www.python.org/downloads/macos/).

#### Make 
If you allready installed brew, paste this command in the terminal:

    brew install make

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

## TODO  
* Add BlinkStick devices support to SignalRGB
* Add BlinkStick devices support to OpenRGB
* Optional, maybe add built-in effects and animations, 

## License

Released under CC-BY-NC-SA 3.0 license:

http://creativecommons.org/licenses/by-nc-sa/3.0/

(c) 2013 by Agile Innovative Ltd  
(c) 2023 by gty77663
