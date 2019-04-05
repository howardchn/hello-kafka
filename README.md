# Kafka Quick Test Env
This is used for setting up a Kafka environment with a simple producer and continuously sending a number per second. You could just build your own client to consume the predefined topics `foobar`.

## Quick Setup
For quick start, only the following commands will be ready to go.

Note: before running the following commands, make sure the following items are installed.

### Prerequisite
1. [docker](https://docs.docker.com/get-started/) CE or EE
2. [docker composer](https://docs.docker.com/compose/install/)
3. ports `2181`, `9092` and `29092` are not in using

### Launch The Service
```terminal
cd [your work directory]
curl https://raw.githubusercontent.com/howardchn/hello-kafka/master/docker-compose.yaml -o docker-compose-kafka.yaml
docker-compose -f docker-compose-kafka.yaml up
```

Then wait about `15` seconds, the `zookeeper`, `kafka` and `default simple producer` are ready.

## Build Your Own Producer
The integrated producer has hard-coded topic name `foolbar` nad the key is `Null` (not defined), the content is an `incremented number` and the sending interval is `1 second`. Seems lots of restriction inside. The following steps will help to customize your own producer and docker images.

1. modify `main.py` which is the implementation of the producer
1. build docker image with `docker build -t [your producer image name] .`
1. replace the producer image `howardch/hello-kafka-producer` with `[your producer image name]` in `docker-compose.yaml` file
1. everything is set, execute command `docker-compose up -d` to run your own environment



