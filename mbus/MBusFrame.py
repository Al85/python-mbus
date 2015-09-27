from ctypes import Structure,c_uint8,c_uint32,c_void_p

class MBusFrame(Structure):
    _fields_ = [("start1",   c_uint8 * 16),  # MBusFrameFixed
                ("length1",  c_uint8),
                ("length2",  c_uint8),
                ("start2",   c_uint8),
                ("control",  c_uint8),
                ("address",  c_uint8),
                ("control_infomation",  c_uint8),
                ("checksum", c_uint8),
                ("stop",     c_uint8),
                ("data",     c_uint8 * 252),
                ("data_size", c_uint32),  # check
                ("stop",      c_uint8),
                ("timestamp", c_uint32),  # check
                ("next",      c_void_p)]  # pointer

    def __str__(self):
        return "MBusFrame: XXX"
