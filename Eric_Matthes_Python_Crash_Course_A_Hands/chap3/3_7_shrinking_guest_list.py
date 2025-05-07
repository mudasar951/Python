guest_list = ['Ali', 'Hammad', "Mohsin"]

not_comming = 'Hammad'

guest_list.remove(not_comming)
guest_list.insert(1,'Hannan')
guest_list.insert(0,"Imad")
guest_list.insert(3,"Haris")
guest_list.append("Munawer")

print("The bigger table is not available anymore. Know i have space for two persons only")

guest_1 = guest_list.pop()
guest_2 = guest_list.pop()
guest_3 = guest_list.pop()
guest_4 = guest_list.pop()

print(f"Sorry {guest_1}, you are not comming to dinner as I don't have enough space")
print(f"Sorry {guest_2}, you are not comming to dinner as I don't have enough space")
print(f"Sorry {guest_3}, you are not comming to dinner as I don't have enough space")
print(f"Sorry {guest_4}, you are not comming to dinner as I don't have enough space")


invitation_1 = f"Hi {guest_list[0].title()}, You are still invited to dinner. So you have to come"
invitation_2 = f"Hi {guest_list[1].title()}, You are still invited to dinner. So you have to come"

print(invitation_1)
print(invitation_2)

del guest_list[1]
del guest_list[0]

print(guest_list)

