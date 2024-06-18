from __future__ import print_function

import os
import sys

import serial

DEVNULL = open(os.devnull, 'w')


def list_serial_ports():
    # from https://github.com/pyserial/pyserial/blob/master/serial/tools/list_ports.py
    from serial.tools.list_ports import comports
    result = []
    for port, desc, info in comports():
        if not port or "VID:PID" not in info:
            continue
        split_desc = desc.split(' - ')
        if len(split_desc) == 2 and split_desc[0] == split_desc[1]:
            desc = split_desc[0]
        result.append((port, desc))
    result.sort()
    # return[('COM1', 'USB Serial Port 1'),('COM2', 'USB Serial Port 2')]    # for testing EMS-ESP
    return result


def prevent_print(func, *args, **kwargs):
    orig_sys_stdout = sys.stdout
    sys.stdout = DEVNULL
    try:
        return func(*args, **kwargs)
    except serial.SerialException as err:
        from esp_flasher.common import EspflasherError

        raise EspflasherError("Serial Port closed: {}".format(err))
    finally:
        sys.stdout = orig_sys_stdout
        sys.stdout.isatty = lambda: False
        pass
