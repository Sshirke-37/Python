#Regex
import re

def valid_name():
    name = input("Enter your name: ")
    name = ' '.join(name.strip().split())
    pattern = (r'^[A-Za-z ]{2,}$')
    if re.fullmatch(pattern, name):
        print("Valid name.")
    else:
        print("Invalid name. Use only letters and spaces, no digits or symbols.")

def valid_aadhar():
    aadhar = input("Enter your Aadhaar number: ")
    aadhar = aadhar.replace(" ", "")
    pattern = (r'^[2-9]\d{11}$')
    if re.match(pattern, aadhar):
        print("Valid Aadhar number.")
    else:
        print("Invalid Aadhar number. It must be a 12-digit number starting with 2–9.")

def valid_pan():
    pan = input("Enter your PAN number: ")
    pan = pan.replace(" ", "").upper()
    pattern = (r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$')
    if re.match(pattern, pan):
        print("Valid PAN number.")
    else:
        print("Invalid PAN number. It should be: 5 letters, 4 digits, 1 letter.")

def valid_mobile():
    mobile = input("Enter your mobile number: ")
    pattern =  (r'^[7-9][0-9]{9}$')
    if re.match(pattern,mobile):
        print("It is a valid mobile number !")
    else:
        print("It is a invalid mobile number. It should start from 7 onwards.")

def valid_gst():
    gst = input("Enter your GSTNum: ")
    gst = gst.replace(" ", "").upper()
    pattern = (r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$')
    if re.match(pattern, gst):
        print("Valid gst.")
    else:
        print("Invalid gst. Format should be: 2 digits + PAN + entity code + Z + checksum (e.g., 27ABCDE1234F1Z5).")
