""""
with open("sample.txt",'r') as f:
    content=f.read()
    print(content)
    """
"""
with open("sampletext_1.txt",'w')as f:
     content=f.write("Hi all")
     print(content)
"""
with open("output.txt", 'w') as f:
     content=input("Enter a text to write into the file: ")
     f.write(content+ "\n")
     print("Data successfully added to output.txt")
with open("output.txt", 'a') as fh:
     content_xtra=input("Enter additional text to append: ")
     fh.write(content_xtra+ "\n")
     print("Data successfully appended")
with open("output.txt", "r") as file:
     x=file.read()
     print(f"The final content of output.txt is\n{x} ")
