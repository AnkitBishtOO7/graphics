import circle 
import line

print("we will draw using bresenhamm's algorithms")
print("1. circle drawing")
print("2. line drawing")

cho=int(input("enter your choice"))
 
 #now for the entered choice by the user

if cho==1:
    print("let's start the process for the printing of circle enter following details")
    print("size of screen is 800*600")
    #circle from circle.py file
    circle.main()


elif cho==2:
    print("let's start printing of a line enter following details")
    print("size of screen is 800*600")
    #line drawing from the line.py file
    line.main()


else:
    print("you entered a wrong choice")
    #there is no other choioce

    
