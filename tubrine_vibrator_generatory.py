#pip install azure-eventhub

import json
import random
import time
from datetime import datetime
from azure.eventhub import EventHubProducerClient, EventData

# Replace these with your actual Event Hub details
EVENT_HUB_CONNECTION_STR = conn #replace your conn with your own connection 
EVENT_HUB_NAME = varHubname  # replace varHubname with your own event hubnam
# Create producer client
producer = EventHubProducerClient.from_connection_string(
    conn_str=EVENT_HUB_CONNECTION_STR,
    eventhub_name=EVENT_HUB_NAME
)

def generate_event():
    return {
        "ts": datetime.utcnow().isoformat(),
        "id": f"Turbine_{random.randint(1,3)}",
        "rms": round(random.uniform(1.0, 7.0), 2),
        "peak": round(random.uniform(2.0, 10.0), 2),
        "freq": round(random.uniform(49.5, 50.5), 2)
    }

# Simulate streaming 10 messages with 1-second interval
for i in range(10):
    data = generate_event()
    event_data_batch = producer.create_batch()
    event_data_batch.add(EventData(json.dumps(data)))
    producer.send_batch(event_data_batch)
    print(f"Sent event: {data}")
    time.sleep(1)

producer.close()
