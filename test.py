import boto3, os, sys, logging

def main():

    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=FORMAT)
    logger = logging.getLogger(__name__)

    try:

        sqs = boto3.resource('sqs')
        queue = sqs.get_queue_by_name(QueueName=os.environ['SQS_QUEUE'])

        while True:
            for message in queue.receive_messages():
                logger.info('message received')
                message.delete()

        # TODO: Catch the signal to stop and exit cleanly

    except KeyError:
        logger.error('Please set the environment variable SQS_QUEUE')
        sys.exit(1)

if __name__ == '__main__':
    main()
