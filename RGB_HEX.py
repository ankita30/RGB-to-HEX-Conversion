"""RGB: red, green, blue. Each stored in 8 bits hence 2^8-1 = 255 so range is from 0 to 255. When converted to binary, 255 is 11111111 hence 8 bits. Total are 24 bits.
Hexadecimal: 0 to 9 then A to F hence total 16 base. hex(int) function is used in python to change int to hex. 255 is 'FF' hence full RGB is 'FFFFFF'. 
Int: range is 0 to 2^32-1 = 4.29 billion. hex of max int is 'FFFFFFFF'. 
RGB to HEX: take binary of red shifted to 16 on left, green shifted to 8 on left and blue covering total 24 bits. then convert that internal 24 bits binary to hex. (No need to convert to binary: outer is all int)
HEX to RGB: 24 binary needs to be divided into 8-8-8 so divide int by 2^8 so modulo int is blue. shifted rest to right by 8 is again divided by 2^8 which is green. Rest is red."""

#Message for any invalid entry!
invalid_msg = "Invalid value entered!"

#Function for converting RGB to HEX:
def rgb_hex():
  #Input red value
  red = int(raw_input("Enter a value for red: "))
  if red < 0 or red > 255:
    print invalid_msg
    return
  
  #Input green value
  green = int(raw_input("Enter a value for green: "))
  if green < 0 or green > 255:
    print invalid_msg
    return
  
  #Input blue value
  blue = int(raw_input("Enter a value for blue: "))
  if blue < 0 or blue > 255:
    print invalid_msg
    return
  
  #Shift RGB to put in 8-8-8 position and using         hex(int) function
  val = (red << 16) + (green << 8) + (blue)
  print val
  print "%s" % (hex(val)[2:]).upper()
  
#HEX to RGB function:
def hex_rgb():
  #Input hex value
  hex_val = raw_input("Enter a hexadecimal value")
  if len(hex_val)!=6:
    print invalid_msg
    return
  else:
    hex_val = int(hex_val,16)
  
  #Dividing hex by 2^8 will give last 8 bits as modulo
  two_hex_digits = 2**8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "%s, %s, %s" % (red, green, blue)
  
#Main function for options
def convert():
  while True: 
    option = raw_input("Enter 1 to convert RGB to HEX, 2 to convert HEX to RGB, X to exit: ")
    if option == '1':
      print "RGB to Hex..."
      rgb_hex()
    elif option == '2':
      print "Hex to RGB..."
      hex_rgb()
    elif option.upper() == 'X':
      break
    else:
      print "Error"
  
convert()
