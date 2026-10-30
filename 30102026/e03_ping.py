import platform as pf
import subprocess as sp

def hacer_ping(host):
    if pf.system().lower() == "windows":
        comando = ["ping", "-n", "1", "-w", "1000", host]
    else:
        comando = ["ping", "-c", "1", "-W", "1", host]

    try:
        resultado = sp.run(comando, stdout=sp.DEVNULL, stderr=sp.DEVNULL, timeout=5)

        return resultado.returncode == 0
    except (sp.TimeoutExpired, FileNotFoundError):
        return False


host = input("Host IP a probar: ").strip()
if hacer_ping(host):
    print(host, "responde")
else:
    print(host, "no responde")