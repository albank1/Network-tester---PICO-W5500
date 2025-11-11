# Network-tester---PICO-W5500

![IMG_20250820_205447](https://github.com/user-attachments/assets/1194126f-6e9e-4c92-bfbc-a89046003d3c)

Small battery powered network tester using WIZnet W5500-EVB-Pico and 1.3" OLED Display HAT

This is a project to create a cheap pocket sized network tester to find if a port is live and has DHCP scope. This is an improvement of my previous arduino Network Tester. This has been very useful for the hospital environment I work in where network ports are unpatched regularly. Yes you can use a laptop to do this and more but this is pocket sized and about £20.

It uses a WIZnet W5500-EVB-Pico with a 1.3" OLED Waveshare Display HAT. To power a LIPO battery, a cheap LIPO charging board and a toggle switch are used. The code is in MicroPython and there is a 3D printerable enclosure.

Parts required:
1) WIZnet W5500-EVB-Pico with header (eg from PI Hut)
2) 1.3" OLED Display HAT for Raspberry Pi Pico (64×128) (eg 1.3 oLED Waveshare from PI Hut)
3) 3.7V 260mAh 601730 or 300mAh Lipo battery
4) TP4056 Lithium Battery Charging Board - Type C
5) A switch to turn off/on (Rocker Switch Control Micro 14mm Diameter)
The LIPO is connected to the TP4056 and the output connected via the switch to the VSYS and the ground connected directly.

I have had to cut the pin on the 1.3 OLED HAT as one of the buttons connects to pin 17 on the PICO but this is also used for the W5500. This was instead soldered to pin 15.

![IMG_20250820_205455](https://github.com/user-attachments/assets/23f2a5e2-0bf1-45fb-a832-12b36cd81b06)![IMG_20250820_205419](https://github.com/user-attachments/assets/6fd15c67-4166-4950-b9cc-fa57a211fece)
![IMG_20251003_184639](https://github.com/user-attachments/assets/e12dd2ba-9773-4276-81cf-56d2358fc9fe)
![IMG_20250915_135053](https://github.com/user-attachments/assets/c1e38354-5f31-4999-aeb5-962214a4c4e0)
![IMG_20250915_135034](https://github.com/user-attachments/assets/d8f6e047-d309-4f4d-aea0-382c8e500115)
![IMG_20250915_135047](https://github.com/user-attachments/assets/4f01784c-9471-4eff-b037-cb7e608b0541)


