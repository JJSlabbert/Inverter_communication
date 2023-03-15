from pymodbus.client import ModbusSerialClient as ModbusClient
import time

def get_string(res, index, length):  
    string = ""
    for pos in range(0, length):
        string += str(
            chr(res.registers[index + pos] >> 8)
            + chr(res.registers[index + pos] & 0x000000FF)
        )
    return string

client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, timeout=1)

client.connect()
readh=client.read_holding_registers(0,100,1) #Start, End, Device adress

print ('Reading the holding registers values. These are also writable')
for i in range(100):
    data=readh.registers[int(i)] #read register id 64
    print(i, data) #print register data

print('Inverter Serial Number: ',get_string(readh, 23, 5))
print('Inverter Firmware Version: ',get_string(readh, 9, 3))
print('Modbus Version: ',get_string(readh, 12, 3))

#How to write to holding registers. 
#print ('Set absorption charge voltage to 50.8')
#client.write_register(35,508,1)

print ('Reading input registers. You can not write to them')

readi=client.read_input_registers(0,127,1) #Start, End, Device adressprint
for i in range(127):
    data=readi.registers[int(i)] #read register id 64
    print(i, data) #print register data
time.sleep(10)



