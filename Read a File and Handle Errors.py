with open("sample.txt","r") as f:
    try:
        print("Reading file content: ")
        data=f.read()
        print(data)
    except FileNotFoundError:
        print("The file sample.txt not found.")

