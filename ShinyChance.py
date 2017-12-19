gen1 = 8191/8192
gen2 = 4095/4096

def ShinyRoll(x = gen1):
	Chance=0
	try:
	    n=int(input("Type the number of SRs: "))
	except:
	    print("You screwed up.")

	Chance=(1-((x)**n))*100
	print("Encounter: ",n,"  Shiny Chance: ",Chance,"%")

def ShinyList():
	Chance=0
	i=1
	try:
	    n=int(input("Type the number of cycles: "))
	except:
	    print("You screwed up.")

	while(i <= n):
	    Chance=(1-((gen1)**i))*100
	    print("Encounter: ",i,"  Shiny Chance: ",Chance,"%")
	    i+=1

def ShinyRollNew():
        Chance=0
        ans = False
        while(ans == False):
                try:
                        n=int(input("Type the number of SRs: "))
                        ans = True
                except:
                        print('Nope.')

        Chance=(1-((gen2)**n))
        print("Encounter: ",n," Shiny Chance: ",Chance,"%")


