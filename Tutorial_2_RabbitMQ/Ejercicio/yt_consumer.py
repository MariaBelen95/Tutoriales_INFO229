#!/usr/bin/env python
import pika
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

##ID Cliente = 238246015667-dqc0v6mpoc4m0hnvcg9o54p8d9090c91.apps.googleusercontent.com

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='yt_queue')

def youtube(n):

    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_238246015667-dqc0v6mpoc4m0hnvcg9o54p8d9090c91.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part = "snippet",
        maxResults = 25,
        q = n
    )
    response = request.execute()
    return response

def on_request(ch, method, props, body):
    n = body

    print(" [.] youtube(%s)" % n)
    response = youtube(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='yt_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
