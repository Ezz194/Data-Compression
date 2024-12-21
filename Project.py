import subprocess
def shl_selection():
    
    result = subprocess.run(['zenity','--file-selection'],capture_output = True,text=True)
    if (result.stdout):
        pth_Entry.delete(0,'end')
        pth_Entry.insert(0,result.stdout.strip())

def LZW_compression(input_string):
    #This creates a dictionary where each character (from ASCII code 0 to 127) is mapped to its corresponding ASCII code.
    #chr(i) converts the integer i to its corresponding character (e.g., chr(65) returns 'A').
    dictionary = {chr(i): i for i in range(128)}
    #dict_size keeps track of the next available code for the dictionary. It starts at 128 because the first 128 codes are already taken by the ASCII characters.
    dict_size = 128
    #current_string
    current_string = ""
    #output
    compressed_data = []

    for char in input_string:
        combined_string = current_string + char
        if combined_string in dictionary:
            current_string = combined_string
        else:
            
            compressed_data.append(dictionary[current_string])
            # Add the new string to the dictionary
            dictionary[combined_string] = dict_size
            dict_size += 1
            current_string = char

    # Add the last string's code to the output
    if current_string:
        compressed_data.append(dictionary[current_string])

    return compressed_data

def LZW_decompression(compressed_data):
    """Decompress a list of integers using the LZW algorithm."""
    # Build the initial dictionary with single character mappings starting from 128.
    dictionary = {i: chr(i) for i in range(128)}
    dict_size = 128

    # Initialize decompression variables
    current_code = compressed_data.pop(0)
    pre_string = dictionary[current_code]
    decompressed_data = [pre_string]

    for code in compressed_data:
        if code in dictionary:
            #dictionary[code] ==pattern
            #If the code is already in the dictionary, we get the corresponding pattern (current).
            current = dictionary[code]
        elif code == dict_size:
            # Special case for the dictionary's next addition
            current = pre_string + pre_string[0]
        else:
            raise ValueError("Invalid compressed data.")

        decompressed_data.append(current)

        # Add new sequence to the dictionary
        #Set pre_string to the current pattern, because it's needed for the next iteration
        dictionary[dict_size] = pre_string + current[0]
        dict_size += 1

        pre_string = current

    return "".join(decompressed_data)
    
def RLE(input_string):
    # Handle empty input
    if not input_string:
        return ''
    prev_char = input_string[0]
    encoded_string = '' # Initialize the encoded string
    count = 1 # Initialize count for the first character
    # Iterate through the string starting from the second character
    for char in input_string[1:]:
        if char == prev_char:
            count += 1 # Increment count if the same character is found
        else:
            encoded_string += prev_char + str(count) # Append character and
            prev_char = char # Update previous character
            count = 1 # Reset count for the new character
    # Append the Last character and its count
    encoded_string += prev_char + str(count)
    return encoded_string


def RLD(txt):
    pass

def huff_encoding(text):
    returnings= {}
    import heapq  # For creating and managing a heap
    from collections import Counter  # For counting character frequencies and creating default dictionaries
    # Step 1: Count the frequency of each character in the text
    # Using Counter from collections to count how many times each character appears
    frequency = Counter(text)
    returnings['frequency']=frequency
    # print(frequency)  # Printing the character frequency dictionary

    # Step 2: Create a priority queue (min-heap) for building the Huffman tree
    # Initializing a heap where each element is a list containing the frequency and character
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    # print(heap)  # Printing the initial heap structure
    heapq.heapify(heap)  # Converting the list into a min-heap
    # print(heap)  # Printing the heap after heapify

    # Step 3: Build the Huffman Tree
    # Combining nodes until there is only one node left (the root of the tree)
    while len(heap) > 1:
        lo = heapq.heappop(heap)  # Removing the smallest element from the heap
        hi = heapq.heappop(heap)  # Removing the next smallest element
        for pair in lo[1:]:  # Adding a '0' to the code for each character in 'lo' subtree
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:  # Adding a '1' to the code for each character in 'hi' subtree
            pair[1] = '1' + pair[1]
        # Combining the two nodes and pushing them back into the heap
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Printing the tree structure containing characters and their corresponding Huffman codes
    # print(heap[0][1:])

    # Step 4: Create a dictionary for Huffman codes
    # Sorting the characters by the length of their Huffman codes, and storing them in a dictionary
    huffman_codes = sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))
    # print(huffman_codes)  # Printing the sorted list of characters with their codes
    huffman_dict = {char: code for char, code in huffman_codes}  # Creating a dictionary from the sorted list
    # print(huffman_dict)  # Printing the dictionary with characters and their Huffman codes

    # Step 5: Encode the text using the Huffman codes
    # Generating the encoded version of the text by replacing each character with its Huffman code
    encoded_text = "".join(huffman_dict[char] for char in text)

    # Step 6: Print the results
    # Displaying the Huffman codes and the encoded version of the text
    returnings['Character Huffman Codes']=huffman_dict
    returnings['Encoded Text']=encoded_text
    # print("Character Huffman Codes:", huffman_dict)
    # print("Encoded Text:", encoded_text)

    # Step 7 (Optional): Compare the original size and the encoded size
    returnings['original_size'] = len(text) * 8  # Calculating the size in bits assuming each character takes 8 bits
    returnings['encoded_size'] = len(encoded_text)  # Calculating the length of the encoded text
    # print(f"Original size: {original_size} bits")  # Printing the original size of the text
    # print(f"Encoded size: {encoded_size} bits")  # Printing the size after encoding
    return returnings

