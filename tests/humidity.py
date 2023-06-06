import Adafruit_DHT

# Set sensor type: DHT11
sensor = Adafruit_DHT.DHT11

# Set GPIO pin number
pin = 17

# Read temperature and humidity from sensor
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Check if data was successfully retrieved
if humidity is not None and temperature is not None:
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')
else:
    print('Failed to retrieve data from sensor.')

