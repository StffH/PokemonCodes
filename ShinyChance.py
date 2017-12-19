#After Gen 5 the Chance to obtain a shiny Pokemon doubled

gen1 = 8191/8192
gen2 = 4095/4096
banner = ("\n------------------------------------")
print("Shiny Pokemon Probability Calculator",banner)
while(True):
        def GenAsk():
                print("Do want to to calcute:\n\n1. Pre Gen 5 1:8192\nor\n2. Post Gen 5 1:4096?")
                cl = int(input(">>>>>"))
                if cl == 1:
                        x = gen1
                        return x
                elif cl == 2:
                        x = gen2
                        return x
                else:
                        print("Choose 1 or 2!")
                        GenAsk()
        def Calc():
                print()
                print("Do you want your output as\n\n1. A List\nor\n2. A Single Output?")
                ch = int(input(">>>>>"))
                #Put Loop here
                if ch == 1:
                        
        GenAsk()
        
        
                
        

#Chance = (1-((x)**n)*100)
#n = Cycles
#replace n with i for list
#Good night
