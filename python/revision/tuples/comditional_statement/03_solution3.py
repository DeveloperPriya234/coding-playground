score =115
if score >=101:
    print("invalid score")
exit()
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >=70:
    grade = "c"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade",grade)