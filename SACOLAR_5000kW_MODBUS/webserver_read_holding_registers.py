from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from pymodbus.client import ModbusSerialClient as ModbusClient
import time
import serial


inv_serial_num=''
inv_firmware_version=''
modbus_version=''
holding_reg_string=''
inverter_info_string=''
holding_reg_list=[]

PORT='/dev/ttyUSB0'

def get_string(res, index, length):  
    string = ""
    for pos in range(0, length):
        string += str(
            chr(res.registers[index + pos] >> 8)
            + chr(res.registers[index + pos] & 0x000000FF)
        )
    return string


def connect_to_modbus():
    global inv_serial_num
    global inv_firmware_version
    global modbus_version
    global PORT
    global holding_reg_list
    try:
        client = ModbusClient(method='rtu', port=PORT, baudrate=9600, timeout=1)
        client.connect()
        readh=client.read_holding_registers(0,105,0) #Start, Count, Device adress
        print(readh.registers[5])
    except:
        print('Fail1')
        try:
            time.sleep(1)
            PORT='/dev/ttyUSB1'
            client = ModbusClient(method='rtu', port=PORT, baudrate=9600, timeout=1)
            client.connect()
            readh=client.read_holding_registers(0,105,0) #Start, Count, Device adress
            print(readh.registers[5])
        except:
            print('Fail2')
            try:
                time.sleep(1)
                PORT='/dev/ttyUSB2'
                client = ModbusClient(method='rtu', port=PORT, baudrate=9600, timeout=1)
                client.connect()
                readh=client.read_holding_registers(0,105,0) #Start, Count, Device adress
                print(readh.registers[5])
            except:
                print('Fail3')
                print('Could not read registers')
                print ('Reading the holding registers values. These are also writable')
    holding_reg_list.clear()
    time.sleep(1)
    for i in range(105):
        data=readh.registers[i] #read register id 64
        holding_reg_list.append(data)
    inv_serial_num=get_string(readh, 23, 5)
    inv_firmware_version=get_string(readh, 9, 3)
    modbus_version=get_string(readh, 12, 3)
    print('BACKLIGHT ON OFF: ',holding_reg_list[104])





hostName = "192.168.10.174"
serverPort = 8080

