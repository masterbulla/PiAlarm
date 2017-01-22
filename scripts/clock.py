import sys
from time import sleep
# try:
#     import thread
# except ImportError:
#     import _thread as thread

from modules import tm1637
from modules import config as cg

# Initialize the clock (GND, VCC=3.3V, Example Pins are DIO-20 and CLK21)
clock = cg.get_pin('7Segment', 'clk')
digital = cg.get_pin('7Segment', 'dio')
Display = tm1637.TM1637(CLK=clock, DIO=digital, brightness=1.0)

# if __name__ == "__main__":
if len(sys.argv) <= 1:
    cg.send("Starting 7-segment clock in the background")
    Display.StartClock(military_time=True)
else:
    Display.StartClock(military_time=False)
    print 'Continue Python script and tweak Display!'
    sleep(1)
    Display.ShowDoublepoint(False)
    sleep(1)
    for i in range(0, 5):
        Display.SetBrightness(i / 5.0)
        sleep(0.25)
    Display.StopClock()

# try:
#     print "Starting clock in the background (press CTRL + C to stop):"
#     Display.StartClock(military_time=False)
#     print 'Continue Python script and tweak Display!'
#     sleep(5)
#     Display.ShowDoublepoint(False)
#     sleep(5)
#     loops = 3
#     while loops > 0:
#         for i in range(0, 10):
#             Display.SetBrightness(i / 10.0)
#             sleep(0.5)
#         loops -= 1
#     Display.StopClock()
#     thread.interrupt_main()
# except KeyboardInterrupt:
#     print "Properly closing the clock and open GPIO pins"
#     Display.cleanup()
