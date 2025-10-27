from confluent_kafka import Consumer, KafkaException, KafkaError
import sys
import logging

def create_consumer(config):
    consumer = Consumer(config)

    return consumer

def basic_consume_loop(consumer, topics):
    try:
           
        consumer.subscribe(topics)

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                    (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(f"Received message: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

            

def main():
    kafka_config = {
        'bootstrap.servers': 'localhost:9092', 
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    }

    consumer_loop = create_consumer(kafka_config)
    basic_consume_loop(consumer_loop, ['sensor_data'])

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()