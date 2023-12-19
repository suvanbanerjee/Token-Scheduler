# Token Scheduler (Bank) :bank:

Welcome to this project! This system will change the way you wait in line at the bank. No more boring queues, we've got you covered!

## Features :sparkles:

- Token generation: Once you're registered, you can generate tokens for all the bank services.
- Token display: Watch your tokens appear on the screen.
- Use of multiple counters: Our bank staff is so efficient, they can call tokens from different counters simultaneously.
- Use of Completely Fair Scheduler (CFS): We believe in fairness, so we call tokens so that nobody waits.

## Installation :computer:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/token-scheduler.git
    ```

2. Install the required dependencies:

    ```bash
    npm install
    ```

3. Start the application:

    ```bash
    npm start
    ```

## Usage :clipboard:

1. Open the application in your web browser.
2. Register as a customer by providing your personal information. Don't worry, we won't ask for your secret superhero identity.
3. Generate a token for the desired service.
4. Wait for your token to be called by our super friendly bank staff. They might even crack a joke or two!
5. Check the status of your token and see how many lucky people are ahead of you. Patience is a virtue, my friend!

## FAQ

### How does it work? 


The system is composed of two main parts: the server and the client. The server is responsible for managing the tokens and the queues, while the client is responsible for displaying the tokens and calling them. The server and the client communicate with each other using websockets.

### Wait banks already have token systems, why do we need this? :thinking:

Good Question!
 Most banks use a simple FIFO (First In, First Out) system, which means that the first person to arrive is the first to be served. This is not fair, because some services take longer than others. For example, if you're only going to deposit money, you shouldn't have to wait behind someone who wants to open a new account. Our system uses the CFS algorithm to ensure that everyone is served in a fair manner.



## Contributing :raised_hands:

We love contributions! If you have any ideas or suggestions to make this project even more awesome, please open an issue or submit a pull request. Let's make waiting in line a fun experience!
