# For WIZnet W5500-EVB-Pico2 with 1.3 OLED Waveshare hat

from usocket import socket, AF_INET, SOCK_DGRAM, getaddrinfo
from machine import Pin, SPI
import network
import framebuf
import time
import struct

# OLED pin config
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

class OLED_1inch3(framebuf.FrameBuffer):
    def __init__(self):
        self.width = 128
        self.height = 64
        self.rotate = 180
        self.cs = Pin(CS, Pin.OUT)
        self.rst = Pin(RST, Pin.OUT)
        self.cs(1)
        self.spi = SPI(1, 20000000, polarity=0, phase=0, sck=Pin(SCK), mosi=Pin(MOSI), miso=None)
        self.dc = Pin(DC, Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width // 8)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_HMSB)
        self.init_display()
        self.white = 0xffff
        self.black = 0x0000

    def write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def init_display(self):
        self.rst(1)
        time.sleep(0.001)
        self.rst(0)
        time.sleep(0.01)
        self.rst(1)
        for cmd in [
            0xAE, 0x00, 0x10, 0xB0, 0xDC, 0x00, 0x81, 0x6F, 0x21,
            0xA1 if self.rotate == 180 else 0xA0, 0xC0, 0xA4, 0xA6,
            0xA8, 0x3F, 0xD3, 0x60, 0xD5, 0x41, 0xD9, 0x22, 0xDB,
            0x35, 0xAD, 0x8A, 0xAF
        ]:
            self.write_cmd(cmd)

    def show(self):
        self.write_cmd(0xB0)
        for page in range(0, 64):
            self.column = 63 - page if self.rotate == 0 else page
            self.write_cmd(0x00 + (self.column & 0x0f))
            self.write_cmd(0x10 + (self.column >> 4))
            for num in range(0, 16):
                self.write_data(self.buffer[page * 16 + num])

# Initialize WIZnet chip
def w5x00_init(OLED, timeout=10):
    spi = SPI(0, 2_000_000, mosi=Pin(19), miso=Pin(16), sck=Pin(18))
    OLED.fill(0)
    OLED.text('Connecting...', 1, 0, OLED.white)
    OLED.show()
    try:
        nic = network.WIZNET5K(spi, Pin(17), Pin(20))  # CS=GP17, RST=GP20
        nic.active(True)

        start_time = time.ticks_ms()
        while time.ticks_diff(time.ticks_ms(), start_time) < timeout * 1000:
            ip = nic.ifconfig()[0]
            if ip and ip != '0.0.0.0':
                break
            time.sleep(0.1)

        ip, mask, gw, dns = nic.ifconfig()
        OLED.fill(0)
        if ip != '0.0.0.0':
            print("Connected! IP config:", ip, mask, gw, dns)
            OLED.text('IP Address:', 1, 0, OLED.white)
            OLED.text(ip, 1, 10, OLED.white)
            OLED.text('Mask:', 1, 20, OLED.white)
            OLED.text(mask, 1, 30, OLED.white)
            OLED.text('Gateway:', 1, 40, OLED.white)
            OLED.text(gw, 1, 50, OLED.white)         
        else:
            OLED.text('No network', 1, 0, OLED.white)
        OLED.show()
        return nic
    except Exception as e:
        print("Init failed:", e)
        OLED.fill(0)
        OLED.text('Network error', 1, 0, OLED.white)
        OLED.text('No DHCP/IP', 1, 10, OLED.white)
        OLED.show()
        return None

# DNS resolve
def dns_request(nic, OLED):
    SERVER = 'www.google.co.uk'

    try:
        OLED.fill(0)
        OLED.text('DNS query...', 1, 0, OLED.white)
        OLED.text(SERVER, 1, 10, OLED.white)       
        OLED.show()

        addr = getaddrinfo(SERVER, 80)[0][-1]
        print(addr[0])
        OLED.text("DNS Resolved", 1, 30, OLED.white)
        OLED.text(addr[0], 1, 40, OLED.white)
        OLED.show()
    except Exception as e:
        print("DNS failed:", e)
        OLED.text('DNS resolution failed', 1, 30, OLED.white)
        OLED.text(str(e), 1, 40, OLED.white)
        OLED.show()

# Main
if __name__ == "__main__":
    OLED = OLED_1inch3()
    OLED.fill(0)
    OLED.text('Initialising...', 1, 0, OLED.white)
    OLED.show()

    nic = w5x00_init(OLED)

    keyA = Pin(14, Pin.IN, Pin.PULL_UP)  # For re-checking network
    keyB = Pin(15, Pin.IN, Pin.PULL_UP)  # For SNTP request

    while True:
        if keyA.value() == 0:
            time.sleep(0.05)
            if keyA.value() == 0:
                dns_request(nic, OLED)

        if keyB.value() == 0:
            time.sleep(0.05)
            if keyB.value() == 0:
                OLED.fill(0)
                OLED.text('Rechecking...', 1, 0, OLED.white)
                OLED.show()
                time.sleep(0.7)
                nic = w5x00_init(OLED)

        time.sleep(0.1)
