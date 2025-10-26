import os
import time
from colorama import init, Fore, Style

init()

#! PLEASE DONT CHANGE THESE VARIABLES !#
phishingQuestions = 10
malwareQuestions = 10
passwordSecurityQuestions = 10
networkSecurityQuestions = 10
userAnswers = 0
#! END OF VARIABLES !#

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def phishing_section():
    global userAnswers
    clear_screen()
    print("===============================")
    print("   PHISHING ATTACKS SECTION")
    print("===============================\n")

    correct = 0
    user_answers = []
    correct_answers = ['2', '2', '3', '1', '2', '2', '4', '3', '3', '3']
    
    print("Q1: What is phishing?")
    print("1) A type of malware")
    print("2) A method to steal personal information")
    print("3) A way to improve internet speed")
    print("4) A secure login system\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ2: Which of the following is a common sign of a phishing email?")
    print("1) Personalized greeting")
    print("2) Urgent request for personal information")
    print("3) High-quality graphics")
    print("4) Proper grammar and spelling\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ3: What should you do if you receive an email from an unknown sender asking for personal info?")
    print("1) Reply with your information")
    print("2) Click on any links provided")
    print("3) Delete the email or mark it as spam")
    print("4) Forward the email to friends\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '3':
        correct += 1

    print("\nQ4: What is 'spear phishing'?")
    print("1) A phishing attack targeting a specific individual or organization")
    print("2) A phishing attack using fake antivirus software")
    print("3) A phishing attack that spreads through social media")
    print("4) A phishing attack using phone calls\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '1':
        correct += 1

    print("\nQ5: Which platform is most commonly used for phishing attacks?")
    print("1) Social media")
    print("2) Email")
    print("3) SMS/Text messages")
    print("4) Gaming apps\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ6: What is smishing?")
    print("1) Phishing via voice calls")
    print("2) Phishing via SMS")
    print("3) Phishing via social media")
    print("4) Phishing via browser pop-ups\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ7: Why do phishing emails often contain spelling mistakes?")
    print("1) To bypass spam filters")
    print("2) To test user awareness")
    print("3) To appear more authentic")
    print("4) To target less cautious users\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '4':
        correct += 1

    print("\nQ8: What should you check before clicking a link in an email?")
    print("1) The sender's profile picture")
    print("2) The font style")
    print("3) The URL destination")
    print("4) The time the email was sent\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '3':
        correct += 1

    print("\nQ9: Which of these is a safe practice to avoid phishing?")
    print("1) Use the same password everywhere")
    print("2) Click links from unknown senders")
    print("3) Enable two-factor authentication")
    print("4) Share credentials over email\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '3':
        correct += 1

    print("\nQ10: What is the goal of most phishing attacks?")
    print("1) To entertain users")
    print("2) To improve system performance")
    print("3) To steal sensitive data")
    print("4) To promote cybersecurity awareness\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '3':
        correct += 1

    userAnswers += correct
    print(f"\n{Fore.GREEN}You got {correct} out of {phishingQuestions} phishing questions correct.{Style.RESET_ALL}\n")
    print("Go back home or look at the answers? (h/a)\n")
    choice = input("Your choice: ").strip().lower()
    if choice == 'a':
        print("\nAnswers Review:")
        answers_info = [
            ("2", "Phishing tricks users into giving up personal info."),
            ("2", "Urgency is a common tactic in phishing emails."),
            ("3", "Deleting or reporting is the safest action."),
            ("1", "Spear phishing targets specific individuals."),
            ("2", "Email is the most common phishing platform."),
            ("2", "Smishing is phishing via SMS."),
            ("4", "Spelling mistakes filter out cautious users."),
            ("3", "Always check the URL before clicking."),
            ("3", "2FA adds protection against phishing."),
            ("3", "The goal is to steal sensitive data.")
        ]
        
        for i, (ans, reason) in enumerate(answers_info, 1):
            if user_answers[i-1] == ans:
                print(f"{Fore.GREEN}Q{i}) Correct! The answer was {ans}, reason: {reason}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Q{i}) Incorrect. You answered {user_answers[i-1]}. The correct answer was {ans}, reason: {reason}{Style.RESET_ALL}")

        print("\nPress any key to return home...\n")
        home = input()
        if home:
            main()

    elif choice == 'h':
        print("\nReturning to home...\n")
        main()

def malware_section():
    global userAnswers
    clear_screen()
    print("===============================")
    print("        MALWARE SECTION")
    print("===============================\n")

    correct = 0
    user_answers = []
    correct_answers = ['2', '3', '2', '3', '2', '2', '2', '2', '1', '3']

    print("Q1: What is malware?")
    print("1) A security tool")
    print("2) Malicious software")
    print("3) A firewall")
    print("4) A password manager\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ2: Which of these is a type of malware?")
    print("1) VPN")
    print("2) Antivirus")
    print("3) Trojan")
    print("4) Router\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '3':
        correct += 1

    print("\nQ3: What does ransomware do?")
    print("1) Speeds up your PC")
    print("2) Encrypts files and demands payment")
    print("3) Deletes your browser history")
    print("4) Installs updates\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ4: Which malware disguises itself as legitimate software?")
    print("1) Worm")
    print("2) Rootkit")
    print("3) Trojan")
    print("4) Spyware\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '3':
        correct += 1

    print("\nQ5: What is a keylogger?")
    print("1) A tool to log network traffic")
    print("2) A program that records keystrokes")
    print("3) A password manager")
    print("4) A firewall\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ6: Which malware spreads without user interaction?")
    print("1) Trojan")
    print("2) Worm")
    print("3) Spyware")
    print("4) Adware\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ7: What does a rootkit do?")
    print("1) Encrypts your files")
    print("2) Hides malicious processes from detection")
    print("3) Logs your passwords")
    print("4) Blocks pop-ups\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ8: What is spyware designed to do?")
    print("1) Speed up your system")
    print("2) Monitor and steal user data")
    print("3) Protect against viruses")
    print("4) Block ads\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ9: Which malware displays unwanted advertisements?")
    print("1) Adware")
    print("2) Ransomware")
    print("3) Worm")
    print("4) Botnet\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '1':
        correct += 1

    print("\nQ10: What is the best way to prevent malware infections?")
    print("1) Use outdated software")
    print("2) Disable your firewall")
    print("3) Install antivirus and keep software updated")
    print("4) Share passwords with friends\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '3':
        correct += 1

    userAnswers += correct
    print(f"\n{Fore.GREEN}You got {correct} out of {malwareQuestions} malware questions correct.{Style.RESET_ALL}\n")
    print("Go back home or look at the answers? (h/a)\n")
    choice = input("Your choice: ").strip().lower()

    if choice == 'a':
        print("\nAnswers Review:")
        answers_info = [
            ("2", "Malware is malicious software."),
            ("3", "Trojans disguise themselves as legit apps."),
            ("2", "Ransomware encrypts files and demands payment."),
            ("3", "Trojans pretend to be safe software."),
            ("2", "Keyloggers record keystrokes."),
            ("2", "Worms spread without user action."),
            ("2", "Rootkits hide malicious activity."),
            ("2", "Spyware monitors and steals user data."),
            ("1", "Adware shows unwanted ads."),
            ("3", "Antivirus and updates prevent malware.")
        ]
        
        for i, (ans, reason) in enumerate(answers_info, 1):
            if user_answers[i-1] == ans:
                print(f"{Fore.GREEN}Q{i}) Correct! The answer was {ans}, reason: {reason}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Q{i}) Incorrect. You answered {user_answers[i-1]}. The correct answer was {ans}, reason: {reason}{Style.RESET_ALL}")

        print("\nPress any key to return home...\n")
        home = input()
        if home:
            main()

    elif choice == 'h':
        print("\nReturning to home...\n")
        main()

def password_security_section():
    global userAnswers
    clear_screen()
    print("===============================")
    print("  PASSWORD SECURITY SECTION")
    print("===============================\n")

    correct = 0
    user_answers = []
    correct_answers = ['4', '1', '2', '4', '2', '2', '3', '3', '4', '2']

    print("Q1: Which of these is a strong password?")
    print("1) password123\n2) 123456\n3) qwerty\n4) Sh@nzo!2025\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '4':
        correct += 1

    print("\nQ2: What does 2FA stand for?")
    print("1) Two-Factor Authentication\n2) Two-Firewall Access\n3) Fast Access\n4) File Authorization\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '1':
        correct += 1

    print("\nQ3: What is a password manager?")
    print("1) A tool to share passwords\n2) A tool to store and encrypt passwords\n3) A type of malware\n4) A browser extension for ads\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ4: What is the recommended minimum password length?")
    print("1) 4 characters\n2) 6 characters\n3) 8 characters\n4) 12 characters\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '4':
        correct += 1

    print("\nQ5: Which of these is a bad password habit?")
    print("1) Using a password manager\n2) Reusing passwords across sites\n3) Enabling 2FA\n4) Creating unique passwords\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ6: What does a password hash do?")
    print("1) Stores passwords in plain text\n2) Converts passwords into unreadable strings\n3) Sends passwords to the cloud\n4) Encrypts passwords with your email\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ7: What is a passphrase?")
    print("1) A short password\n2) A phrase used to reset passwords\n3) A long, memorable sentence used as a password\n4) A backup code\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '3':
        correct += 1

    print("\nQ8: Which of these passwords is most secure?")
    print("1) iloveyou\n2) 12345678\n3) !Q2w#E4r\n4) admin\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '3':
        correct += 1

    print("\nQ9: What should you do if a site suffers a data breach?")
    print("1) Ignore it\n2) Change your password immediately\n3) Share your password with support\n4) Use the same password elsewhere\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ10: What is the benefit of using a password manager?")
    print("1) It remembers and secures all your passwords\n2) It shares passwords with friends\n3) It disables 2FA\n4) It stores passwords in plain text\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '1':
        correct += 1

    userAnswers += correct
    print(f"\n{Fore.GREEN}You got {correct} out of {passwordSecurityQuestions} password security questions correct.{Style.RESET_ALL}\n")
    print("Go back home or look at the answers? (h/a)\n")
    choice = input("Your choice: ").strip().lower()

    if choice == 'a':
        print("\nAnswers Review:")
        answers_info = [
            ("4", "Strong passwords use symbols, numbers, and case variety."),
            ("1", "2FA adds a second layer of login security."),
            ("2", "Password managers store and encrypt passwords."),
            ("4", "12+ characters is the recommended minimum."),
            ("2", "Reusing passwords is risky."),
            ("2", "Hashing makes passwords unreadable."),
            ("3", "Passphrases are long and memorable."),
            ("3", "Complex passwords are harder to crack."),
            ("2", "Change passwords after a breach."),
            ("1", "Password managers improve security and convenience.")
        ]
        
        for i, (ans, reason) in enumerate(answers_info, 1):
            if user_answers[i-1] == ans:
                print(f"{Fore.GREEN}Q{i}) Correct! The answer was {ans}, reason: {reason}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Q{i}) Incorrect. You answered {user_answers[i-1]}. The correct answer was {ans}, reason: {reason}{Style.RESET_ALL}")
        
        print("\nPress any key to return home...\n")
        home = input()
        if home:
            main()
    elif choice == 'h':
        print("\nReturning to home...\n")
        main()

def network_security_section():
    global userAnswers
    clear_screen()
    print("===============================")
    print("  NETWORK SECURITY SECTION")
    print("===============================\n")

    correct = 0
    user_answers = []
    correct_answers = ['2', '1', '2', '2', '2', '2', '1', '3', '2', '4']

    print("Q1: What does a firewall do?")
    print("1) Stores passwords\n2) Blocks unauthorized access\n3) Speeds up internet\n4) Deletes malware\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ2: What is a VPN used for?")
    print("1) Encrypting internet traffic\n2) Installing updates\n3) Speeding up downloads\n4) Sharing files\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '1':
        correct += 1

    print("\nQ3: What is the safest way to use public Wi-Fi?")
    print("1) Use incognito mode\n2) Use a VPN\n3) Turn off your firewall\n4) Share your hotspot\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ4: What is network sniffing?")
    print("1) A way to clean your router\n2) Monitoring network traffic to steal data\n3) A method of speeding up Wi-Fi\n4) A type of encryption\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ5: What is MAC address filtering?")
    print("1) Blocking websites\n2) Allowing only specific devices to connect\n3) Encrypting passwords\n4) Sharing files securely\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ6: What is the role of a router?")
    print("1) Encrypts your emails\n2) Connects devices to a network\n3) Stores passwords\n4) Blocks malware\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ7: What is WPA3?")
    print("1) A type of malware\n2) A secure Wi-Fi encryption protocol\n3) A browser plugin\n4) A password manager\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ8: What is a DDoS attack?")
    print("1) A virus that deletes files\n2) A method of speeding up networks\n3) Overloading a server with traffic\n4) Encrypting network data\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '3':
        correct += 1

    print("\nQ9: What is port scanning used for?")
    print("1) Encrypting data\n2) Identifying open network ports\n3) Speeding up downloads\n4) Blocking ads\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '2':
        correct += 1

    print("\nQ10: What is the best way to secure a home network?")
    print("1) Use default router settings\n2) Disable encryption\n3) Use strong Wi-Fi passwords and update firmware\n4) Share your network with neighbors\n")
    answer = input("Your answer: ").strip()
    user_answers.append(answer)
    if answer == '3':
        correct += 1

    userAnswers += correct
    print(f"\n{Fore.GREEN}You got {correct} out of {networkSecurityQuestions} network security questions correct.{Style.RESET_ALL}\n")
    print("Go back home or look at the answers? (h/a)\n")
    choice = input("Your choice: ").strip().lower()

    if choice == 'a':
        print("\nAnswers Review:")
        answers_info = [
            ("2", "Firewalls block unauthorized access."),
            ("1", "VPNs encrypt your internet traffic."),
            ("2", "VPNs protect you on public Wi-Fi."),
            ("2", "Sniffing captures network data."),
            ("2", "MAC filtering limits device access."),
            ("2", "Routers connect devices to networks."),
            ("2", "WPA3 is a secure Wi-Fi protocol."),
            ("3", "DDoS attacks flood servers with traffic."),
            ("2", "Port scanning identifies open network ports."),
            ("3", "Strong passwords and updates secure networks.")
        ]
        
        for i, (ans, reason) in enumerate(answers_info, 1):
            if user_answers[i-1] == ans:
                print(f"{Fore.GREEN}Q{i}) Correct! The answer was {ans}, reason: {reason}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Q{i}) Incorrect. You answered {user_answers[i-1]}. The correct answer was {ans}, reason: {reason}{Style.RESET_ALL}")

        print("\nPress any key to return home...\n")
        home = input()
        if home:
            main()

    elif choice == 'h':
        print("\nReturning to home...\n")
        main()

def main():
    clear_screen()
    print("====================================================================")
    print("                 Welcome to the Cyber Security Quiz!")
    print("Test your knowledge about cyber security threats and best practices.")
    print("                Author: Shane Green (Shanzo/ShaneYLad)")
    print("====================================================================\n")
    
    print("\033[32mPress A Key to begin...\033[0m")
    input()

    clear_screen()
    print("Loading...")
    time.sleep(2)
    clear_screen()

    print("What sections would you like to explore?\n")
    print("1. Phishing Attacks")
    print("2. Malware")
    print("3. Password Security")
    print("4. Network Security\n")

    answer = input("Enter 1, 2, 3, or 4: ").strip()

    match answer:
        case '1':
            phishing_section()
        case '2':
            malware_section()
        case '3':
            password_security_section()
        case '4':
            network_security_section()
        case _:
            print("\033[31mInvalid selection. Please restart the quiz.\033[0m")
            main()
            time.sleep(2)

if __name__ == "__main__":

    main()
