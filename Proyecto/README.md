# Proyecto: Desarrollo de un bot (slack)

- **Por el momento el bot de slack accede a una base de datos para luego publicarlo en el canal, ademas se implemento docker**


### Comandos utiles
    - docker run -v $(pwd)/mongodata:/data/db --name "nestor_mongo" mongo &
    - docker exec -it nestor_mongo bash  , con este comando entro al contenedor de manera interactiva para crear la base de datos con los siguientes comandos.
      - mongo
      - use nestor
      - db.frase.insert({text:'ingrese texto'})
      - exit
    - docker-compose build
    - docker-compose up
     
