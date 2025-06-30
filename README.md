# Network-tester---PICO-W5500
Small battery powered network tester using WIZnet W5500-EVB-Pico2 and 1.3" OLED Display HAT

This is a project to create a cheap pocket sized network tester to find if a port is live and has DHCP scope. This has been very useful for the hospital environment I work in where network ports are unpatched regularly. Yes you can use a laptop to do this and more but this is pocket sized and about £20.

It uses a WIZnet W5500-EVB-Pico2 with a 1.3" OLED Waveshare Display HAT. To power a LIPO battery, a cheap LIPO charging board and a toggle switch are used. The code is in MicroPython and there is a 3D printerable enclosure.

Parts required:
1) WIZnet W5500-EVB-Pico2 with header (eg from PI Hut)
2) 1.3" OLED Display HAT for Raspberry Pi Pico (64×128) (eg from PI Hut)
3) 3.7V 260mAh 601730 Lipo battery
4) TP4056 Lithium Battery Charging Board - Type C

The LIPO is connected to
