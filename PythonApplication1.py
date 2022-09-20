import os
file2 = 'file2'
location = r"C:/Users/Temirlan/Desktop/file"
path = os.path.join(location, file2)
os.mkdir(path)
os.chdir(r"C:/Users/Temirlan/Desktop/file")
os.rename("file2","FILE")
file2 = 'FILE'
path = os.path.join(location, file2)
os.rmdir(path)

