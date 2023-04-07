import logging
from confluent_kafka import Consumer
import settings

logger = logging.getLogger('main')
kafka_logger = logging.getLogger('main')


if __name__ == '__main__':
    c = Consumer({
        'bootstrap.servers': settings.KAFKA_BROKERS,
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    })

    c.subscribe([settings.BASIC_TOPIC])

    while True:
        msg = c.poll()

        if msg is None:
            continue
        if msg.error():
            logger.error("Consumer error: {}".format(msg.error()))
            continue

        logger.info('Received message: {}'.format(msg.value().decode('utf-8')))

    c.close()