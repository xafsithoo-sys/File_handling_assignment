# creating a file with some content
with open ('test.txt','w')as file:
    file.write('Enjoying PLPL Sessions\n')
    file.write('The modules are amazing!!\n')
    print ('crated test.txt')
#Read the file and modify
with open ('test.txt','r')as file:
    content=file.read()
    print(content)
#modify it to uppercase and save to new file
modified_content=content.upper()
#saving the modified content to a new file#
with open('new_file.txt','w')as file:
 file.write(modified_content)
print('created new_file.txt with uppercase text')

#Ask the user for a file name
filename=input('Enter a filename to read:')
#Error Handling
try:

 file=open('new_file.txt','r')
 content=file.read()
 print(f'modified file saved as "{'new_file.txt'}"')
except FileNotFoundError:
    print('file not found')