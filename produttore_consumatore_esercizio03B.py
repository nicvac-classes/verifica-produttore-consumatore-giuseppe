import threading
import random

DIM_BUFFER = 7
N_PRODUTTORI = 4
N_CONSUMATORI = 3
N_RICHIESTE = 4

buffer = [None] * DIM_BUFFER
metti = 0
togli = 0

vuoto = threading.Semaphore(DIM_BUFFER)
pieno = threading.Semaphore(0)
mutexP = threading.Semaphore(1)
mutexC = threading.Semaphore(1)


def genera_drone():
    return f"DRN-{random.randint(100, 999)}"


class ProduttoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    # DA IMPLEMENTARE (run)

      def run(self):
        global buffer, metti
        
        for _ in range(N_RICHIESTE):
            drone = genera_drone()  
            vuoto.acquire() 
            mutexP.acquire()  
            
            buffer[metti] = drone
            print(f"[PRODUTTORE {self.idx}] Ha inserito {drone} nello slot {metti}")
            metti = (metti + 1) % DIM_BUFFER
            
            mutexP.release()
            pieno.release()   
            time.sleep(random.uniform(0.1, 0.5));



class ConsumatoreThread(threading.Thread):
    def __init__(self, idx);
        super().__init__()
        self.idx = idx

    # DA IMPLEMENTARE (run)
     def run(self);
        global buffer, togli
        
        while True:
            pieno.acquire()   
            mutexC.acquire()  
            
            drone = buffer[togli]
            togli = (togli + 1) % DIM_BUFFER
            
            mutexC.release()
            vuoto.release()  
            
            if drone is None:
                print(f"[CONSUMATORE {self.idx}] Ricevuto segnale di chiusura. Termino.")
                break
                
            print(f"[CONSUMATORE {self.idx}] Ha prelevato ed elaborato {drone}")
            time.sleep(random.uniform(0.2, 0.6))



def main():
    global metti

    produttori = [ProduttoreThread(i + 1) for i in range(N_PRODUTTORI)]
    consumatori = [ConsumatoreThread(i + 1) for i in range(N_CONSUMATORI)]

    # DA IMPLEMENTARE: start dei thread produttori e consumatori
       for p in produttori:
        p.start()
        for c in consumatori:
        c.start()


    # DA IMPLEMENTARE: join di tutti i produttori
     for p in produttori:
        p.join()

    print("Tutti i sensori hanno terminato. Chiusura piste...")


    # Invia una sentinella None per ogni pista attiva.
    for _ in range(N_CONSUMATORI):
        # DA IMPLEMENTARE: inserire None nel buffer
        for _ in range(N_CONSUMATORI):
        vuoto.acquire()
        mutexP.acquire()
        
        buffer[metti] = None
        metti = (metti + 1) % DIM_BUFFER
        
        mutexP.release()
        pieno.release()


    # DA IMPLEMENTARE: join di tutti i consumatori
     c.join()
    print("Torre operativa chiusa.")
    if __name__ == "__main__":
    main()
