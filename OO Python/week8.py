""" Write a program that creates a file named answers.txt
 and writes all the answers to the questions in the file.
 The program should then read the file and 
display the contents on the screen. """
# file = open("answers.txt", "x")
with open('answers.txt', 'w') as file:
   l1 = "1. Mutable\n"
   l2 = "2. set_1={}\n"
   l3 = "3. Immutable\n"
   l4 = "4. {'v', 4, 6.9, 'e'}\n"
   l5 = "5.oth Strings and Tuples\n"
   l6 = "6.3\n"
   l7 = "7.[2, -1, 4, 4, 1, 6, 5, 2, 7, 9, 6, 11,10, 7, 12, 1, -2, 3]\n"
   l8 = "8.[1, -3, 0, 6]\n"   
   l9 = "9.['A', 'B', 'C', 'D', 'E', 'F', 'G']\n"   
   l10 = "10.Positive, negative\n"
   l11= "11.[16, 25, 24]\n"
   l12= "12.dlroW olleH\n"
   l13= "13.'i' ‘end’\n"
   l14= "14.print(reduce(lambda x,y: x if x<y else y,[-3,2,9,0]))\n"
   l15= "15.0 1 4\n"
   l16= "16.Pass statement\n"
   l17= "17.23\n"
   l18= "18.list\n"
   l19="19.None pf the above\n"
   l20="20. 63\n"
   l21="21.BlueGreenOrange \n"
   l22="22.AttributeError\n"
   l23="23 .Inheritance\n"
   l24="24.To listen\n"
   l25="25.dic[7][1]\n"
   l26="26.1.2 0.4 6.5\n"
   l27="27.{}\n"
   l28="28.The process of calling the function within itself\n"
   l29= "29 Python \n"
   l30 ="30 False True False True False\n"
   l31 ="31 RecursionError\n"
   l32 ="32.0 0\n"
   l33 ="33.Not a car\n"
   l34 ="34.String “Bananas” is printed once\n"
   l35 = "35.Built-in\n"
   l36 = "36.['modules'] False\n"
   l37= "37.getcwd()\n"
   l38 = "38.16\n"
   l39 = "39.Sam 24\n"
   l40 = "Thank YOU\n"
   l38 = "HAPPY WEEKEND!"
   
   file.writelines([l1, l2, l3, l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34,l35,l36,l37,l38,l39,l40])

file = open('answers.txt', 'r')
count = 0
  
while True:
    count += 1
  
    # Get next line from file
    line = file.readline()
  
    # if line is empty
    # end of file is reached
    if not line:
        break
    print("Line{}: {}".format(count, line.strip()))
  
file.close()
