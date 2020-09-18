Name: Fabiane Yeung
CS351 – Assignment 4
Instructor: Ben McCamish


How to run the program:

To run the file type "python3 compression.py" I did attached also the files generated from the program just in case. If you erase the files and only run the code all the other files should be generated except the animals.txt

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Write up:

Files included:
	animals.txt (given)

	sorted_Animals.txt (sorted from animals.txt)

	sorted_Animals_Bits.txt (this is the sorted output in 0's and 1's bitmap)

	unsorted_Animals_Bits.txt (this is the unsorted output in 0's and 1's bitmap)

	Ucolumn_unsorted.txt (is where my column function output unsorted)

	Ucolumn_sorted.txt (is where my column function output sorted)

	Ucompressed_unsorted32.txt (output from my 32 bit compression from unsorted file)

	Ucompressed_sorted32.txt (output from 32 bit compression from sorted file)

	Ucompressed_unsorted64.txt (output from my 64 bit compression from unsorted file)

	Ucompressed_sorted64.txt (output from my 64 bit compression from sorted file)

All the files can be generated from the code. I implemented it to erase the files everytime it's ran so its cleaner.

Below is my test:

Unsorted WAH 32 Compression
Number of 0 fills: 1260
Number of 1 fills: 0
Number of literals: 50356

Sorted WAH 32 Compression
Number of 0 fills: 41045
Number of 1 fills: 8795
Number of literals: 1776

Unsorted WAH 64 Compression
Number of 0 fills: 18
Number of 1 fills: 0
Number of literals: 25390

Sorted WAH 64 Compression
Number of 0 fills: 19740
Number of 1 fills: 3870
Number of literals: 1798



	
