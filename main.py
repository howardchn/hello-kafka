from kafka import KafkaProducer
import time

def run():
    print('waiting for kafka...')
    time.sleep(20)

    producer = KafkaProducer(bootstrap_servers='kafka:9092')

    i = 0
    while True:
        producer.send('foobar', b'%d' % i)
        producer.flush()
        print('sent number', i)

        i += 1

        time.sleep(1)


run()
