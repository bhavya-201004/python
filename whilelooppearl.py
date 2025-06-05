thermo =("zeroth","first","second","third","entropy","enthalpy","gibbs free enrgy","helmhotz free energy","maxwell's energy")
x="entropy"
i=0
while i <= len(thermo)-1:
    if(thermo[i] == x):
        print("Found at position:",i+1)
        break
    else:
        print("finding....")
    i += 1
