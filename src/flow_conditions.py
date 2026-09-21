# Calculate aerodynamic flow conditions for the CFD case
import math

temperature = float(input("Enter the flow temperature (K): "))

temperature_reference = 273.15
viscosity_reference = 1.716e-5
sutherland_constant = 110.4

gamma = float(input("Enter the ratio of specific heats: "))

gas_constant = float(input("Enter the value of the gas constant: "))

chord_length = float(input("Please enter the chord length: "))

mach_number_target = float(input("Enter the target mach number: "))

reynolds_number_target = float(input("Enter the target reynolds number: "))


#######################################
#Calculation only                     #
#######################################

viscosity = viscosity_reference * ((temperature_reference + sutherland_constant)/(temperature + sutherland_constant))*(temperature/temperature_reference)**1.5

print(f"The viscosity is: {viscosity} Pa.s")

speed_of_sound = math.sqrt(gamma*gas_constant*temperature)

print(f"The speed of sound is: {speed_of_sound} m/s")

velocity = (speed_of_sound * mach_number_target)

print(f"The velocity of the fluid is: {velocity} m/s")

density = (reynolds_number_target*viscosity)/(velocity*chord_length)

print(f"The required density is: {density} Kg/m^3")

reynolds_number_calculated = (density * velocity * chord_length)/viscosity

print(f"The calculated reynolds number is : {reynolds_number_calculated}")

mach_number_calculated = velocity / speed_of_sound

print(f"The calculated Mach number is: {mach_number_calculated}")