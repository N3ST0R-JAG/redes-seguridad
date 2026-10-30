import socket as sk
import time as tm

nombre = input("Dominio a resolver: ").strip()
inicio = tm.perf_counter()
try:
    canonico, alias, ips = sk.gethostbyname_ex(nombre)
except sk.gaierror:
    print("No se pudo resolver", nombre)
    raise SystemExit(1)

ms = (tm.perf_counter() - inicio) * 1000

print("Nombre canónico: ", canonico)
for ip in ips:
    print("IP: ", ip)
print("Tiempo de resolucion: {:.1f} ms".format(ms))

try:
    print("Resolución inversa: ", sk.gethostbyaddr(ips[0])[0])
except sk.herror:
    print("Resolución inversa: sin registro")