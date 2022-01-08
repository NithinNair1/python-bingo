import random
cList=[]
pList=[]

def genCard():
  while len(cList)!=10:
    cElement=random.randint(1,100)
    if cElement not in cList:
      cList.append(cElement)

  while len(pList)!=10:
    pElement=random.randint(1,100)
    if pElement not in pList:
      pList.append(pElement)  

genCard()
print("\nComputer's Card: ",*cList,sep=" ")
print("Your Card: ",*pList,sep=" ")

def compCalls():
  while len(cList)!=0 and len(pList)!=0:
    calledNum=random.randint(1,100)
    if calledNum in cList and calledNum in pList:
      print("––––––––––––––––––––––––––––––––––––––––––––––––")

      print("\n"+str(calledNum)+" was present in both Computer's Bingo as well as yours")
      cList.remove(calledNum)
      pList.remove(calledNum)
      print("Computer's Card: ",*cList,sep=" ")
      print("Your Card: ",*pList,sep=" ")
    elif calledNum in cList and calledNum not in pList:
      print("––––––––––––––––––––––––––––––––––––––––––––––––")

      print(calledNum,"was present in Computer's Bingo")
      cList.remove(calledNum)
      print("Computer's Card: ",*cList,sep=" ")
      print("Your Card: ",*pList,sep=" ")
    elif calledNum in pList and calledNum not in cList:
      print("––––––––––––––––––––––––––––––––––––––––––––––––")
      print(calledNum,"was present in your Bingo")
      pList.remove(calledNum)
      print("Computer's Card: ",*cList,sep=" ")
      print("Your Card: ",*pList,sep=" ")
    else:
      continue
  print("––––––––––––––––––––––––––––––––––––––––––––––––")
  

compCalls()

def winner(cList,pList):
  if len(cList)==0 and len(pList)==0:
    print("DRAWWWW!!!!! A very Rare Case...")
    print("Computer's Card: ",*cList,sep=" ")
    print("Your Card: ",*pList,sep=" ") 
  elif len(cList)==0:
    print("You Lost")
    print("Computer's Card: ",*cList,sep=" ")
    print("Your Card: ",*pList,sep=" ")
  elif len(pList)==0:
    print("Bingoooooo!!!!! you Won")
    print("Your Card: ",*pList,sep=" ")
    print("Computer's Card: ",*cList,sep=" ")

  else:
    print("Error")


winner(cList,pList)