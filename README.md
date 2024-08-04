# encode-decode



This Project is basically an encoder and decode of text file contents.
Lets say you have a text file called helloworld.txt the program will encode the contents of the file and write it in andother file that you have provided.
now lets presume you have stored the encoded content in a file named encoded.txt and you want to view the contents, you can read encoded.txt and display the decoded contents.



CONTENTS OF THE PROJECT:

library used:
base64

user defined packages:
decoder
encoder

program:
main_program.py



HOW IT WORKS:
message_encoder.py:
encodes in message in base 16,32,64 and 85 then returns the encoded message

message_decoder.py:
decodes the encoded message in 85,64,32 and 16 then returns the decoded message

main_program.py:
Gets choice of user to encode or decode file

if choice = encode:
gets file address to be read and
gets file address to write the encoded message
reades file content
writes encoded content in file provided by user

if choice = decode:
gets file address of encoded file
decodes and displays the decoded contents of encoded file
