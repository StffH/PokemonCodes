#After Gen 5 the Chance to obtain a shiny Pokemon doubled

gen1 = 8191/8192
gen2 = 4095/4096
banner = ("\n------------------------------------")
print("Shiny Pokemon Probability Calculator",banner)
def GenAsk():
        print("Do want to to calcute:\n\n1. Pre Gen 5 1:8192\nor\n2. Post Gen 5 1:4096?")
#try
        cl = int(input(">>>>>"))
        
        if cl == 1:
                x = gen1
        elif cl == 2:
                x = gen2
        else:
                print("Choose 1 or 2!")
                GenAsk()
        print()
        print("Do you want your output as\n\n1. A List\nor\n2. A Single Output?")
#try
        ch = int(input(">>>>>"))
        if ch == 2:
                try:
                        n = int(input("Type the number of Soft Resets: "))
                except:
                        GenAsk()
                Chance = ((1-(x**n))*100)
                print("SRs: ",n," Shinyprobability: ",Chance,"%")
                GenAsk()
        elif ch == 1:
                try:
                        n = int(input("Type the number of SR Cycles: "))
                except:
                        GenAsk()
                i = 1
                while(i<=n):
                        Chance = ((1-(x**i))*100)
                        print("SRs: ",i," Shinyprobability: ",Chance,"%")
                        i+=1
                GenAsk()
        else:
                GenAsk()
                        

                
GenAsk()
