import csv

with open("Q3.vcf", "w") as f:
    # Write the vCard header
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:3.0\n")
    
    # Accept contact details from the user
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    
    # Write the contact details to the vCard
    f.write(f"N:{name}\n")
    f.write(f"TEL:{phone}\n")
    f.write(f"EMAIL:{email}\n")
    
    # Write the vCard footer
    f.write("END:VCARD\n")
