# Token Scheduler (Bank) :bank:

Welcome to this project! This system is implementation of the token system used in banks. It is designed to be used in a LAN environment. It is build using python. It is a part of the Operating Systems course at Dayananda Sagar College of Engineering.

## Features :sparkles:

- Token generation:You can generate tokens for all the bank services.
- Token display: Watch your tokens appear on the screen.
- Use of multiple counters: Call tokens from different counters simultaneously.

## Installation :computer:

this project relies on some external libraries. To install them, run the following command:

```bash
pip install -r requirements.txt
```


## Usage :clipboard:

For this Project to run you ideally need 3 computers connected to a common network. One computer will act as the server and the other two will act as clients. The server will be used to generate tokens and the clients will be used to display the tokens and call them.

In each code you have to specify the IP address of the server. The IP address of the server can be found by running the following command on the server computer:
```ipconfig``` (for Windows)
```ifconfig``` (for linux)
IP should start with 192.168.XX.XXX

### Server
Go to the server folder and run the following command:
```bash
cd "Scheduler and Server"
python3 main.py
```
This will start the server. and print Server is Up on terminal and a GUI showing current tokens

### Client Generator
Go to the client folder and run the following command:
```bash
cd Client
python3 client_generator.py
```
This will show you a UI which has 4 buttons to generate tokens clicking on them will generate a token and send it to Server

### Client Counter
Go to the client folder and run the following command:
```bash
cd Client
python3 client_counter.py
```
This is for Bank staff it has two buttons one to call the Next token and other to Hold the token

### Note
You Must have exactly One server and Generator and at least one counter for the system to work. You can also run all of the above on a single computer. In that case you have to run the server first and then the generator and counter. and set the IP to 127.0.0.1 on Port 1234 (which is default also)

## FAQ

### How does it work? 


The system is composed of two main parts: the server and the client. The server is responsible for managing the tokens and the queues, while the client is responsible for displaying the tokens and calling them. The server and the client communicate with each other using websockets.

### Wait banks already have token systems, why do we need this? :thinking:

Good Question!
 This system dont require complicated softwares and expensive hardware even a Pi Zero will do. This system is also very easy to setup and use. Not to mention it is also very cheap to make. This system is also very flexible and can be modified to suit your needs. It can also be used in other places like hospitals, restaurants, etc.


## License :page_facing_up:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details