import random
import time
from kafka import KafkaProducer
from datetime import datetime
import json



producer = KafkaProducer(
    bootstrap_servers='localhost:29092', 
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  
)


def generate_random_number():
    numbers = [i for i in range(16) if i not in [9, 10]]
   
    return random.choice(numbers + random.choices([9, 10], k=1))


def send_to_kafka():
    try:
        while True:
            number = generate_random_number()
            data = {
                'number': number,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            producer.send('random_numbers', value=data)
            print(f"Gönderilen veri: {data}")
            time.sleep(1)  
    except KeyboardInterrupt:
        print("Görev durduruldu.")
    finally:
        producer.close()

if __name__ == '__main__':

    send_to_kafka()
