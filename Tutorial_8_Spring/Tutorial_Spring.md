#Tutorial Spring
Este tutorial está basado en la guía oficial de Spring.

Usaremos [start.spring.io](start.spring.io) para crear un proyecto web con Spring Boot, en la sección 'Dependencies' agregamos Spring Web y luego generamos nuestro proyecto.

A continuación descomprimiremos nuestros archivos y buscaremos el archivo llamado DemoApplication.java que se encuentra en la carpeta src/main/java/com/example/demo. Cambiaremos el contenido de este archivo por el siguiente:

    package com.example.demo;
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestParam;
    import org.springframework.web.bind.annotation.RestController;

    @SpringBootApplication
    @RestController
    public class DemoApplication {      
        public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
        }

        @GetMapping("/hello")
        public String hello(@RequestParam(value = "name", defaultValue = "World") String name) {
        return String.format("Hello %s!", name);
        }      
    }

El método hello() está diseñado para tomar un parámetro String 'name' y luego combinarlo con la palabra Hello. La idea es que si te llamas Juan, retorne Hello Juan!

La anotación @RestController le dice a Spring que el código describe un endpoint que debe estar disponible en la web. @GetMapping("/hello") le dice a Spring que use el método hello() para responder las solicitudes que se envíen a la dirección http://localhost:8080/hello. Finalmente, @RequestParam le está diciendo que espere un valor 'name' en la solicitud, pero que si no está use la palabra 'World'.

Para ejecutar el programa, nos ubicamos donde tenemos los archivos del proyecto en la consola y ejecutamos el comando

    $./mvnw spring-boot:run

Si abrimos el navegador y nos dirigimos a http://localhost:8080/hello deberíamos ver el mensaje en la pantalla.

##RESTful Web Services
A continuación construiremos un servicio que acepte solicitudes HTTP GET en http://localhost:8080/greeting. Esta responderá con una representación JSON de un saludo como el que vemos aquí:

    {"id":1,"content":"Hello, World!"}

Se puede personalizar con un parámetro opcional 'name' en la cadena de la consulta:

    http://localhost:8080/greeting?name=User

Este parámetro sobrescribe la palabra 'World' en el saludo.

Para todas las aplicaciones Spring deberíamos usar el [Spring Initializr](https://start.spring.io), este nos ofrece una forma rápida de incorporar todas las dependencias que necesitamos y realiza gran parte de la configuración. para este ejemplo solo necesitamos Spring Web.

###Crear Clase de Representación de Recursos
Ahora que tenemos la forma inicial de nuestro proyecto, podemos crear nuestro servicio web.

Este servicio manejará solicitudes GET para /greeting, con un parámetro opcional 'name'. La solicitud GET debe retornar la respuesta 200 OK con un JSON que representa el saludo. Este se debe ver algo así:

    {
        "id": 1,
        "content": "Hello, World!"
    }

El campo 'id' es un identificador único para el saludo, 'context' es la representación textual del saludo.

Para modelar la representación del saludo, creamos una clase de representación de recursos. Para hacer esto proporcionamos un objeto Java simple con campos, constructores y accesors para los datos de 'id' y 'content' y lo guardamos en 'src/main/java/com/example/restservice/Greeting.java' de la siguiente forma:

    package com.example.restservice;

    public class Greeting {

    	private final long id;
    	private final String content;

    	public Greeting(long id, String content) {
    		this.id = id;
    		this.content = content;
    	}

    	public long getId() {
    		return id;
    	}

    	public String getContent() {
    		return content;
    	}
    }

###Crear un Controlador de recursos
En el enfoque de Spring para crear servicios web RESTful, las solicitudes HTTP son manejadas por un controlador. Estos componentes son identificados por la anotación @RestController, y el @GreetingController maneja las solicitudes GET para /greeting devolviendo una nueva instancia de la clase Greeting. Ambas se muestran en el siguiente código y que debemos guardar en la ubicación 'rc/main/java/com/example/restservice/GreetingController.java':

    package com.example.restservice;

    import java.util.concurrent.atomic.AtomicLong;

    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestParam;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    public class GreetingController {

    	private static final String template = "Hello, %s!";
    	private final AtomicLong counter = new AtomicLong();

    	@GetMapping("/greeting")
    	public Greeting greeting(@RequestParam(value = "name", defaultValue = "World") String name) {
    		return new Greeting(counter.incrementAndGet(), String.format(template, name));
    	}
    }

Este controlador es conciso y simple, sin embargo hay muchas cosas pasando por debajo.

La anotación @GetMapping asegura que las solicitudes HTTP GET para /greeting se asignen al método greeting().

La anotación @RequestParam une el valor del parámetro 'name' en la consulta con el parámetro 'name' del método greeting(). Si el parámetro está ausente en la consulta, se usa el valor por defecto.

La implementación del cuerpo del método crea y retorna un nuevo objeto Greeting con atributos 'id' y 'content' basados en el siguiente valor del contador y formatea el nombre dado usando la plantilla del saludo.

Este código usa la anotación de Spring @RestController la cual marca la clase como un controlador donde cada método retorna un objeto de dominio en vez de una vista. Es una forma abreviada que incluye @Controller y @ResponseBody.

La anotación @SpringBootApplication es una muy conveniente que añade:
- @Configuration: Etiqueta a la clase como fuente de definiciones bean para el contexto de la aplicación.
- @EnableAutoConfiguration: Le dice a Spring Boot que comience a agregar beans basado en el classpath, otros beans, y varias configuraciones de propiedades.
- @ComponentScan: Le dice a Spring que busque otros componentes, configuraciones y servicios en el paquete com/example, dejándolo encontrar los controladores.

El método main() usa el método SpringApplication.run() de Spring Boot para iniciar la aplicación.

###Construir un ejecutable JAR
La aplicación se puede ejecutar por lineas de comando con Gradle o Maven, pero también se puede construir un ejecutable JAR.
En caso que se esté usando Gradle se puede ejecutar usando './gradlew bootRun'. El ejecutable se puede hacer usando '.gradlew build' y luego se ejecuta el JAR de la siguiente forma:

    $java -jar build/libs/gs-rest-service-0.1.0.jar

En el caso de Maven se usa './mvnw spring-boot:run' o para el JAR './mvnw clean package' y luego:

    $java -jar target/gs-rest-service-0.1.0.jar

###Probar el Servicio
Ahora que levantamos el servicio, visitamos http://localhost:8080/greeting donde deberíamos ver:

    {"id":1,"content":"Hello, World!"}

Si ahora le damos un nombre usando http://localhost:8080/greeting?name=User, deberíamos ver:

    {"id":2,"content":"Hello, User!"}

Este cambio demuestra que @RequestParam está funcionando como corresponde. El hecho de que el id también cambie demuestra que se está trabajando sobre la misma instancia de GreetingController y que su contador está aumentando como se espera.
