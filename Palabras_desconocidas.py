meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "BATMAN" : "Una risa ligera",
            "BANEAR" : "Impedir el acceso de un usuario a un foro o sitio",
            "ADMIN" : "Es la persona que alguien elige para controlar un servidor",
            "ASAP" : "Significa lo más pronto posible (As Soon As Possible)",
            "AFK" : "Se utiliza en videojuegos cuando un jugador esta ausente (Away From Keyboard)",
            "BTW" : "Significa por cierto (By The Way)",
            "DELAY" : "Se utiliza en videojuegos cuando los movimientos están retrasados",
            "IDK" : "Significa no lo sé (I Don't Know)",
            "IMO" : "Significa en mi opinion (In My Opinion)",
            "KICK" : "Expulsar a un usuario de un chat, pero a diferencia de banear se te permite volver a entrar",
            "LAG" : "Retraso de una comunicacion usualmente por fallos en la coneccion a internet",
            "RATIO" : "Se utiliza en Twitter o X cuando las respuestas al tweet som mayores que los me gusta, significa que los comentarios son negativos y el contenido es malo",
            "SPOILER" : "La revelacion de un suceso importante en una trama o pelicula, se suele tratar de evitar",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
    
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("No tenemos esta palabra")
