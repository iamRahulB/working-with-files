real_names=[]

with open("./Input/Names/invited_names.txt") as names:
	all_names=names.readlines()
	for stripped in all_names:
		me=stripped.strip()
		real_names.append(me)


with open("./Input/Letters/starting_letter.txt",) as letter:
	content=letter.read()
	print(content)
	for i in real_names:
		
		new_content=content.replace("[name]", i)
		with open(f"./Output/ReadyToSend/letter_for_{i}.txt","w") as completed:
			completed.write(new_content)
	
	
