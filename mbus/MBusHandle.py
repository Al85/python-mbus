from ctypes import *

libmbus = None
try:
    libmbus = cdll.LoadLibrary('libmbus.so')
except OSError:
    libmbus = cdll.LoadLibrary('/usr/local/lib/libmbus.so')

if None == libmbus:
    raise OSError("libmbus not found")


class MBusHandle(Structure):
    _fields_ = [("fd",        c_uint32),
                ("is_serial", c_uint8),
                ("internal",  c_uint32 * 6)]  # pointers

    def __str__(self):
        return "MBusHandle: XXX"
