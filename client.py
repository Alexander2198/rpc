# client.py
import xmlrpc.client

# Conectar al servidor RPC
server = xmlrpc.client.ServerProxy("http://localhost:8000")

# Llamar a las funciones remotas
result_concat = server.concatenate("Hola", "Mundo")
result_split = server.split_string("Esto es un ejemplo de RPC")

print(f"Resultado de la concatenación: {result_concat}")
print(f"Resultado de dividir la cadena: {result_split}")

