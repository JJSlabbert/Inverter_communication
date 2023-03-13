"""Constants for GrowattClient library."""

# Defaults
DEFAULT_PORT = "/dev/ttyUSB0"
DEFAULT_ADDRESS = 0x1


##PHOTOVOLTAICS_1 = "photovoltaics_1"
##PHOTOVOLTAICS_1_VOLTAGE = "photovoltaics_1_voltage"
##PHOTOVOLTAICS_1_TODAY = "photovoltaics_1_today"
##PHOTOVOLTAICS_1_LIFETIME = "photovoltaics_1_lifetime"
##PHOTOVOLTAICS_2 = "photovoltaics_2"
##PHOTOVOLTAICS_2_VOLTAGE = "photovoltaics_2_voltage"
##PHOTOVOLTAICS_2_TODAY = "photovoltaics_2_today"
##PHOTOVOLTAICS_2_LIFETIME = "photovoltaics_2_lifetime"
##PHOTOVOLTAICS = "photovoltaics"
##PHOTOVOLTAICS_LIFETIME = "photovoltaics_lifetime"
##STATEMENT_OF_CHARGE = "statement_of_charge"
##BATTERY_VOLTAGE = "battery_voltage"
##BATTERY_CHARGE = "battery_charge"
##BATTERY_CHARGE_TODAY = "battery_charge_today"
##BATTERY_CHARGE_LIFETIME = "battery_charge_lifetime"
##BATTERY_DISCHARGE = "battery_discharge"
##BATTERY_DISCHARGE_TODAY = "battery_discharge_today"
##BATTERY_DISCHARGE_LIFETIME = "battery_discharge_lifetime"
##LOCAL_LOAD = "local_load"
##LOCAL_LOAD_TODAY = "local_load_today"
##LOCAL_LOAD_LIFETIME = "local_load_lifetime"
##EXPORT_TO_GRID = "export_to_grid"
##EXPORT_TO_GRID_TODAY = "export_to_grid_today"
##EXPORT_TO_GRID_LIFETIME = "export_to_grid_lifetime"
##IMPORT_FROM_GRID = "import_from_grid"
##IMPORT_FROM_GRID_TODAY = "import_from_grid_today"
##IMPORT_FROM_GRID_LIFETIME = "import_from_grid_lifetime"
##SYSTEM_PRODUCTION_WITH_BATTERY_TODAY = "system_production_with_battery_today"
##SYSTEM_PRODUCTION_WITH_BATTERY_LIFETIME = ("system_production_with_battery_lifetime")
##GRID_VOLTAGE = "grid_voltage"
##GRID_FREQUENCY = "grid_frequency"
##INVERTER_TEMPERATURE_1 = "inverter_temperature_1"
##INVERTER_TEMPERATURE_2 = "inverter_temperature_2"
##INVERTER_TEMPERATURE_3 = "inverter_temperature_3"
##PHOTOVOLTAICS_TODAY = "photovoltaics_today"
##CONSUMPTION = "consumption"
##CONSUMPTION_TODAY = "consumption_today"
##CONSUMPTION_LIFETIME = "consumption_lifetime"
##SYSTEM_PRODUCTION = "system_production"
##SYSTEM_PRODUCTION_TODAY = "system_production_today"
##SYSTEM_PRODUCTION_LIFETIME = "system_production_lifetime"
##SELF_CONSUMPTION = "self_consumption"
Vpv1='PV1 voltage'
Vpv2='PV2 voltage'
Ppv1H='PV1 charge power (high)'
Ppv1L='PV1 charge power (low)'
Ppv2H='PV2 charge power (high)'
Ppv2L='PV2 charge power (low)'
Buck1Curr='Buck1 current'
Buck2Curr='Buck2 current'
OP_Watt_H='Output active power (high)'
OP_Watt_L='Output active power (low)'
OP_VA_H='Output apparent power (high)'
OP_VA_L='Output apparent power (low)'
ACChr_Watt_H='AC charge watt (high)'
ACChr_Watt_L='AC charge watt (low)'
ACChr_VA_H='AC charge apparent power (high)'
ACChr_VA_L='AC charge apparent power (low)'
Bat_Volt='Battery volt (M3)'
BatterySOC='Battery SOC'
Bus_Volt='Bus Voltage'
Grid_Volt='AC input Volt'
Line_Freq='AC input frequency'
OutputVolt='AC output Volt'
OutputFreq='AC output frequency'
Ouput_DCV='Ouput DC Volt'
InvTemp='Inv Temperature'
DcDc_Temp='DC‐DC Temperature'
LoadPercent='Load Percent'
Bat_s_Volt='Battery‐port volt (DSP)'
Bat_Volt_DSP='Battery‐bus volt (DSP)'
Time_total_H='Work time total (high)'
Time_total_L='Work time total (low)'
Buck1_NTC='Buck1 Temperature'
Buck2_NTC='Buck2 Temperature'
OP_Curr='Output Current'
AC_InWatt_H='AC input watt (high)'
AC_InWatt_L='AC input watt (low)'
AC_InVA_H='AC input apparent power (high)'
AC_InVA_L='AC input apparent power (low)'

