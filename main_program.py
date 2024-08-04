import sys
import encoder.message_encoder as en
import decoder.message_decoder as de

def file_reader(read):
    try:
        with open(read, 'r') as re:
            ls = []
            for i in re:
                x = en.encode(i.strip())
                ls.append(x)

        return ls
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def file_writer(write, x):
    try:
        with open(write, 'w') as wr:
            for i in x:
                wr.write(i.decode() + '\n')

    except Exception as e:
        print(f"Error writing file: {e}")

def file_decoder(read):
    try:
        with open(read, 'r') as re1:
            ls = []
            for i in re1:
                x = de.decode(i.strip())
                ls.append(x)
            print(ls)
    except Exception as e:
        print(f"Error decoding file: {e}")

print("File Content Encoder/Decoder\nMENU\n1.Encode the given file\n2.Decode the file")
sys.stdout.flush()  # Ensure immediate output

try:
    ch = int(input("Enter Choice = "))

    if ch == 1:
        read = input("Enter the address of the file to be read = ")
        write = input("Enter the address where the encoded file is stored = ")
        x = file_reader(read)
        if x:  # Only write if encoding was successful
            file_writer(write, x)

    elif ch == 2:
        read = input("Enter the address of the file to be read = ")
        file_decoder(read)

    else:
        print("Invalid choice. Please enter 1 or 2.")
except ValueError:
    print("Invalid input. Please enter a number.")
