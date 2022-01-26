#!/usr/bin/env python

from pyModbusTCP.client import ModbusClient
import time
import win_inet_pton
import os


# uRTU Initialization
#SERVER_HOST = "10.0.177.171"
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 502
FUNCTION = 1
START_ADDR = 0
LENGTH = 1

client = ModbusClient()

while True:
    client.host(SERVER_HOST)
    client.port(SERVER_PORT)
    client.unit_id(1)
    client.debug()
    print("Modbus reader: Initializing...")
    # open or reconnect TCP to server
    if not client.is_open():
        if not client.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    # if open() is ok, read register (modbus function 0x03)
    if client.is_open():
        print("Connected!")
        if FUNCTION == 1:
            print("read_coils")
            regs = client.read_coils(START_ADDR, LENGTH)
        elif FUNCTION == 2:
            print("read_discrete_inputs")
            regs = client.read_discrete_inputs(START_ADDR, LENGTH)
        elif FUNCTION == 3:
            print("read_holding_registers")
            regs = client.read_holding_registers(START_ADDR, LENGTH)
        elif FUNCTION == 4:
            print("read_input_registers")
            regs = client.read_input_registers(START_ADDR, LENGTH)
        else:
            regs = "Wrong function :D"
        print(regs)
    exit()
