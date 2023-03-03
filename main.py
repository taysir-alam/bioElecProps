# Input parameters
desired_voltage = 10 
electrode_area = 0.01
skin_impedance = 500 
current_density = 1 

current = current_density * electrode_area

voltage = current * skin_impedance

amperage = voltage / skin_impedance

print("For the 'saddle bag' zone:")
print(" - Voltage range: {} to {} volts".format(voltage-1, voltage+1))
print(" - Amperage required: {} amps".format(amperage))
