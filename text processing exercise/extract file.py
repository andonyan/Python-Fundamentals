file_path = input()
file = file_path.rsplit('\\', maxsplit=1)[1]
file_extension = file.split('.')[1]
file_name = file.split('.')[0]
print(f'File name: {file_name}')
print(f'File extension: {file_extension}')

