while True:
    print "\n\nPlease select the OS from the list \n\t1.Mac\n\t2.Windows\n\t3.Linux \n\t enter \"q\" to quit"
    user_input=raw_input("enter the selection :")
    if user_input=="1":
        print "you are selected Mac"
    elif user_input=="2":
        print "you are selceted Windows"
    elif user_input=="3":
        print "you are selcted Linux"
    elif user_input in ["q","quit"]:
        print "Thank you bye.."
        break
    else:
        print "\nplease select a proper value and please select from the below list "
