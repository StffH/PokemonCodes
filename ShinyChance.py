def ShinyRoll():
	Chance=0
	try:
	    n=int(input("Type the number of SRs: "))
	except:
	    print("You screwed up.")

	Chance=(1-((8191/8192)**n))*100
	print("Encounter: ",n,"  Shiny Chance: ",Chance,"%")

def ShinyList():
	Chance=0
	i=1
	try:
	    n=int(input("Type the number of cycles: "))
	except:
	    print("You screwed up.")

	while(i <= n):
	    Chance=(1-((8191/8192)**i))*100
	    print("Encounter: ",i,"  Shiny Chance: ",Chance,"%")
	    i+=1
	print('Test')
