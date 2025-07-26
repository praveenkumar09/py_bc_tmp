file_ob = open('demo.txt', mode='w')
file_ob.write('Hello from Python!')
file_ob.close()

file_ob_append = open('demo.txt', mode='a')
file_ob_append.write('\nThis content was appended!')
file_ob_append.close()

file_read_ob = open('demo.txt',mode='r')
file_read_content = file_read_ob.read()
file_read_ob.close()
print(file_read_content)

file_read_lines = open('demo.txt',mode='r')
file_read_lines_content = file_read_lines.readlines()
file_read_lines.close()
print(file_read_lines_content)