def update_strings():
    global holding_reg_string
    global inverter_info_string
    global holding_reg_list
    global inv_serial_num
    global inv_firmware_version
    global modbus_version
    global PORT
    inverter_info_string='<table><tr><td>INVERTER SERIAL NUMBER</td><td>'+inv_serial_num+'</td></tr>'
    inverter_info_string=inverter_info_string+'<tr><td>INVERTER FIRMWARE VERSION</td><td>'+inv_firmware_version+'</td></tr>'
    inverter_info_string=inverter_info_string+'<tr><td> MODBUS VERSION</td><td>'+modbus_version+'</td></tr>'
    inverter_info_string=inverter_info_string+'<tr><td> INVERTER CONNECTED TO PORT</td><td>'+PORT+'</td></tr></table>'

    # Add reg 00 Inverter, On/Off/Standby state. I thoiught this was supouse to be setting 4 on LCD
    holding_reg_string='<table border=1><th>REG NUM</th><th>DESCRIPTIN</th><th>OPTIONS</th><th>CURRENT VALUE</th>'
    holding_reg_string=holding_reg_string+'<tr><td>00</td><td>The Standby On/Off state and the AC output DisEN/EN state; The low byte is the Standby on/off(1/0), the high byte is the AC output disable/enable (1/0).</td><td>'
    holding_reg_string=holding_reg_string+'0: Standby off, Output enable<br> 1: Standby on, Output enable<br> 4: Standby off, Output disable<br> 5: Standby on, Output disable</td><td>'
    holding_reg_string=holding_reg_string+str(holding_reg_list[0])+'</td></tr>'

    #Add reg 01 Output Config, Setting 1 on LCD of inverter
    holding_reg_string=holding_reg_string+'<tr><td>01</td><td>OUTPUT SOURCE PRIORITY<br>LCD SETTING 1</td><td>0: Solar/Battery/Utility<br> 1: SOL FIRST<br> 2: Utility Firs</td><td>'+str(holding_reg_list[1])+'</td></tr>'

    #Add reg 02 Charge Config Priority, Setting 14 on LCD
    holding_reg_string=holding_reg_string+'<tr><td>02</td><td>CHARGE SOURCE PRIORITY<br>LCD SETTING 14</td><td>0: SOLAR FIRST<br> 1: SOLAR AND UTILITY <br> 2: SOLAR ONLY<br> 3: UTILITY FIRST</td><td>'+str(holding_reg_list[2])+'</td></tr>'

    #Add reg 08 AC INPUT MODE, Setting 03 on LCD
    holding_reg_string=holding_reg_string+'<tr><td>08</td><td>AC INPUT VOLTAGE RANGE<br>LCD SETTING 03</td><td>0: Appliance<br> 1: UPS <br> 2: GENERATOR</td><td>'+str(holding_reg_list[8])+'</td></tr>'

    #Add reg 18 Output Volt Type, Setting 08 on LCD
    holding_reg_string=holding_reg_string+'<tr><td>18</td><td>Output Voltage Type<br>LCD SETTING 08</td><td>0: 208 VAC<br> 1: 230 VAC <br> 2: 240 VAC</td><td>'+str(holding_reg_list[18])+'</td></tr>'

    #Add reg 19 Output Frequency Type, Setting 09 on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>19</td><td>Output Frequency Type<br>LCD SETTING 09</td><td>0: 50 Hz<br> 1: 60 Hz </td><td>'+str(holding_reg_list[19])+'</td></tr>'

    #Add reg 20 Overload Restart, Setting 06 on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>20</td><td>Auto Restart when Overload Occurs<br>LCD SETTING 06</td><td>0: YES<br> 1: NO</td><td>'+str(holding_reg_list[20])+'</td></tr>'

    #Add reg 21 Over Temp Restart, Setting 07 on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>21</td><td>Auto Restart when Over Temperature Occurs<br>LCD SETTING 07</td><td>0: YES<br> 1: NO </td><td>'+str(holding_reg_list[21])+'</td></tr>'

    #Add reg 22 BUZZER ENABLED DISABLED Setting __ on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>22</td><td>BUZZSER STATUS<br>LCD SETTING ?</td><td>0: DISABLED Hz<br> 1: ENABLED </td><td>'+str(holding_reg_list[22])+'</td></tr>'

    #Add reg 34 MASX CHARGE CURRENT Setting 02 on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>34</td><td>MAXIMUM TOTAL (AC+PV) CHARGE CURRENT<br>LCD SETTING 02</td><td>0-20 AMP PER BATTERY</td><td>'+str(holding_reg_list[34])+'</td></tr>'

    #Add reg 34 MASX AC CHARGE CURRENT Setting 11 on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>38</td><td>MAXIMUM AC/GRID CHARGE CURRENT<br>LCD SETTING 11</td><td>0-20 AMP PER BATTERY</td><td>'+str(holding_reg_list[38])+'</td></tr>'
    #Add reg 35 BULK /ABSORPTION/CV CHARGE VOLTAGE Setting 19 on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>35</td><td>ABSORPTION/BULK/CV Charge Voltage<br>LCD SETTING 19</td><td>48.0-58.4 VOLT</td><td>'+str(holding_reg_list[35]*0.1)+'</td></tr>'

    #Add reg 36 FLOATING CHARGE VOLTAGE Setting 20 on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>36</td><td>FLOATING Charge Voltage<br>LCD SETTING 20</td><td>48.0-58.4 VOLT<br>Must be lower or equal to REG 35(Absorption Charge Voltage)'
    holding_reg_string=holding_reg_string+ '</td><td>'+str(holding_reg_list[36]*0.1)+'</td></tr>'    

    #Add reg 37 BATTERY LOW VOLTAGE-SWITCH TO UTILITY Setting 12 on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>37</td><td>BATTERY LOW VOLTAGE-SWITCH TO UTILITY<br> Only Applicable if Output Source Priority is SBU or SOLAR FIRST<br>LCD SETTING 12'      
    holding_reg_string=holding_reg_string+'</td><td>44.0-51.2 </td><td>'+str(holding_reg_list[37]*0.1)+'</td></tr>'

    #Add reg 95 BATTERY HIGH VOLTAGE-SWITCH TO BATTERY Setting 13 on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>95</td><td>BATTERY HIGH VOLTAGE-SWITCH TO BATTERY<br> Only Applicable if Output Source Priority is SBU or SOLAR FIRST<br>LCD SETTING 13'      
    holding_reg_string=holding_reg_string+'</td><td>48.0-58.0 VOLT</td><td>'+str(holding_reg_list[95]*0.1)+'</td></tr>'

    #Add reg 39 BATTERY TYPE Setting 5 on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>39</td><td>BATTERY TYPE<br>LCD SETTING 5</td><td>0: AGM<br> 1: FLOODED <br>2: USER <br>3: LITHIUM(BMS)<br)4:   </td><td>'+str(holding_reg_list[39])+'</td></tr>'
    
    #Add reg 45-47 DATE 
    holding_reg_string=holding_reg_string+'<tr><td>45-47</td><td>INVERTER DATE<br>LCD SETTING N/A</td><td>YYYY/MM/DD</td><td>'+str(holding_reg_list[45])+'/'+str(holding_reg_list[46])+'/'+str(holding_reg_list[47])+'</td></tr>'
    #Add reg 48-50 TIME
    hour=str(holding_reg_list[48])
    minute=str(holding_reg_list[49])
    seconds=str(holding_reg_list[50])
    if holding_reg_list[48]<10:
        hour='0'+hour
    if holding_reg_list[49]<10:
        minute='0'+minute
    if holding_reg_list[50]<10:
        seconds='0'+seconds       
    holding_reg_string=holding_reg_string+'<tr><td>48-50</td><td>INVERTER TIME<br>LCD SETTING N/A</td><td>HH:MM:SS</td><td>'+hour+':'+minute+':'+seconds+'</td></tr>'

    #Add reg 104 LCD BACK LIGHT, Setting 16 on LCD 
    holding_reg_string=holding_reg_string+'<tr><td>104</td><td>LCD BACK LIGHT<br>LCD SETTING 16</td><td>0: OFF<br> 1: ON</td><td>'+str(holding_reg_list[104])+'</td></tr>'
    
    holding_reg_string=holding_reg_string+'</table>'
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print ('In Do GET')
        global inverter_info_string
        global holding_reg_string
        connect_to_modbus()
        update_strings()

        
##        webServer.shutdown()
##        webServer.serve_forever()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>INVERTER MANAGER</title><style>body {font-size: 100%;h1 {font-size: 2.5em;}h2 {font-size: 1.875em;}p {font-size: 0.875em;}</style></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h1>MANAGE THE SACOLAR 5000</h1>", "utf-8"))
        self.wfile.write(bytes("<p>"+inverter_info_string+"</p>","utf-8"))
        self.wfile.write(bytes("<h2>HOLDING REGISTER VALUES.</h2>", "utf-8"))
        self.wfile.write(bytes("<p>"+holding_reg_string+"</p>", "utf-8"))
      
        self.wfile.write(bytes("<h2>INPUT REGISTER VALUES.</h2>", "utf-8"))        
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        print('Try webserver forever')
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

##    webServer.server_close()
##    print("Server stopped.")

