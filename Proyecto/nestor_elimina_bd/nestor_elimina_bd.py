#!/usr/bin/env python
import pika
import time
import os
import pymongo

from pymongo import MongoClient
client = MongoClient()
time.sleep(30)


########### CONNEXIÓN A RABBIT MQ #######################
HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'nestor'
channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="eliminar", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='nestor', queue=queue_name, routing_key="eliminar")


##########################################################


########## ESPERA Y HACE UN BUSQUEDA WIKIPEDIA CUANDO RECIBE UN MENSAJE ####

print(' [*] Waiting for messages. To exit press CTRL+C')

#########CONEXION MONGODB############
client = MongoClient(host=os.environ['MONGO_HOST'], port=int(os.environ['MONGO_PORT']))
db = client.slack
link = db.link
fecha = db.fecha
cierre_semestre = db.cierre
programa_c = db.programa

print(db)
def callback(ch, method, properties, body):
    print(body)
    if str(body).startswith("b'[rm_link]"):
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='eliminando coleccion "link" de slack')
        link.drop()
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='eliminado correctamente.')

    if str(body).startswith("b'[rm_fecha]"):
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='eliminando coleccion "fecha" de slack')
        link.fecha()
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='eliminado correctamente.')
        
    if str(body).startswith("b'[rm_cierre_semestre]"):
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='eliminando coleccion "cierre" de slack')
        cierre_semestre.drop()
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='eliminado correctamente.')

    if str(body).startswith("b'[rm_programa]"):
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='eliminando coleccion "programa" de slack')
        programa_c.drop()
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='eliminado correctamente.')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

###########################################################
