import socket
import threading
from datetime import datetime


threds = []
ports_ouvert = {}


def verifie_port(ip, port, delai, ports_ouvert):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(delai)
    resultat = sock.connect_ex((ip, port))

    if resultat == 0:
       ports_ouvert[port] ='ouvert'
       return True

def scannage_ports(host_ip, delai):
    """
    Fonction qui scanne les ports d'un hote, en prenant en paramètre l'adresse IP ciblé et le temps d'exécution des threads.
    Elle retourne le numéro du port, l'état et précise le sevice correspondant
    """

    for port in range(1, 1025):
        thread = threading.Thread(target=verifie_port, args= (host_ip, port, delai, ports_ouvert))
        threds.append(thread)

    for i in range(0, 1024): threds[i].start()

    for i in range(0, 1024): threds[i].join()

    for key, value in ports_ouvert.items():
        try:
            return ("Le port  {}  est {}, service correspondant: {}".format(key, value, socket.getservbyport(key, "tcp")))
        except:
            return ("Le port  {}  est {}, service: {}".format(key, value, "inconnue"))

#Fonction principale
def main():
    try:
        host_ip = input("Entrez l'adresse IP à scanner: ")

    except socket.gaierror:
        print("Le nom d'hote entrée est incorrect")

    t1 = datetime.now()
    print("\nTemps initiale: {}\n".format(t1))

    print(scannage_ports(host_ip, 0.001))

    t2 = datetime.now()
    print("\n\nTemps fininal: {}".format(t2))

    print("\nDurée: {}".format(t2 - t1))


if __name__ == '__main__':
    main()
