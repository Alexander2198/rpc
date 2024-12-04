# server.py
from xmlrpc.server import SimpleXMLRPCServer

# Función para concatenar dos cadenas
def concatenate(str1, str2):
    return str1 + " " + str2

# Función para dividir una cadena en palabras
def split_string(string):
    return string.split()

# Crear el servidor
server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC en ejecución en puerto 8000...")

# Registrar las funciones
server.register_function(concatenate, "concatenate")
server.register_function(split_string, "split_string")

# Iniciar el servidor
server.serve_forever()
