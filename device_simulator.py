import time
import random
import json
from azure.iot.device import IoTHubDeviceClient, Message

# Replace with your actual device connection string from Azure
CONNECTION_STRING = "HostName=IoT-Predictive-Hub.azure-devices.net;DeviceId=simulated-device;SharedAccessKey=TxKkT4cHNwBLZc6iCH58bJzYY9yjObJJJjHulb8K1Hg="

# Initialize the IoT client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

print("IoT Hub device simulator started...")

try:
    while True:
        # Generate random sensor data
        data = {
            "temperature": round(random.uniform(70, 100), 2),
            "vibration": round(random.uniform(0.2, 1.2), 2),
            "pressure": round(random.uniform(30, 80), 2)
        }

        # Create message
        message = Message(json.dumps(data))

        # Send message
        client.send_message(message)
        print(f"Message sent: {data}")
        time.sleep(5)  # Wait for 5 seconds

except KeyboardInterrupt:
    print("Simulation stopped.")

