# BlinkStick Advanced Docs

## USB Specification

#### USB Descriptor

```
USAGE_PAGE (Generic Desktop)
USAGE (Vendor Usage 1)
COLLECTION (Application)
  LOGICAL_MINIMUM (0)
  LOGICAL_MAXIMUM (255)
  REPORT_SIZE (8)
  REPORT_ID (1)
  REPORT_COUNT (3)
  USAGE (Undefined)
  FEATURE (Data,Var,Abs,Buf)
  REPORT_ID (2)
  REPORT_COUNT (32)
  USAGE (Undefined)
  FEATURE (Data,Var,Abs,Buf)
  REPORT_ID (3)
  REPORT_COUNT (32)
  USAGE (Undefined)
  FEATURE (Data,Var,Abs,Buf)
  REPORT_ID (4)
  REPORT_COUNT (1)
  USAGE (Undefined)
  FEATURE (Data,Var,Abs,Buf)
  REPORT_ID (5)
  REPORT_COUNT (5)
  USAGE (Undefined)
  FEATURE (Data,Var,Abs,Buf)
  REPORT_ID (6)
  REPORT_COUNT (25)
  USAGE (Undefined)
  FEATURE (Data,Var,Abs,Buf)
  REPORT_ID (7)
  REPORT_COUNT (49)
  USAGE (Undefined)
  FEATURE (Data,Var,Abs,Buf)
  REPORT_ID (8)
  REPORT_COUNT (97)
  USAGE (Undefined)
  FEATURE (Data,Var,Abs,Buf)
  REPORT_ID (9)
  REPORT_COUNT (193)
  USAGE (Undefined)
  FEATURE (Data,Var,Abs,Buf)
END_COLLECTION
```


#### Reports usage
| Report ID | Write purpose               | Read purpose                   | Syntax                      |
|-----------|-----------------------------|--------------------------------|-----------------------------|
| 1         | Set RGB LED Color           | Read RGB LED Color             | [R, G, B]                   |
| 2         | Set Device Name             | Read Device Name               | [Binary Data 0..32]         |
| 3         | Set Device Data             | Read Device Data               | [Binary Data 0..32]         |
| 4         | Set Mode                    | Read Mode                      | [MODE]                      |
| 5         | -                           | Read Color from Specified ALED | [CHANNEL, INDEX, R, G, B]   |
| 6         | Set Led Frame(ARGB) [0..7]  | -                              | [Channel, [G, R, B][0..7]]  |
| 7         | Set Led Frame(ARGB) [0..15] | -                              | [Channel, [G, R, B][0..15]] |
| 8         | Set Led Frame(ARGB) [0..31] | -                              | [Channel, [G, R, B][0..31]] |
| 9         | Set Led Frame(ARGB) [0..63] | -                              | [Channel, [G, R, B][0..63]] |



## Modes
| Mode        | Mode ID  | Description                                            |
|-------------|----------|--------------------------------------------------------|
| RGB         | 0        | RGB LEDs only, colors are inversed(0 - max, 255 - min) |
| RGB_INVERSE | 1        | RGB LEDs only, normal colors(0 - min, 255 - max)       |
| WS2812      | 2        | Only ARGB LEDs are active                              |
| ADVANCED    | 3        | Both ARGB and ARG LEDs are active                      |



## EEPROM Memory Map
| Address | Description                         |
|---------|-------------------------------------|
| 00      | <unused>                            |
| 01 - 0C | Serial number of BlinkStick         |
| 0D      | Current Mode                        |
| 0F - 1F | <unused>                            |
| 20-3F   | Assignable Name of BlinkStick       |
| 40 - 5F | Assignable Data Field of BlinkStick |
| 60 -    | <unused>                            |