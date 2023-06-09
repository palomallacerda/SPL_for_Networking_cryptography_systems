import socket
import argparse
from rich.console import Console
from rich.progress import Progress
import time

console = Console()

def menu(action, user_message, return_message, key, encp_method):
        console.print(" ╔╦╦╦═╦╗╔═╦═╦══╦═╗╔══╦═╗╔═╦╗╔═╦╦╦╦═╦╦══╦╦╗", style='bold red')
        console.print(" ║║║║╦╣╚╣╠╣║║║║║╦╣╚╗╔╣║║║╣╣╚╣║║║║║╔╣╠╗╚╣═║", style='bold red')
        console.print(" ╚══╩═╩═╩═╩═╩╩╩╩═╝.╚╝╚═╝╚═╩═╩═╩══╩╝╚╩══╩╩╝", style='bold red')
        console.print('                              [i]your encryptation program[/i]\n\n[b]Make a wish[b]')
        console.print('[1] Encrypt\n[2] Decode\n[3] E X I T\n')
        action = input('> ')
        sck.send(action.encode('utf-8'))

        if action == '1':
            console.print('\nGive me a message', style='bold red')
            user_message = input('>> ')
            sck.sendall(user_message.encode('utf-8'))
            console.print('\nGive me a key with minimum 8 caracters', style='bold red')
            key = input('>> ')
            sck.sendall(key.encode('utf-8'))
            console.print('\nChoose a encryption Method', style='bold red')
            console.print('\nA) AES\nB) Blowfish\nC) RSA\nD) TripleDes', style='bold red')
            encp_method = input('>> ')

            if((encp_method == 'A') or (encp_method == 'a') or (encp_method == 'b') or  (encp_method == 'B' ) or (encp_method == 'C' ) or (encp_method == 'c')) or (encp_method == 'd') or (encp_method == 'D'):
                sck.sendall(encp_method.encode('utf-8'))

            return_message = sck.recv(1024)
            with Progress() as progress:
                        taks_1 = progress.add_task("[yellow]Processing....", total=100)
                        time.sleep(0.3)
                        while not progress.finished:
                            progress.update(taks_1, advance=40)
                            time.sleep(1)
            console.print("\nENCRYPTED MESSAGE", style='bold yellow')
            print(return_message.decode())
            time.sleep(0.5)
            console.print("\nRESTARTING SYSTEM....", style='bold yellow')
            time.sleep(2)

        elif action == '2':
                console.print('\nGive me a encrypted message', style='bold red')
                user_message = input('>> ')
                sck.sendall(user_message.encode('utf-8'))
                console.print('\nGive me a key with minimum 8 caracters', style='bold red')
                key = input('>> ')
                
                sck.sendall(key.encode('utf-8'))
                
                console.print('\nA) AES\nB) Blowfish\nC) RSA\nD) TripleDes', style='bold red')
                encp_method1 = input('>> ')
                if(encp_method == encp_method1):
                    if((encp_method1 == 'A') or (encp_method1 == 'a') or (encp_method1 == 'b') or  (encp_method1 == 'B' ) or (encp_method1 == 'C' ) or (encp_method1 == 'c')) or (encp_method1 == 'd') or (encp_method1 == 'D'):
                        sck.sendall(encp_method1.encode('utf-8'))
                        decrypted_message = sck.recv(1024)
                else:
                    sck.sendall(' '.encode('utf-8'))
                    console.print("\nDifferents methods of encoding and decoding\n", style='bold yellow')
                    decrypted_message = ' '.encode()

                decrypted_message = decrypted_message.decode()
                with Progress() as progress:
                    taks_1 = progress.add_task("[yellow]Processing....", total=100)
                    time.sleep(0.3)
                    while not progress.finished:
                        progress.update(taks_1, advance=40)
                        time.sleep(1)
                if decrypted_message == ' ':
                    console.print("\nERROR\n", style='bold yellow')
                    time.sleep(0.5)
                    console.print("\nFollow these steps:\n", style='Green')
                    console.print("\n--> Verify if the typed key matches the true decoder key\n", style='Green')
                    console.print("\n--> Verify if your message is corretly encrypted or mistyped\n", style='Green')
                    console.print("\n--> Verify if you've tried to decode with the correct method\n", style='Green')               
                    time.sleep(1)
                    console.print("NOW, TRY AGAIN....", style='bold yellow')
                else:
                    console.print("\nDECODED MESSAGE", style='bold yellow')
                    time.sleep(0.7)
                    print(decrypted_message)
                    time.sleep(0.5)
                    console.print("\nRESTARTING SYSTEM....", style='bold yellow')
                    time.sleep(2)

        elif action == '3':
            console.print("Shutting down server...", style='bold yellow')
            time.sleep(0.5)
            return

        else:
            console.print("Wrong input try again", style='bold yellow')
            time.sleep(0.5)
        menu(action, user_message, return_message, key, encp_method)

parser = argparse.ArgumentParser(description="This is a client for multthreads connections")
parser.add_argument('--host', metavar= 'host', type= str, nargs='?', default= socket.gethostname())
parser.add_argument('--port', metavar= 'port', type= int, nargs='?', default= 14000)
arg = parser.parse_args()
print(f"Connecting to server: {arg.host} on port {arg.port}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
    try:
        sck.connect((arg.host, arg.port))
    except Exception as e:
        raise SystemExit(f"We cant connect to {arg.host} on {arg.port} because: {e}")
    while True:
        action = ''
        user_message = ''
        return_message = ''
        key = ''
        encp_method = ''
        shut = menu(action, user_message, return_message,key,encp_method)
        break