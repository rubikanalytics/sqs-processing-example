import boto3, os, sys

def main():

    queue_name = None

    try:
        queue_name = os.environ['SQS_QUEUE']
    except KeyError:
        print('Please set the environment variable SQS_QUEUE')
        sys.exit(1)

    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName=queue_name)

    while True:
        for message in queue.receive_messages(WaitTimeSeconds=20):
            print('message received')
            message.delete()

if __name__ == '__main__':
    main()
