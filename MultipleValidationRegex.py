import re

def valid_name():
    name = input("Enter your name: ")
    name = ' '.join(name.strip().split())
    pattern = (r'^[A-Za-z ]{2,}$')
    if re.match(pattern, name):
        print(" Valid name.")
        return True
    else:
        print("Invalid name. Use only letters and spaces.")
        return False

def valid_aadhar():
    aadhar = input("Enter your Aadhaar number: ").replace(" ", "")
    pattern = (r'^[2-9]\d{11}$')
    if re.match(pattern, aadhar):
        print(" Valid Aadhaar number.")
        return True
    else:
        print("Invalid Aadhaar number. Must be 12 digits starting with 2–9.")
        return False

def valid_pan():
    pan = input("Enter your PAN number: ").replace(" ", "").upper()
    pattern = (r'^[A-Z]{5}[0-9]{4}[A-Z]$')
    if re.match(pattern, pan):
        print(" Valid PAN number.")
        return True
    else:
        print("Invalid PAN number. Format: 5 letters, 4 digits, 1 letter.")
        return False

def valid_gst():
    gst = input("Enter your GST number: ").replace(" ", "").upper()
    pattern = (r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$')
    if re.match(pattern, gst):
        print(" Valid GST number.")
        return True
    else:
        print("Invalid GST number. Format: 2 digits + PAN + entity code + Z + checksum.")
        return False

def valid_mobile():
    mobile = input("Enter your mobile number: ").replace(" ", "")
    pattern = (r'^[7-9][0-9]{9}$')
    if re.match(pattern, mobile):
        print(" Valid mobile number.")
        return True
    else:
        print("Invalid mobile number. Must start with 7–9 and be 10 digits.")
        return False

if valid_name():
    if valid_aadhar():
        if valid_pan():
            if valid_gst():
                if valid_mobile():
                    print("\n All inputs are valid!")
                else:
                    print("Mobile validation failed.")
            else:
                print("GST validation failed.")
        else:
            print("PAN validation failed.")
    else:
        print("Aadhaar validation failed.")
else:
    print("Name validation failed.")
