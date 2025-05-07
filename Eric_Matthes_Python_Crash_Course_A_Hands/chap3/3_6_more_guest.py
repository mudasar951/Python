guest_list = ['Ali', 'Hammad', "Mohsin"]

not_comming = 'Hammad'

guest_list.remove(not_comming)
guest_list.insert(1,'Hannan')
guest_list.insert(0,"Imad")
guest_list.insert(3,"Haris")
guest_list.append("Munawer")

invitation_1 = f"Hi {guest_list[0].title()}, How are you?, Tonight I have a small dinner plan. All friends are comming. You also have to come"
invitation_2 = f"Hi {guest_list[1].title()}, How are you?, Tonight I have a small dinner plan. All friends are comming. You also have to come"
invitation_3 = f"Hi {guest_list[2].title()}, How are you?, Tonight I have a small dinner plan. All friends are comming. You also have to come"
invitation_4 = f"Hi {guest_list[3].title()}, How are you?, Tonight I have a small dinner plan. All friends are comming. You also have to come"
invitation_5 = f"Hi {guest_list[4].title()}, How are you?, Tonight I have a small dinner plan. All friends are comming. You also have to come"
invitation_6 = f"Hi {guest_list[5].title()}, How are you?, Tonight I have a small dinner plan. All friends are comming. You also have to come"

print(invitation_1)
print(invitation_2)
print(invitation_3)
print(invitation_4)
print(invitation_5)
print(invitation_6)

print(f"I have found bigger table, so I am also inviting to {guest_list[3].title()}, {guest_list[4].title()} and {guest_list[5].title()}")
