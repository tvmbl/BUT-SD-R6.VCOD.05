import json
import random
import time

from kafka import KafkaProducer


### Changez ces 2 paramètres
KAFKA_SERVER = '12.34.56.78:9092'
TOPIC_DIAMETERS_AND_WEIGHTS = 'un-nom-orginal'


producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

apple_id = 0

while True:
    apple_id += 1
    diameter_cm = 5 * random.random() + 8
    weight_g = 80 * random.random() + 60
    message = {
        'apple_id': apple_id,
        'diameter': diameter_cm,
        'weight': weight_g
    }

    print(f'Sending {message} to {TOPIC_DIAMETERS_AND_WEIGHTS}')
    producer.send(TOPIC_DIAMETERS_AND_WEIGHTS, json.dumps(message).encode())

    delay = random.random()
    time.sleep(delay)
