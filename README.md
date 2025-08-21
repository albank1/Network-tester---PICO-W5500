# Network-tester---PICO-W5500

![IMG_20250820_205455](https://github.com/user-attachments/assets/07d66ca6-d657-42e2-989e-28de3c028574)![IMG_20250820_205447](https://github.com/user-attachments/assets/21e52d9d-a7a7-4a3a-8611-e5df872cf1be)![IMG_20250820_205419](https://github.com/user-attachments/assets/d6e54994-6ba5-4bcc-931b-2ba00212dbcd)

Small battery powered network tester using WIZnet W5500-EVB-Pico2 and 1.3" OLED Display HAT

This is a project to create a cheap pocket sized network tester to find if a port is live and has DHCP scope. This is an improvement of my previous arduino Network Tester. This has been very useful for the hospital environment I work in where network ports are unpatched regularly. Yes you can use a laptop to do this and more but this is pocket sized and about £20.

It uses a WIZnet W5500-EVB-Pico2 with a 1.3" OLED Waveshare Display HAT. To power a LIPO battery, a cheap LIPO charging board and a toggle switch are used. The code is in MicroPython and there is a 3D printerable enclosure.

Parts required:
1) WIZnet W5500-EVB-Pico2 with header (eg from PI Hut)
2) 1.3" OLED Display HAT for Raspberry Pi Pico (64×128) (eg from PI Hut)
3) 3.7V 260mAh 601730 Lipo battery
4) TP4056 Lithium Battery Charging Board - Type C
5) A switch to turn off/on

The LIPO is connected to the TP4056 and the output connected via the switch to the VSYS and the ground connected directly.

I have had to cut the pin on the 1.3 OLED HAT as one of the buttons connects to pin 17 on the PICO but this is also used for the W5500. This was instead soldered to pin 15.