def huff_decoding(txt):
    pass


def starting():
    import os
    Compressed = None  # Initialize variables
    deCompressed = None

    if pth_Entry.get()[-3:] == 'txt':
        with open(pth_Entry.get(), 'r') as source:
            text = source.read()
            choice = tech_combo.get()
            output_file = os.path.join(os.path.dirname(__file__), 'compressed_output.txt')

            if check.get() == 1:  # Compress
                match choice:
                    case 'LZW':
                        Compressed = LZW_compression(text)
                        with open(output_file, 'w') as f:
                            f.write(' '.join(map(str, Compressed)))
                    case 'Run Length Encoding':
                        Compressed = RLE(text)
                        with open(output_file, 'w') as f:
                            f.write(Compressed)
                    case 'Huffman Encoding':
                        huff = huff_encoding(text)
                        Compressed = huff['Encoded Text']
                        sBefore = huff['original_size']
                        sAfter = huff['encoded_size']
                        with open(output_file, 'w') as f:
                            f.write(Compressed)
                    case _:
                        pass
            elif check.get() == 2:  # Decompress
                match choice:
                    case 'LZW':
                        compressed_data = list(map(int, text.split()))
                        deCompressed = LZW_decompression(compressed_data)
                        xtracted_file = os.path.join(os.path.dirname(__file__), 'xtracted_file.txt')
                        with open(xtracted_file, 'w') as f:
                            f.write(deCompressed)
                    case 'Run Length Encoding':
                        deCompressed = RLD(text)
                    case 'Huffman Encoding':
                        deCompressed = huff_decoding(text)
                    case _:
                        pass

        if Compressed is not None or deCompressed is not None:
            subprocess.run(['zenity', '--info', '--text=Done, file saved'], capture_output=True, text=True)
        else:
            subprocess.run(['zenity', '--error', '--text=No code to execute'], capture_output=True, text=True)
    else:
        subprocess.run(['zenity', '--error', '--text=Input a text file'], capture_output=True, text=True)








from tkinter import Tk, Label, Button, ttk, IntVar , Frame , Entry , Radiobutton 
tech_choices= ['Run Length Encoding','Huffman Encoding','LZW']





root = Tk()
root.geometry('605x250')
root.title('Compression / Decompression Tool')
check =IntVar()
main = Frame(root, bg='#04395e')
main.pack(fill='both', expand=True)  



chs_file_lbl = Label(main , text='Choose File',width=20,bg='#04395e',fg='#ff4a26', font = 30,height=2)
pth_Entry = Entry(main,width=25 , bg='black' , fg='#ff4a26', font = 30)
slct_btn = Button(main,text='Select',command=shl_selection,bg = '#04395e',fg='#ff4a26',
                borderwidth=1 , relief='flat',highlightbackground='#ff4a26'
                ,activebackground='#2aaaff',activeforeground='#ff4a26', font = 27)




chs_teq_lbl = Label(main,text='Choose Technique',width=20,bg='#04395e',fg='#ff4a26', font = 30,height=2)
tech_combo = ttk.Combobox(main, values=tech_choices, width=20,height=4 , font=28 )


comp_rd_btn = Radiobutton(main,text='Compress',value=1   ,bg='#04395e',fg='#ff4a26',
                        variable=check,borderwidth=0 , relief='flat',highlightbackground='#ff4a26'
                        ,activebackground='#2aaaff',activeforeground='#ff4a26' , font = 27,height=2)
deco_rd_btn = Radiobutton(main,text='Decompress',value=2  ,bg='#04395e',fg='#ff4a26',
                        variable=check,borderwidth=1 , relief='flat',highlightbackground='#ff4a26'
                        ,activebackground='#2aaaff',activeforeground='#ff4a26', font = 27,height=2)



strt_btn = Button(master=main , text='Start',bg = '#04395e',fg='#ff4a26',
                borderwidth=1 , relief='flat',highlightbackground='#ff4a26'
                ,activebackground='#2aaaff',activeforeground='#ff4a26',
                font = 27,height=2,command=starting)






chs_file_lbl.grid(row=1,column=0 ,padx=10,pady=10 , sticky='w')
pth_Entry.grid(row=1,column=2,columnspan=2,padx=10,pady=10 , sticky='we')
slct_btn.grid(row=1,column=4,padx=10,pady=10 , sticky='e')

chs_teq_lbl.grid(row=2,column=0,padx=10,pady=10 , sticky='we')
tech_combo.grid(row=2,column=2,padx=10,pady=10 , sticky='we',columnspan=3)

comp_rd_btn.grid(row=3,column=0,padx=10,pady=10,sticky='e' )
deco_rd_btn.grid(row=3,column=3,padx=10,pady=10 )

strt_btn.grid(row=4,column=1,columnspan=2,ipadx=10,pady=20 ,sticky='nswe')


root.mainloop()
