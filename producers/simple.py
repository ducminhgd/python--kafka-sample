import logging
from confluent_kafka import Producer, Message

import settings

logger = logging.getLogger('main')

def producer_callback(err, msg: Message):
    logger.info(err)
    logger.info(f'topic: {msg.topic()}, key: {msg.key()}, offset: {msg.offset()}, value: {msg.value()}')

if __name__ == '__main__':
    p: Producer = Producer({'bootstrap.servers': settings.KAFKA_BROKERS})
    
    p.poll(0)
    p.produce('simple', 'Hello, Kafka! I\'m simple Python Producer'.encode('utf-8'), callback=producer_callback)
    
    p.flush()