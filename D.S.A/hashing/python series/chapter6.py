chai_types = "ginger chai"
customer_name = "Priya"

print(f"order for{customer_name}:{chai_types} please !")
chai_description = "aromatic and bold"


print(f"first word:{chai_description[0:8:2]}")# 1 means every character 2. means every 2 character'
print(f"first word:{chai_description[:8]}")
print(f"last word:{chai_description[12:]}")


print(f"last word:{chai_description[::-1]}")

label_text = "chai spècial"
ecoded_label = label_text.encode("utf-8")
print(f"non encoded label: {label_text}")
print(f"encoded label:{ecoded_label}")
decoded_label  = ecoded_label.decode("utf-8")
print(f"decoded label: {decoded_label}")

