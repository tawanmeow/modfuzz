# Tawannnnnnnn :)
# ref tawanmeow/ida-modbus-reader

from pyModbusTCP.client import ModbusClient
import time
import win_inet_pton
import os

SERVER_HOST = "10.0.177.160"
SERVER_PORT = 502
FUNCTION = 5
START_ADDR = 0
LENGTH = 1
# Coils = boolean | Register value = int
VALUE = True
# Multiple coils | Register = list
LIST = []


client = ModbusClient()

while True:
    client.host(SERVER_HOST)
    client.port(SERVER_PORT)
    #client.unit_id(1)
    client.debug()
    print("Modbus writer: Initializing...")
    # open or reconnect TCP to server
    if not client.is_open():
        if not client.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    # if open() is ok, read register (modbus function 0x03)
    if client.is_open():
        print("Connected!")
        if FUNCTION == 5:
            print("write_single_coil")
            regs = client.write_single_coil(START_ADDR, VALUE)
            if VALUE == True:
                VALUE = False
            else:
                VALUE = True
        elif FUNCTION == 15:
            print("write_multiple_coils")
            regs = client.write_multiple_coils(START_ADDR, LIST)
        elif FUNCTION == 6:
            print("write_single_register")
            regs = client.write_single_register(START_ADDR, VALUE)
        elif FUNCTION == 16:
            print("write_multiple_registers")
            regs = client.write_multiple_registers(START_ADDR, LIST)
        else:
            regs = "Wrong function :D"
        print(regs)
