# MorseCodeConverter
A program where it either converts:
- Text --> Morse code
  OR
  -Morse code --> Text
  
  To be clear:
  For Text, we mean all letters, numbers, and these symbols: !@$?=+&()-;:',.-/_
  
  For morse code, only dots (.) and dashes (-) are allowed.

__HOW PROGRAM TELLS WHETHER INPUT IS TEXT OR MORSE CODE__
The way the program distinguishes between the two (text and morse code) by regular expression.
If the program detects any numbers, letter, or any of the characters specified above EXCEPT the dot (.) and dash (-), then the program knows that the input is text and it needs to convert it to morse code. The reason we make an exception for the dot and dash is because morse code is made up of dots and dashes. Therefore, if the input is made up of dots and dashes, it assumes that it is morse code that needs to be converted to text.
  
__HOW TO RUN PROGRAM__  
To run the program, all you would have to do is have Python already installed and set up the environment variables and such. You can run this in either your favorite python IDE or in terminal/Command Prompt. For terminal/command prompt, simply type "python morsecode.py" to run the program.
  
Once the program runs, you can enter your message that you wish to convert. You may enter either text or morse code. As it stands, it will only convert one message per run.
