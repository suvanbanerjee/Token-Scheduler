# Token Scheduler (Bank) :bank:

Welcome to this project! This system will change the way you wait in line at the bank. No more boring queues, we've got you covered!

## Features :sparkles:

- Token generation:You can generate tokens for all the bank services.
- Token display: Watch your tokens appear on the screen. Like a Movie.
- Use of multiple counters: Our bank staff is so efficient, they can call tokens from different counters simultaneously.
- Use of Completely Fair Scheduler (CFS): We believe in fairness, so we call tokens so that nobody waits long.

## Installation :computer:

TODO

## Usage :clipboard:

TODO

## FAQ

### How does it work? 


The system is composed of two main parts: the server and the client. The server is responsible for managing the tokens and the queues, while the client is responsible for displaying the tokens and calling them. The server and the client communicate with each other using websockets.

### Wait banks already have token systems, why do we need this? :thinking:

Good Question!
 Most banks use a simple FIFO (First In, First Out) system, which means that the first person to arrive is the first to be served. This is not fair, because some services take longer than others. For example, if you're only going to deposit money, you shouldn't have to wait behind someone who wants to open a new account. Our system uses the CFS algorithm to ensure that everyone is served in a fair manner.


## Notice :warning:

This project is a part of the Operating Systems course at Dayananda Sagar College of Engineering. The use of Network sockets is used without encryption and is not secure. Moreover it is not intended to be used on a internet connected network. It is only intended to be used on a LAN. The developers are not responsible for any loss of data or any other damages caused by the use of this software. Use at your own risk.
