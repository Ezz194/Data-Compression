Report on the Compression/Decompression Tool Implementation
This report outlines the design and implementation of the provided code, focusing on its algorithms, architecture, and functionality. The primary purpose of this tool is to compress and decompress text files using multiple encoding techniques, including LZW Compression, Run-Length Encoding (RLE), and Huffman Encoding.

# 1. Algorithms Used
## 1.1 LZW (Lempel-Ziv-Welch) Compression and Decompression
Purpose: LZW is a dictionary-based compression algorithm. It encodes sequences of characters as single dictionary entries, making it efficient for repetitive patterns in text.
Algorithm:
Compression:
Start with an initial dictionary containing all ASCII characters (codes 0–127).
Iterate through the input string, adding new patterns (character sequences) to the dictionary.
Replace recognized patterns with their corresponding dictionary codes.
Decompression:
Initialize the dictionary with ASCII characters.
Use the compressed codes to reconstruct the original patterns by referencing and expanding the dictionary.
Key Features in Code:
The dictionary is dynamically updated during both compression and decompression.
Special handling for cases where a code corresponds to a new dictionary entry.
## 1.2 Run-Length Encoding (RLE)
Purpose: RLE compresses data by encoding consecutive identical characters as a single character followed by a count.
Algorithm:
Traverse the input string.
Count consecutive occurrences of each character and append the character followed by the count to the output.
Key Features in Code:
Efficient encoding through a single loop.
Handles empty input gracefully.
Simple implementation suitable for text with many repeated characters.
## 1.3 Huffman Encoding
Purpose: Huffman encoding is a variable-length compression algorithm that assigns shorter codes to more frequent characters, optimizing compression efficiency.
Algorithm:
Build a frequency table for all characters in the text.
Construct a binary tree (Huffman tree) using a priority queue where nodes with lower frequencies are closer to the root.
Traverse the tree to generate binary codes for each character.
Encode the text using these codes.
Key Features in Code:
Use of heapq for the priority queue.
Creation of a dictionary mapping characters to their binary Huffman codes.
Calculation of compression efficiency (original size vs. encoded size).
# 2. Software Implementation
## 2.1 Core Functions
File Selection:

Uses the zenity command-line tool to create a GUI file selection dialog.
Handles user input for the file path via the shl_selection() function.
Compression and Decompression:

Compression Techniques:
The LZW_compression, RLE, and huff_encoding functions implement the respective algorithms.
Decompression Techniques:
The LZW_decompression function handles LZW decompression.
RLD and huff_decoding are placeholders for implementing decompression for RLE and Huffman encoding.
Starting Process:

The starting() function orchestrates the workflow:
Reads the input text file.
Executes the selected compression or decompression algorithm based on user input.
Outputs results to a file (compressed_output.txt or xtracted_file.txt).
## 2.2 Graphical User Interface (GUI)
Design:
Built using Tkinter.
Features include:
File selection entry (pth_Entry) and button.
Dropdown menu (tech_combo) for selecting compression technique.
Radio buttons (comp_rd_btn, deco_rd_btn) for choosing between compression and decompression.
A "Start" button to initiate the process.
User Workflow:
Users select a text file and desired technique.
Choose whether to compress or decompress.
The tool processes the file and provides feedback via zenity dialogs.
# 3. Code Design Analysis
## 3.1 Strengths
Modularity:
Each compression algorithm is encapsulated in its own function, enhancing readability and maintainability.
Algorithm Variety:
Supports multiple algorithms, catering to different types of text data.
GUI Integration:
Provides an intuitive user interface for selecting files and options.
Error Handling:
Handles invalid input (e.g., non-text files) with error dialogs.
LZW decompression includes error handling for invalid compressed data.
## 3.2 Limitations
Incomplete Features:
The RLD (Run-Length Decoding) and huff_decoding functions are placeholders and need implementation.
Dependency on External Tools:
Uses zenity for file dialogs and notifications, which may limit portability on non-Linux systems.
Compression Feedback:
Compression ratio (e.g., size reduction) is calculated but not always displayed to the user.
## 3.3 Optimization Opportunities
Huffman Encoding:
Use a more compact representation for the Huffman tree to improve decoding speed.
Generalized Interface:
Consolidate compression and decompression logic into a single framework for scalability.
GUI Enhancements:
Add progress bars or status indicators for large files.
Provide direct display of compression ratios in the GUI.
# 4. Suggested Improvements
Complete Decompression Algorithms:
Implement RLD and huff_decoding to support full functionality.
Cross-Platform Compatibility:
Replace zenity with a Tkinter-based file dialog and message boxes.
Performance Enhancements:
Optimize dictionary operations in LZW for faster performance on large files.
Robust Error Handling:
Add detailed error messages for unsupported file formats or corrupted compressed data.
Documentation:
Include comprehensive docstrings for each function and an overarching user guide.
# 5. Conclusion
The code demonstrates a well-structured implementation of text compression techniques, showcasing efficient algorithms like LZW, RLE, and Huffman encoding. While the tool is functional for compression, it requires additional development for full decompression capabilities and improved user interaction. With the suggested improvements, this tool can become a robust and versatile solution for text compression tasks.

