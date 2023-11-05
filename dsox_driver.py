import pyvisa
import time

rm = pyvisa.ResourceManager()
scope = rm.open_resource('USB0::0x2A8D::0x0396::CN60447307::INSTR')

class DSOX:

    print(scope)

    def display_clear():
        scope.write(":DISPlay:CLEar")

    def display_channel(chan):
        scope.write(f":CHANnel{chan}:DISPlay ON")
        scope.write(f":CHANnel{chan}:DISPlay ON")
