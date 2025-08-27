#ecoded and decoded
label_text = "chai spècial"
ecoded_label = label_text.encode("utf-8")
print(f"non encoded label: {label_text}")
print(f"encoded label:{ecoded_label}")
decoded_label  = ecoded_label.decode("utf-8")
print(f"decoded label: {decoded_label}")