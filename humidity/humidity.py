from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(180)
red = (255, 0, 0)

# temperature = sense.get_temperature_from_humidity().__round__(2)

while True:
  humidity = sense.get_humidity().__round__(2)
  sense.show_message("Humidity: %s" % humidity, text_colour=red)
  time.sleep(15)
# sense.show_message("Temperature: %s C" % temperature, text_colour=red)

