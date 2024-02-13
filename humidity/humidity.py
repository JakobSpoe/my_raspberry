from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(180)
red = (255, 0, 0)


humidity = sense.get_humidity()

temperature = sense.get_temperature()


sense.show_message("Humidity: %s %%rH" % humidity, text_colour=red)
time.sleep(15)
sense.show_message("Temperature: %s C" % temperature, text_colour=red)

