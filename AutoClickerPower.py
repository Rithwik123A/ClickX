
import pyautogui
import time
import argparse
import sys


print("\n")
print("======================================= AutoClicker Version 1.4.0 [CLI CONFIGURATION] =======================================")
print("\n")


# ======================== ARGUMENT CONFIGURATION ========================

parser = argparse.ArgumentParser(
    description="AutoClicker V1.4.0 - Advanced CLI Configuration"
)

parser.add_argument(
    "--mode",
    type=str.upper,
    choices=["TOKEN", "INFINITE"],
    required=True,
    help="Select clicking mode (TOKEN/INFINITE)"
)

parser.add_argument(
    "--tokens",
    type=int,
    default=100,
    help="Number of clicks in TOKEN mode (default: 100)"
)

parser.add_argument(
    "--interval",
    type=float,
    default=0.01,
    help="Time between clicks in seconds (default: 0.01)"
)

parser.add_argument(
    "--grace",
    type=int,
    default=3,
    help="Grace time before clicking starts (default: 3)"
)

parser.add_argument(
    "--button",
    type=str.lower,
    choices=["left", "right", "middle"],
    default="left",
    help="Mouse button to click (default: left)"
)


args = parser.parse_args()


# ======================== VARIABLE ASSIGNMENT ========================

UserMODE = args.mode
tokens = args.tokens
TOTAL = tokens
click_interval = args.interval
Time = args.grace
MouseButton = args.button

Clicks = 0
STATUS = "NOT STARTED"

pyautogui.FAILSAFE = True


# ======================== INPUT VALIDATION ========================

if tokens <= 0:
    parser.error("Token amount must be greater than zero.")

if click_interval <= 0:
    parser.error("Click interval must be greater than zero.")

if Time < 0:
    parser.error("Grace time cannot be negative.")


# ======================== STARTUP ========================

print(f"Mode: {UserMODE}")
print(f"Click Interval: {click_interval}")
print(f"Grace Time: {Time}")
print(f"Mouse Button: {MouseButton.upper()}")

if UserMODE == "TOKEN":
    print(f"Total Tokens: {tokens}")

print("\n")
print(f"AutoClicker Starting In {Time} Seconds...")

try:
    time.sleep(Time)

except KeyboardInterrupt:
    STATUS = "INTERRUPTED BEFORE START"
    print("\nAutoClicker Startup Interrupted.")


# ======================== INFINITE MODE ========================

if UserMODE == "INFINITE" and STATUS != "INTERRUPTED BEFORE START":

    print("\nINFINITE MODE ACTIVATED!")

    STATUS = "RUNNING"

    try:
        while True:

            pyautogui.click(button=MouseButton)

            Clicks += 1

            print(f"Total Clicks: {Clicks}   ", end="\r", flush=True)

            time.sleep(click_interval)

    except pyautogui.FailSafeException:

        STATUS = "FAILSAFE ACTIVATED"
        print("\nFAILSAFE ACTIVATED! AutoClicker Stopped.")

    except KeyboardInterrupt:

        STATUS = "INTERRUPTED"
        print("\nAutoClicker Stopped By User.")

    finally:

        print("\n")
        print("======================================= SUMMARY =======================================")
        print("\n")

        print(f"Total Clicks: {Clicks}")
        print(f"Status: {STATUS}")

        print("\n")
        print("=======================================================================================")


# ======================== TOKEN MODE ========================

elif UserMODE == "TOKEN" and STATUS != "INTERRUPTED BEFORE START":

    print("\nTOKEN MODE ACTIVATED!")

    STATUS = "RUNNING"

    try:
        while tokens > 0:

            pyautogui.click(button=MouseButton)

            tokens -= 1
            Clicks += 1

            print(f"Tokens Remaining: {tokens}   ", end="\r", flush=True)

            time.sleep(click_interval)

        STATUS = "COMPLETED! NO TOKENS REMAINING."

        print("\n")
        print("AUTOCLICKER FINISHED CLICKING ALL TOKENS!")

    except pyautogui.FailSafeException:

        STATUS = "FAILSAFE ACTIVATED"
        print("\nFAILSAFE ACTIVATED! AutoClicker Stopped.")

    except KeyboardInterrupt:

        STATUS = "INTERRUPTED"
        print("\nAutoClicker Stopped By User.")

    finally:

        print("\n")
        print("======================================= SUMMARY =======================================")
        print("\n")

        print(f"Total Tokens: {TOTAL}")
        print(f"Total Clicks: {Clicks}")
        print(f"Tokens Remaining: {tokens}")
        print(f"Status: {STATUS}")

        print("\n")
        print("=======================================================================================")
