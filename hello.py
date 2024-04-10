def display_menu():
  print("Menu\n
        "-------------\n
        "1. Encode\n
        "2. Decode\n
        "3. Quit\n")
def main():
  while True:
    display_menu()
    menu_option = int(input("Please enter an option: "))
    if menu_option == 1:
      de_pass = int(input("Please enter your password to encode: "))
      de_pass_str = str(de_pass)
      de_pass_arr = []
      for i in range(len(de_pass_str)):
          en_pass_num = int(de_pass_str[i]) + 3
          de_pass_arr.append(str(en_pass_num))
      en_pass_str = ''.join(de_pass_arr)
      en_pass = int(en_pass_str)
      print("Your password has been encoded and stored!")
    if menu_option == 2:
    
     
      password_arr = []
      for i in range(len(en_pass_str)):
          encoded = int(en_pass_str[i]) -3
          password_arr.append(str(encoded))
      decoded_str = "".join(password_arr)
      print("The encoded password is"+ en_pass +",and the original password is"+ decoded_str)

    if menu_option == 3:
      break

if __name__ == __"main"__:
  main()
