# IBIS Projekat - SCADA Simulator

Ovaj repozitorijum sadrži projekat iz predmeta IBIS koji su izradili Milos Pantelić, Cvjetin Glisić i Stefan Popović.

## Opis Projekta

U okviru projekta implementiran je sistem za nadgledanje i kontrolu parametara unutrašnjeg prostora. Za implementaciju su korišćeni programski jezik Python, EMQX aplikacija (koja implementira MQTT protokol kao Docker kontejner), Hive MQTT Broker (koji takođe implementira MQTT protokol) i InView Cloud SCADA.

![image](https://github.com/user-attachments/assets/85ff042e-24f6-4f70-83e0-1561c9d779ff)

Aplikacija se sastoji od tri glavne komponente: Simulatora, Klijenta i InView SCADA sistema, koji međusobno komuniciraju putem MQTT protokola.

### Simulator

Simulator je Python aplikacija koja koristi dokerizovanu EMQX aplikaciju za simulaciju MQTT protokola i komunicira sa MQTT Klijentom. Unutar Simulatora se izvršava logika provere trenutnih parametara i simulira ponašanje sistema u zavisnosti od toga da li su određeni uređaji uključeni ili isključeni.

### MQTT Klijent

MQTT Klijent, takođe Python aplikacija, komunicira sa Simulatorom i InView SCADA sistemom putem MQTT protokola. Unutar MQTT Klijenta se proveravaju parametri senzora i upravljaju uređajima na osnovu graničnih vrednosti kako bi očitavanja senzora ostala u normalnim granicama. HiveMQ Broker omogućava komunikaciju sa SCADA sistemom koristeći paho-mqtt paket.

### InView SCADA

InView Cloud SCADA služi za vizuelni prikaz događaja i promena u sistemu.

## Uputstvo za Pokretanje Sistema

1. Preuzmite Docker sliku za EMQX broker izvođenjem sledeće komande u terminalu:
    ```sh
    docker pull emqx:latest
    ```

2. Pokrenite EMQX broker koristeći sledeću komandu:
    ```sh
    docker run -d --name emqx -p 18083:18083 -p 1883:1883 emqx:latest
    ```

3. Nakon uspešnog pokretanja EMQX brokera putem Docker-a, pokrenite `Startup.py` unutar Simulatora i SCADA Klijenta.

4. Na InView SCADA sistemu možete pratiti promene vrednosti i uključivanje/isključivanje uređaja.
