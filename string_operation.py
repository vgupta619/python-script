print("This Programm is written to calculate string")
string="""You can add multiple
line in this section"""
print(f"{string}")
group_string = "python script"
print('\n\n\n\nActual String is: "python script"')
print(f"letter in first index is:{group_string[0]}")
print(f"letter index from 0 to 5: {group_string[0:5]}")
print(f"Negative first index -1 is: {group_string[-1]}")
print(f"Total lenght of the string is: {len(group_string)}")
print(group_string[-8:-7])
print(string.count('i'))
print(string.center(10))
print(string.lstrip('You'))
print(string.rstrip('section'))
print(' > '.join(string))
print(string.zfill(10))
print(string.find('d'))
print(string.index('add'))
