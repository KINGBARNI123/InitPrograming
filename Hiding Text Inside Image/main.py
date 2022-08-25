from stegano import lsb

InputImagePNG = "image.png"
OutputImagePNG = "output.png"
Message = input("Enter your Message: ")
print(Message)
# for hiding text in image
lsb.hide('image.png',message=Message).save('output.png')

# for getting text from Image
print(lsb.reveal(OutputImagePNG))