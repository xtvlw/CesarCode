alphabet, n = 'abcdefghijklmnopqrstuvwxyz', 0
final_message,final_messageD, key = '', '', 3
message = input('message : ').lower()
for i in range(len(message)):
    x = int(alphabet.find(message[n]))
    if message[n] in alphabet:
        final_message += alphabet[(x + key) % len(alphabet)]
        final_messageD += alphabet[(x - key) % len(alphabet)]
    else:
        final_message += message[n]
        final_messageD += message[n]
    n += 1
print(final_message, '\n', final_messageD)
