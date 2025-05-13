import time


import time

def main_menu():
    print("\n=== VÄLKOMMEN TILL: FLY FRÅN FÄNGELSET ===")
    print("1. Starta spelet")
    print("2. Avsluta\n")
    choice = input("Välj ett alternativ (1 eller 2): ")

    if choice == "1":
        start_game()
    elif choice == "2":
        print("Hejdå!")
    else:
        print("Ogiltigt val, försök igen.")
        main_menu()

def start_game():
    print("\n--- FLY FRÅN FÄNGELSET ---\n")
    print("Du vaknar upp i en mörk cell. Dörren är låst och du hör vakter prata utanför.\n")
    time.sleep(1)
    first_choice()

def first_choice():
    print("Vad vill du göra?")
    print("1. Undersöka cellen")
    
    print("2. Ropa på vakten")
    choice = input("\nVälj ett alternativ (1 eller 2): ")
    
    if choice == "1":
        investigate_cell()
    elif choice == "2":
        call_guard()
    else:
        print("Ogiltigt val, försök igen.")
        first_choice()

def investigate_cell():
    print("\nDu söker igenom cellen och hittar en lös sten i väggen.")
    print("Bakom stenen finns en rostig sked.\n")
    time.sleep(1)
    print("Vad vill du göra?")
    print("1. Använd skeden för att försöka gräva en tunnel.")
    print("2. Försök använda skeden för att dyrka upp låset.")
    choice = input("\nVälj ett alternativ (1 eller 2): ")
    
    if choice == "1":
        dig_tunnel()
    elif choice == "2":
        pick_lock()
    else:
        print("Ogiltigt val, försök igen.")
        investigate_cell()

def call_guard():
    print("\nDu ropar på vakten. En vakt kommer fram och ser irriterad ut.")
    print("Han säger: \"Vad vill du? Håll tyst!\"\n")
    time.sleep(1)
    print("Vad vill du göra?")
    print("1. Be om vatten för att locka in vakten.")
    print("2. Försöka övertyga vakten att släppa ut dig.")
    choice = input("\nVälj ett alternativ (1 eller 2): ")
    
    if choice == "1":
        trick_guard()
    elif choice == "2":
        persuade_guard()
    else:
        print("Ogiltigt val, försök igen.")
        call_guard()

def dig_tunnel():
    print("\nDu börjar gräva med skeden, men det tar för lång tid och en vakt upptäcker dig!")
    print("Du blir fasttagen och satt i isoleringscell. Spelet är över.\n")
    restart_game()

def pick_lock():
    print("\nDu använder skeden för att dyrka upp låset... och det fungerar!")
    print("Du smyger ut ur cellen och ser en lång korridor framför dig.\n")
    time.sleep(1)
    corridor_choice()

def trick_guard():
    print("\nVakten öppnar dörren för att ge dig vatten, men du övermannar honom!")
    print("Du tar hans nycklar och flyr ur cellen!\n")
    time.sleep(1)
    corridor_choice()

def persuade_guard():
    print("\nDu försöker övertala vakten att släppa ut dig, men han skrattar och går därifrån.")
    print("Nu har du gjort honom misstänksam!\n")
    time.sleep(1)
    print("Du måste hitta ett annat sätt att fly.\n")
    first_choice()

def corridor_choice():
    print("\nDu befinner dig i en lång korridor. Det finns två vägar.")
    print("1. Smyga genom köket.")
    print("2. Försöka ta dig ut genom vaktens kontor.")
    choice = input("\nVälj ett alternativ (1 eller 2): ")
    
    if choice == "1":
        kitchen_escape()
    elif choice == "2":
        guard_office_escape()
    else:
        print("Ogiltigt val, försök igen.")
        corridor_choice()

def kitchen_escape():
    print("\nDu smyger in i köket. Det är tomt, men du hör vakter i närheten.")
    print("Du hittar en kökskniv och en kockrock.\n")
    time.sleep(1)
    print("Vad vill du göra?")
    print("1. Ta på dig kockrocken och låtsas vara en arbetare.")
    print("2. Smyga ut bakvägen.")
    choice = input("\nVälj ett alternativ (1 eller 2): ")
    
    if choice == "1":
        disguise_escape()
    elif choice == "2":
        backdoor_escape()
    else:
        print("Ogiltigt val, försök igen.")
        kitchen_escape()

def guard_office_escape():
    print("\nDu smyger in i vaktens kontor och hittar en uniform.")
    print("Det finns också en karta över fängelset.\n")
    time.sleep(1)
    print("Vad vill du göra?")
    print("1. Ta på dig uniformen och försöka gå ut genom huvudingången.")
    print("2. Leta efter en hemlig utgång på kartan.")
    choice = input("\nVälj ett alternativ (1 eller 2): ")
    
    if choice == "1":
        front_gate_escape()
    elif choice == "2":
        secret_exit()
    else:
        print("Ogiltigt val, försök igen.")
        guard_office_escape()

def disguise_escape():
    print("\nDu tar på dig kockrocken och går lugnt ut genom köksdörren.")
    print("Ingen misstänker något! Du är fri!\n")
    victory()

def backdoor_escape():
    print("\nDu smyger ut genom bakdörren, men en vakt ser dig och fångar dig!")
    print("Spelet är över.\n")
    restart_game()

def front_gate_escape():
    print("\nDu går självsäkert ut genom huvudingången i vaktuniformen.")
    print("Ingen ifrågasätter dig. Du är fri!\n")
    victory()

def secret_exit():
    print("\nDu följer kartan och hittar en gammal tunnel under kontoret.")
    print("Du kryper genom tunneln och når friheten!\n")
    victory()

def victory():
    print("\nGRATTIS! Du har rymt från fängelset!\n")
    restart_game()

def restart_game():
    choice = input("Vill du försöka igen? (ja/nej): ")
    if choice.lower() == "ja":
        start_game()
    else:
        print("Tack för att du spelade!")


if __name__ == "__main__":
    main_menu()

