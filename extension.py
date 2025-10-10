fname=input("enter the file name")
dot_position=fname.rfind('.')
if dot_position!=-1 and dot_position!=0:
    extension=fname[dot_position+1:]
    print("file extension",extension)
else:
    print("no extension found in filename")
