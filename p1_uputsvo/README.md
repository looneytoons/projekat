## Uputsvo za preuzimanje slike prilikim odbrane P1

* Preuzmite **client.py** i snimite ga u **ISTI** direktorijum gde vam se nalazi kod ili notebook koji koristite za P1
* U vašem kodu importujte klasu SCClient iz client.py na sledeći način:

```python
from client import SCClient
```

* Inicijalizujte klijenta za preuzimanje slika:

```python
# parametri konstruktora
# code - šifra zadatka - daće vam asistent
# indeks - vaš broj indeksa
# ip - adresa servera koji isporučuje slike - daće vam asistent
scclient = SCClient(code='xxxxx', indeks='RAXX/2012', ip='0.0.0.0', port=8080)
```

* Zatim preuzmite slike:

```python
scclient.download_imgs()
```

* Ako sve prođe kako treba, slike bi trebalo da budu u istom direktorijumu gde vam se nalazi kod ili notebook koji koristite
* Sliku *_train.jpg* koristite za obučavanje neuronske mreže, a na slici *_test.jpg* treba izvršiti prepoznavanje
* Kada završite sa odbranom P1, zatvorite klijenta:

```python
scclient.close()
```
