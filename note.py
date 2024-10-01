amount=int(input("enter your amount or money you have right now"))
note_100=amount//100
note_50=(amount%100)//50
note_10=((amount%100)%50)//10
print(note_100)
print(note_50)
print(note_10)