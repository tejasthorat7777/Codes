def hospital():
    is_critical=0
    disease=int(input("Enter the disease or problem the person is suffering from \n 1.Diabetes \n 2.Blood pressure \n 3.Accident"))
    if(disease==1):
        problem=int(input("enter the blood glucose level of patient"))
        if(problem>150):
            print("patient has high blood glucose level")
            new=int(input("enter 1 for critical else not critical"))
            if(new==1):
                print("patient is critical")
                ambulance=int(input("call ambulance from nearby locations \n 1 star hospital \n 2 niramaya hospital \n 3 sasun hospital"))
                if(ambulance==1):
                    print("ambulance from star hospital will reach your location")
                elif(ambulance==2):
                    print("ambulance from nirmaya hospital will reach your location")
                else:
                    print("ambulance from sasun hospital will reach your location")
            else:
                print("patient is not critical")    
        else:
            print("patient is normal")    
    
    elif(disease==2):
        problem=int(input("enter the blood pressure range of patient"))
        if(problem>120):
            print("patient has high blood pressure level")
            new=int(input("enter 1 for critical else not critical"))
            if(new==1):
                print("patient is critical")
                ambulance=int(input("call ambulance from nearby locations \n 1 star hospital \n 2 niramaya hospital \n 3 sasun hospital"))
                if(ambulance==1):
                    print("ambulance from star hospital will reach your location")
                elif(ambulance==2):
                    print("ambulance from nirmaya hospital will reach your location")
                else:
                    print("ambulance from sasun hospital will reach your location")
            else:
                print("patient is not critical")    
        else:
            print("patient is normal")    
    
    else:
            problem=int(input("patient has met with an accident "))
            new=int(input("enter 1 for critical else not critical"))
            if(new==1):
                print("patient is critical")
                ambulance=int(input("call ambulance from nearby locations \n 1 star hospital \n 2 niramaya hospital \n 3 sasun hospital"))
                if(ambulance==1):
                    print("ambulance from star hospital will reach your location")
                elif(ambulance==2):
                    print("ambulance from nirmaya hospital will reach your location")
                else:
                    print("ambulance from sasun hospital will reach your location")
            else:
                print("patient is not critical")    

hospital()          
    

    
