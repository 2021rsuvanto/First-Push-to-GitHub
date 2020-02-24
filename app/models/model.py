from app import routes

car_mpg_dict =	{
  "Minivan": 20,
  "Hybrid": 45,
  "Electric": 100,
  "SUV": 20,
  "Pickup": 19,
  "Covertible": 25,
  "Wagon": 24,
  "Two-Seater Car": 23,
  "Family Car": 37,
  "I don't drive": 0
}

trans_dict = {
  "Bus": 111,
  # around 111 g/mi per passenger on a bus
  "Airplane": 162.5
  # around 162.5 g/mi per passenger
}

beef_dict = {
  "None": 8.4,
  # around 8.4 CO2 lbs/serving
  "Breakfast": 6.61,
  "Lunch": 6.61,
  "Dinner": 6.61,
  # around 6.61 CO2 lbs/serving
  "2 Meals": 13.22,
  # around 13.22 CO2 lbs/serving
  "Every meal": 19.83
  # around 19.83 CO2 lbs/serving
}

computer_dict = {
  "Laptop": 180.8,
  # around 180.8 CO2 g/day
  "Desktop computer": 479.5,
  # around 479.5 CO2 g/day
  "Neither": 0
}

lights_dict = {
  "LED": 60.9,
   # around 60.9 CO2 g/day
  "Halogen": 295.8,
  "CFL": 95.7,
  "Incandescent": 417.6
}

excess_power_dict = {
  "no": 596020.4,
  # I do not turn the lights off when leaving a room
  "yes": 0
  # I turn the lights off when leaving a room
}


def car_emissions(car_type, mileage):
  variable1 = car_mpg_dict[car_type]
  variable2 = variable1 / int(mileage)
  variable3 = variable2 * 8897
  return variable3

def trans_emissions(trans_type, times_per_day):
  var1 = trans_dict[trans_type]
  var2 = var1 * int(times_per_day)
  return var2

def beef_emissions(number_meals):
  variabol1 = beef_dict[number_meals]
  return variabol1

def computer_emissions(computer_type):
  varr1 = computer_dict[computer_type]
  return varr1

def light_emissions(bulb_type):
  vari1 = lights_dict[bulb_type]
  return vari1

def excess_power_emissions(power_type):
  varii1 = excess_power_dict[power_type]
  return varii1
