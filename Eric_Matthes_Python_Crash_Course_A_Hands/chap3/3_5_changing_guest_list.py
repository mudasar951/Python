guest_list = ['Ali', 'Hammad', "Mohsin"]

not_comming = 'Hammad'

guest_list.remove(not_comming)
guest_list.insert(1,'Hannan')

invitation_1 = f"Hi {guest_list[0].title()}, How are you?, Tonight I have a small dinner plan. All friends are comming. You also have to come"
invitation_2 = f"Hi {guest_list[1].title()}, How are you?, Tonight I have a small dinner plan. All friends are comming. You also have to come"
invitation_3 = f"Hi {guest_list[2].title()}, How are you?, Tonight I have a small dinner plan. All friends are comming. You also have to come"

print(invitation_1)
print(invitation_2)
print(invitation_3)

print(f"{not_comming} is not comming to dinner")