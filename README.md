# SPL_for_Networking_cryptography_systems

A software product line with foucos on messages cryptography methods using networking concepts such as socket, network architecture, transport protocols.

## What can it do
- Encrypt a given message using blowfish, AES, RSA and TripleDes techniques.
- Decrypt a given message
- Perform multithread server connection, encrypting/decrypting multiple clients messages

## What will be able to do
- Encrypt a given message using others techniques.
- Maybe a graphic interface

## How to run
1. Install the dependencies used in this project, by running the following command in your terminal:
```
    pip install -r requirements.txt
```

2. As it was built TCP-based, you need to enable the server before making new connections.

```
    python3 src/multithread_server.py
```

3. Now is up to the client (or clients), open a new terminal and have fun!
```
    python3 src/client.py
```

```
    ╔╦╦╦═╦╗╔═╦═╦══╦═╗╔══╦═╗╔═╦╗╔═╦╦╦╦═╦╦══╦╦╗
    ║║║║╦╣╚╣╠╣║║║║║╦╣╚╗╔╣║║║╣╣╚╣║║║║║╔╣╠╗╚╣═║
    ╚══╩═╩═╩═╩═╩╩╩╩═╝.╚╝╚═╝╚═╩═╩═╩══╩╝╚╩══╩╩╝
```