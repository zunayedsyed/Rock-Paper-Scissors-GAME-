# rules-----
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.
# -------------------
# build the game 
# introduce
n=input("name:")
n2=input("name:")
# chosse
c=input("1st------Rock/Paper/Scissors?=")
v=input("2nd------Rock/Paper/Scissors?=")
# Writing logic
# Paper covers rock.
if c=="rock":
    if v=="paper":
        print(n2,"------WON!!!-------")
if c=="paper":
    if v=="rock":
        print(n,"------WON!!!-------")
# Scissors cut paper.
if c=="scissors":
    if v=="paper":
        print(n,"------WON!!!-------")
if c=="paper":
    if v=="scissors":
        print(n2,"------WON!!!-------")
# Rock smashes scissors.
if c=="rock":
    if v=="scissors":
        print(n,"------WON!!!-------")
if c=="scissors":
    if v=="rock":
        print(n2,"------WON!!!-------")
# Draw
if c==v:
    print("------DRAW-------")
		  