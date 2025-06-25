distance = 6

if distance < 3 :
    transport = ("walk")
elif distance <= 15:
    transport = ("bike")
elif distance >15:
    transport = ("car")
print("AI recommends you the transport of:",transport)