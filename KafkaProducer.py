import requests
from quixstreams import Application
import time,json


app=Application(broker_address="localhost:9092",loglevel="DEBUG")
h={"name":"shania","age":22}
while True:
    with app.get_producer() as producer:
        producer.produce(topic="test-topic",value=json.dumps(h))
        time.sleep(5)
    