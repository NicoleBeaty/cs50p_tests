filename= input("Enter file name: ")

if  filename.endswith(".gif"):
    print("Image/gif")
elif filename.endswith(".jpg"):
    print("Image/jpg")
elif filename.endswith(".jpeg"):
    print("Image/jpeg")
elif filename.endswith(".png"):
    print("Image/png")
elif filename.endswith(".pdf"):
    print("document/pdf")
elif filename.endswith(".txt"):
    print("application/txt")
elif filename.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