# Word type
INT_BYTE = "int_byte"
SINGLE_BYTE = "single_byte"
DOUBLE_BYTE = "double_byte"

# Unit of measurement
ELECTRICAL_POTENTIAL_VOLT = 'V'
ELECTRICAL_CURRENT_AMPERE = 'A'
POWER_KILO_WATT = 'kW'
POWER_WATT='W'
REACTIVE_POWER_VAR = 'var'
APPARENT_POWER='VA'
TIME_HOURS = 'h'
ENERGY_KILO_WATT_HOUR = 'kWh'
REACTIVE_ENERGY_KILO_VAR_HOUR = 'kvarh'
FREQUENCY_HERTZ = 'Hz'
TEMP_CELSIUS = '°C'
PERCENTAGE='%'
TIME='DAYS'


def create_value(name, pos, unit, desc, type=DOUBLE_BYTE, scale=0.1):
    return {
        "name": name,
        "pos": pos,
        "type": type,
        "unit": unit,
        "description": desc,
        "scale": scale,
    }


def create_template(name, unit, desc, template):
    """Creates a nice template value"""
    template = " ".join(template.split())
    value = {
        "name": name,
        "unit": unit,
        "description": desc,
        "template": template,
    }
    return value


ATTRIBUTES = [
    create_value(Vpv1,1,ELECTRICAL_POTENTIAL_VOLT,'PV1 VOLTAGE', SINGLE_BYTE),
    create_value(Vpv2,2,ELECTRICAL_POTENTIAL_VOLT,'PV2 VOLTAGE', SINGLE_BYTE),
    create_value(Ppv1H,3,POWER_WATT,'PV1 charge power (high)', DOUBLE_BYTE),
    create_value(Ppv1L,4,POWER_WATT,'PV1 charge power (low)', DOUBLE_BYTE),    
    create_value(Ppv2H,5,POWER_WATT,'PV2 charge power (high)', DOUBLE_BYTE),
    create_value(Ppv2L,6,POWER_WATT,'PV2 charge power (low)', DOUBLE_BYTE),
    create_value(Buck1Curr,7,ELECTRICAL_CURRENT_AMPERE,'Buck1 current', SINGLE_BYTE, 100000000),
    create_value(Buck2Curr,8,ELECTRICAL_CURRENT_AMPERE,'Buck2 current', SINGLE_BYTE, 100000000),
    create_value(OP_Watt_H,9,POWER_WATT,'Output active power (high)', DOUBLE_BYTE),
    create_value(OP_Watt_L,10,POWER_WATT,'Output active power (low)', DOUBLE_BYTE),
    create_value(OP_VA_H,11,APPARENT_POWER,'Output apparent power (high)', DOUBLE_BYTE),
    create_value(OP_VA_L,12,APPARENT_POWER,'Output apparent power (low)', DOUBLE_BYTE),
    create_value(ACChr_Watt_H,13,POWER_WATT,'AC charge watt (high)', DOUBLE_BYTE),
    create_value(ACChr_Watt_L,14,POWER_WATT,'AC charge watt (low)', DOUBLE_BYTE),    
    create_value(ACChr_VA_H,15,APPARENT_POWER,'AC charge apparent power (high)', DOUBLE_BYTE),
    create_value(ACChr_VA_L,16,APPARENT_POWER,'AC charge apparent power (low)', DOUBLE_BYTE), 
    create_value(Bat_Volt,17,ELECTRICAL_POTENTIAL_VOLT,'Battery volt (M3)', SINGLE_BYTE, 0.01),
    create_value(BatterySOC,18,PERCENTAGE,'Battery SOC', SINGLE_BYTE, 1),
    create_value(Bus_Volt,19,ELECTRICAL_POTENTIAL_VOLT,'Bus Voltage', SINGLE_BYTE),    
    create_value(Grid_Volt,20,ELECTRICAL_POTENTIAL_VOLT,'AC input Volt', SINGLE_BYTE),
    create_value(Line_Freq,21,FREQUENCY_HERTZ,'AC input frequency', SINGLE_BYTE, 0.01),
    create_value(OutputVolt,22,ELECTRICAL_POTENTIAL_VOLT,'AC output Volt', SINGLE_BYTE),
    create_value(OutputFreq,23,FREQUENCY_HERTZ,'AC output frequency', SINGLE_BYTE, 0.01),
    create_value(Ouput_DCV,24,ELECTRICAL_POTENTIAL_VOLT,'Ouput DC Volt', SINGLE_BYTE),
    create_value(InvTemp,25,TEMP_CELSIUS,'Inv Temperature', SINGLE_BYTE),    
    create_value(DcDc_Temp,26,TEMP_CELSIUS,'DC‐DC Temperature', SINGLE_BYTE),
    create_value(LoadPercent,27,PERCENTAGE,'Load Percent', SINGLE_BYTE),    
    create_value(Bat_s_Volt,28,ELECTRICAL_POTENTIAL_VOLT,'Battery‐port volt (DSP)', SINGLE_BYTE, 1000000),
    create_value(Bat_Volt_DSP,29,ELECTRICAL_POTENTIAL_VOLT,'Battery‐bus volt (DSP)', SINGLE_BYTE, 1000000),
    create_value(Time_total_H,30,TIME,'Work time total (high)', SINGLE_BYTE, 0.55),
    create_value(Time_total_L,31,TIME,'Work time total (low)', SINGLE_BYTE, 0.55),
    create_value(Buck1_NTC,32,TEMP_CELSIUS,'Buck1 Temperature', SINGLE_BYTE), 
    create_value(Buck2_NTC,33,TEMP_CELSIUS,'Buck2 Temperature', SINGLE_BYTE),
    create_value(OP_Curr,34,ELECTRICAL_CURRENT_AMPERE,'Output Current', SINGLE_BYTE),
    create_value(AC_InWatt_H,35,POWER_WATT,'AC input watt (high)', DOUBLE_BYTE),
    create_value(AC_InWatt_L,36,POWER_WATT,'AC input watt (low)', DOUBLE_BYTE),
    create_value(AC_InVA_H,37,APPARENT_POWER,'AC input apparent power (high)', DOUBLE_BYTE),
    create_value(AC_InVA_L,38,APPARENT_POWER,'AC input apparent power (low)', DOUBLE_BYTE),    
    
##    create_value(
##        PHOTOVOLTAICS_1,                        #name #pos #type #Unit #Description #Scale
##        5,                                      #pos
##        POWER_KILO_WATT,                        #type
##        "Photovoltaics (PV) 1",                 #Unit
##        DOUBLE_BYTE,                            #Description
##        0.0001,                                 #Scale
##    ),
##    create_value(
##        PHOTOVOLTAICS_1_VOLTAGE,
##        3,
##        ELECTRICAL_POTENTIAL_VOLT,
##        "Photovoltaics (PV) 1 voltage",
##        SINGLE_BYTE,
##    ),
##    create_value(
##        PHOTOVOLTAICS_1_TODAY,
##        59,
##        ENERGY_KILO_WATT_HOUR,
##        "Photovoltaics (PV) 1 today",
##    ),
##    create_value(
##        PHOTOVOLTAICS_1_LIFETIME,
##        61,
##        ENERGY_KILO_WATT_HOUR,
##        "Photovoltaics (PV) 1 total",
##    ),
##    create_value(
##        PHOTOVOLTAICS_2,
##        9,
##        POWER_KILO_WATT,
##        "Photovoltaics (PV) 2",
##        DOUBLE_BYTE,
##        0.0001,
##    ),
##    create_value(
##        PHOTOVOLTAICS_2_VOLTAGE,
##        7,
##        ELECTRICAL_POTENTIAL_VOLT,
##        "Photovoltaics (PV) 2 voltage",
##        SINGLE_BYTE,
##    ),
##    create_value(
##        PHOTOVOLTAICS_2_TODAY,
##        63,
##        ENERGY_KILO_WATT_HOUR,
##        "Photovoltaics (PV) 2 today",
##    ),
##    create_value(
##        PHOTOVOLTAICS_2_LIFETIME,
##        65,
##        ENERGY_KILO_WATT_HOUR,
##        "Photovoltaics (PV) 2 total",
##    ),
##    create_value(
##        PHOTOVOLTAICS,
##        1,
##        POWER_KILO_WATT,
##        "Photovoltaics (PV) generation",
##        DOUBLE_BYTE,
##        0.0001,
##    ),
##    create_value(
##        PHOTOVOLTAICS_LIFETIME,
##        91,
##        ENERGY_KILO_WATT_HOUR,
##        "Photovoltaics (PV) generation total",
##    ),
##    # Battery
##    create_value(
##        STATEMENT_OF_CHARGE,
##        1014,
##        "%",
##        "Statement of charge (SOC), capacity",
##        INT_BYTE,
##        1,
##    ),
##    create_value(
##        BATTERY_VOLTAGE,
##        1013,
##        ELECTRICAL_POTENTIAL_VOLT,
##        "Battery voltage",
##        SINGLE_BYTE,
##    ),
##    create_value(
##        BATTERY_CHARGE,
##        1011,
##        POWER_KILO_WATT,
##        "Battery charging",
##        DOUBLE_BYTE,
##        0.0001,
##    ),
##    create_value(
##        BATTERY_CHARGE_TODAY,
##        1056,
##        ENERGY_KILO_WATT_HOUR,
##        "Battery charged today",
##    ),
##    create_value(
##        BATTERY_CHARGE_LIFETIME,
##        1058,
##        ENERGY_KILO_WATT_HOUR,
##        "Battery charged total",
##    ),
##    create_value(
##        BATTERY_DISCHARGE,
##        1009,
##        POWER_KILO_WATT,
##        "Battery discharging",
##        DOUBLE_BYTE,
##        0.0001,
##    ),
##    create_value(
##        BATTERY_DISCHARGE_TODAY,
##        1052,
##        ENERGY_KILO_WATT_HOUR,
##        "Battery discharged today",
##    ),
##    create_value(
##        BATTERY_DISCHARGE_LIFETIME,
##        1054,
##        ENERGY_KILO_WATT_HOUR,
##        "Battery discharged total",
##    ),
##    # Load consumtion
##    create_value(
##        LOCAL_LOAD,
##        1037,
##        POWER_KILO_WATT,
##        "Inverter local load",
##        DOUBLE_BYTE,
##        0.0001,
##    ),
##    create_value(
##        LOCAL_LOAD_TODAY,
##        1060,
##        ENERGY_KILO_WATT_HOUR,
##        "Inverter local load today",
##    ),
##    create_value(
##        LOCAL_LOAD_LIFETIME,
##        1062,
##        ENERGY_KILO_WATT_HOUR,
##        "Inverter local load total",
##    ),
##    # Export to grid
##    create_value(
##        EXPORT_TO_GRID,
##        1029,
##        POWER_KILO_WATT,
##        "Export to grid",
##        DOUBLE_BYTE,
##        0.0001,
##    ),
##    create_value(
##        EXPORT_TO_GRID_TODAY,
##        1048,
##        ENERGY_KILO_WATT_HOUR,
##        "Export to grid today",
##    ),
##    create_value(
##        EXPORT_TO_GRID_LIFETIME,
##        1050,
##        ENERGY_KILO_WATT_HOUR,
##        "Export to grid total",
##    ),
##    # Import from grid
##    create_value(
##        IMPORT_FROM_GRID,
##        1021,
##        POWER_KILO_WATT,
##        "Import from grid",
##        DOUBLE_BYTE,
##        0.0001,
##    ),
##    create_value(
##        IMPORT_FROM_GRID_TODAY,
##        1044,
##        ENERGY_KILO_WATT_HOUR,
##        "Import from grid today",
##    ),
##    create_value(
##        IMPORT_FROM_GRID_LIFETIME,
##        1046,
##        ENERGY_KILO_WATT_HOUR,
##        "Import from grid total",
##    ),
##    create_value(
##        SYSTEM_PRODUCTION_WITH_BATTERY_TODAY,
##        1137,
##        ENERGY_KILO_WATT_HOUR,
##        "System production today (including battery)",
##    ),
##    create_value(
##        SYSTEM_PRODUCTION_WITH_BATTERY_LIFETIME,
##        1139,
##        ENERGY_KILO_WATT_HOUR,
##        "System production total (including battery)",
##    ),
##    create_value(
##        GRID_VOLTAGE,                                   #name 
##        20,                                             #pos was 38
##        ELECTRICAL_POTENTIAL_VOLT,                      #type 
##        "Grid voltage",                                 #Unit 
##        SINGLE_BYTE,                                    #Description
##                                                         #Scale
##    ),
####    create_value(
####        GRID_VOLTAGE,                                   #name 
####        38,                                             #pos 
####        SINGLE_BYTE,                                    #type 
####        ELECTRICAL_POTENTIAL_VOLT,                      #Unit 
####        "Grid voltage",                                 #Description
####                                                        #Scale
####    ),    
##    create_value(
##        GRID_FREQUENCY,
##        21,                         #POS 37 IS WATTS, amps, aPERENT POWER, POWER
##        FREQUENCY_HERTZ,
##        "Grid frequency",
##        SINGLE_BYTE,
##        0.01,               #0.01
##    ),
##    create_value(
##        INVERTER_TEMPERATURE_1,
##        93,
##        TEMP_CELSIUS,
##        "Inverter temperature",
##        SINGLE_BYTE,
##    ),
##    create_value(
##        INVERTER_TEMPERATURE_2,
##        94,
##        TEMP_CELSIUS,
##        "The inside IPM in inverter Temperature",
##        SINGLE_BYTE,
##    ),
##    create_value(
##        INVERTER_TEMPERATURE_3,
##        1040,
##        TEMP_CELSIUS,
##        "Battery temperature",
##        SINGLE_BYTE,
##    ),
##    create_template(
##        PHOTOVOLTAICS_TODAY,
##        ENERGY_KILO_WATT_HOUR,
##        "Photovoltaics (PV) generation today",
##        "{photovoltaics_2_today} + {photovoltaics_1_today}",
##    ),
##    create_template(
##        CONSUMPTION,
##        POWER_KILO_WATT,
##        "Consumption",
##        "{photovoltaics} + {battery_discharge} + {import_from_grid} - \
##            {export_to_grid} - {battery_charge}",
##    ),
##    create_template(
##        CONSUMPTION_TODAY,
##        ENERGY_KILO_WATT_HOUR,
##        "Consumption today",
##        "{photovoltaics_today} + {battery_discharge_today} + \
##            {import_from_grid_today} - {export_to_grid_today} - \
##            {battery_charge_today}",
##    ),
##    create_template(
##        CONSUMPTION_LIFETIME,
##        ENERGY_KILO_WATT_HOUR,
##        "Consumption total",
##        "{photovoltaics_lifetime} + {battery_discharge_lifetime} + \
##            {import_from_grid_lifetime} - {export_to_grid_lifetime} - \
##            {battery_charge_lifetime}",
##    ),
##    create_template(
##        SYSTEM_PRODUCTION,
##        POWER_KILO_WATT,
##        "System Production",
##        "{photovoltaics} + {battery_discharge} - {battery_charge}",
##    ),
##    create_template(
##        SYSTEM_PRODUCTION_TODAY,
##        ENERGY_KILO_WATT_HOUR,
##        "System Production today",
##        "{photovoltaics_today} + {battery_discharge_today} - \
##            {battery_charge_today}",
##    ),
##    create_template(
##        SYSTEM_PRODUCTION_LIFETIME,
##        ENERGY_KILO_WATT_HOUR,
##        "System Production total",
##        "{photovoltaics_lifetime} + {battery_discharge_lifetime} - \
##            {battery_charge_lifetime}",
##    ),
##    create_template(
##        SELF_CONSUMPTION,
##        POWER_KILO_WATT,
##        "Self Consumption",
##        "{consumption} if {export_to_grid} > 0 else {system_production}",
##    ),
]
