import logging
from confluent_kafka import Producer, Message, KafkaError
import settings

logger = logging.getLogger('main')
kafka_logger = logging.getLogger('main')


def producer_callback(err: KafkaError, msg: Message):
    logger.info(err)
    logger.info(f'topic: {msg.topic()}, key: {msg.key()}, offset: {msg.offset()}, value: {msg.value()}')


def error_cb(err: KafkaError):
    logger.error(err)


if __name__ == '__main__':
    p: Producer = Producer(
        {
            'bootstrap.servers': settings.KAFKA_BROKERS,
            'socket.timeout.ms': 10,
            'error_cb': error_cb,
        },
        logger=kafka_logger
    )

    p.poll(0)
    p.produce(settings.BASIC_TOPIC, 'Hello, Kafka! I\'m simple Python Producer'.encode('utf-8'), callback=producer_callback)

    p.flush()
