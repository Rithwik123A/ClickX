import pyautogui
import time


print("\n")

print("=======================================You Are Using AutoClicker Version 1.3.4[BUG FIX]=========================================")

print("\n")
UserMODE = str(input("Enter The Mode You Want To Use (TOKEN/INFINITE): ")).upper()

Clicks = 0
click_interval = 0.01


pyautogui.FAILSAFE = True 
if UserMODE == "INFINITE":
     print("You Have Selected INFINITE MODE...")
     print("\n")

     Time = int(input("Enter the Grace Time Before starting: "))
     print(f"AutoClicker Starting In {Time} seconds...")
     time.sleep(Time)
     STATUS = "RUNNING"
     try:
         while True:
             pyautogui.click()
             time.sleep(click_interval)
             Clicks += 1
             print(f"Total Clicks: {Clicks}   ", end="\r", flush=True)

     except pyautogui.FailSafeException:
             print("FAILSAFE ACTIVAED! AutoClicker Stopped.")
             print(f"Total Clicks: {Clicks}")
             STATUS = "FAILSAFE ACTIVATED"

     except KeyboardInterrupt:
             print("AutoClicker Stopped by User.")
             print(f"Total Clicks: {Clicks}")
             STATUS = "INTERRUPTED"

     def SUMMARY_INFINITE():
            print("\n")
            print("=======================================SUMMARY=========================================")
            print("\n")
            print(f"Total Clicks: {Clicks}")

            if pyautogui.FailSafeException:
                 print(f"Status: {STATUS}")

            elif KeyboardInterrupt:
                 print(f"Status: {STATUS}")

            print("\n")
            print("========================================================================================")
            print("\n")

     SUMMARY_INFINITE()


elif UserMODE == "TOKEN":
    print("You Have Selected TOKEN MODE...")
    print("\n")
    
    try:
        tokens =  int(input("Enter The Amount of Tokens To Click: "))
        TOTAL = tokens
        if tokens <= 0:
             print("Invalid Input! Please Enter a Valid Integer for Tokens.")
             exit()

    except ValueError:
        print("Invalid Input! Please Enter a Valid Integer for Tokens.")
        exit()
    print(f"AutoClicker Starting With {tokens} Tokens...")

    Time = int(input("Enter the Grace Time Before starting: "))
    print(f"AutoClicker Starting In {Time} seconds...")
    time.sleep(Time)
    STATUS = "RUNNING"

    try:
      while True and tokens > 0:
          pyautogui.click()
          time.sleep(click_interval)
          tokens -= 1
          print(f"Tokens Remaining: {tokens}   ", end="\r", flush=True)
      if tokens == 0:
          print(f"Tokens Remaining: {tokens}")
          print("--------------------------------AutoClicker Finished Clicking All Tokens----------------------------------------")
          STATUS = "COMPLETED! No Tokens Remaining."

    except pyautogui.FailSafeException:
        print(f"Tokens Remaining: {tokens}")
        print("FAILSAFE ACTIVAED! AutoClicker Stopped.")
        STATUS = "FAILSAFE ACTIVATED"
        

    except KeyboardInterrupt:
        print(f"Tokens Remaining: {tokens}")
        print("AutoClicker Stopped by User.")
        STATUS = "INTERRUPTED"

    def SUMMARY_TOKEN():
         print("\n")
         print("=======================================SUMMARY=========================================")
         print("\n")
         print("Total Tokens: " + str(TOTAL))
         print(f"Total Clicks: {TOTAL - tokens}")
         print(f"Tokens Remaining: {tokens}")

         if pyautogui.FailSafeException:
              print(f"Status: {STATUS}")

         elif KeyboardInterrupt:
                print(f"Status: {STATUS}")

         elif tokens == 0:
                print(f"Status: {STATUS}")

         print("\n")
         print("========================================================================================")
         print("\n")

    SUMMARY_TOKEN()

else:
    print("Invalid Mode Selected. Please Choose Either TOKEN or INFINITE.")