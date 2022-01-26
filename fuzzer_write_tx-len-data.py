from boofuzz import *

SERVER_HOST = "10.0.177.160"
SERVER_PORT = 502

def main():
    session = Session(target=Target(connection=TCPSocketConnection(SERVER_HOST, SERVER_PORT)),
                      restart_threshold=1, restart_timeout=1.0)

    s_initialize(name="Write Single Coil")

    # Modbus TCP header
    if s_block_start("header"):
        # 2-byte tx id
        s_bytes(value=bytes([0x00, 0x00]), size=2, max_len=2, name="tx_id", fuzzable=True)
        # 2-byte protocol id (00 00)
        s_bytes(value=bytes([0x00, 0x00]), size=2, max_len=2, name="proto_id", fuzzable=False)
        # 2-byte message length (00 06)
        s_bytes(value=bytes([0x00, 0x00]), size=2, max_len=2, name="len", fuzzable=True)
        # 1 byte unit ID
        s_bytes(value=bytes([0x01]), size=1, max_len=1, name="unit_id", fuzzable=False)
    s_block_end()

    # Modbus TCP data
    if s_block_start("data"):
        # 1 byte function ID
        s_bytes(value=bytes([0x05]), size=1, max_len=1, name="func_id", fuzzable=False)
        # 2-byte starting address
        s_bytes(value=bytes([0x00, 0x00]), size=2, max_len=2, name="ref_num", fuzzable=False)
        # 2-byte number of value
        s_bytes(value=bytes([0x00, 0x00]), size=2, max_len=2, name="value", fuzzable=True)
    s_block_end()

    session.connect(s_get("Write Single Coil"))

    session.fuzz()

if __name__ == "__main__":
    main()
