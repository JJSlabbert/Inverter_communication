import asyncio
import logging
from sys import argv

from growatt_client import GrowattClient

# defaults
# USB port of RS232/RS485 converter
DEFAULT_PORT = "/dev/ttyUSB1"
# Growatt modbus address
DEFAULT_ADDRESS = 0x01

logging.basicConfig(level=logging.INFO)


async def run_async_client():
    port = str(argv[1]) if len(argv) > 1 else DEFAULT_PORT
    address = int(argv[2]) if len(argv) > 2 else DEFAULT_ADDRESS
    client = GrowattClient(
        port,
        address,
##        attributes=["battery_charge","battery_charge_lifetime", "grid_voltage", "grid_frequency"],
        attributes=['PV1 voltage','PV2 voltage', 'PV1 charge power (high)', 'PV1 charge power (low)',
                    'PV2 charge power (high)', 'PV2 charge power (low)', 'Solar Charger1 PV1 voltage',
                    'Buck1 current', 'Buck2 current', 'Output active power (high)', 'Output active power (low)',
                    'Output apparent power (high)','Output apparent power (low)',
                    'AC charge watt (high)','AC charge watt (low)',
                    'AC charge apparent power (high)', 'AC charge apparent power (low)',
                    'Battery volt (M3)', 'Battery SOC', 'Bus Voltage', 'AC input Volt',
                    'AC input frequency', 'AC output Volt', 'AC output frequency',
                    'Ouput DC Volt', 'Inv Temperature', 'DC‐DC Temperature', 'Load Percent',
                    'Battery‐port volt (DSP)', 'Battery‐bus volt (DSP)', 'Work time total (high)',
                    'Work time total (low)', 'Buck1 Temperature', 'Buck2 Temperature', 'Output Current',
                    'AC input watt (high)', 'AC input watt (low)', 'AC input apparent power (high)',
                    'AC input apparent power (low)'
                    ],
    )
    # client = GrowattClient(port, address)

    data = await client.async_update()
    ser = client.get_serial_number()

    logging.info(
        f" Serial number: {ser} "
        f"Firmware: {client.get_firmware()} "
        f"Model Number: {client.get_model_number()}"
    )

    logging.debug(f"Sensors data: {data}")
    for key in sorted(data):
        desc = client.get_attribute(key)
        value = data[key]
        d = desc["description"]
        u = desc["unit"]
        calculated = "(calculated)" if "template" in desc else ""
        logging.info(f"{d} {value} {u} {calculated}")

    # except Exception as error:
    #     logging.error("Error: " + repr(error))


if __name__ == "__main__":
    asyncio.run(run_async_client())
