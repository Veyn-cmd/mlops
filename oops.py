



import email


class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to Chatbook! Please select an option: 
        1. press 1 to signup
        2. press 2 to signin
        3. press 3 to write a post
        4. press 4 to message a friend
                           
        5. press 5 to exit
 """)



        if user_input == '1':
            self.signup()

        elif user_input == '2':
            self.signin()

        elif user_input == '3':
            self.my_posts()

        elif user_input == '4':
            self.sendmsg()
 
        else:
            exit()


    def signup(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.username = email
        self.password = password
        print("Signup successful!")
        print("\n")
        self.menu()
    

    def signin(self):
        if self.username == '' and self.password == '':
            print("No user found. Please signup first.")
            self.menu()
        else:
            uname = input("Enter your email: ")
            pwd = input("Enter your password: ")
            
            if uname == self.username  and pwd == self.password:
                self.loggedin = True
                print("Signin successful!")
                
            else:
                print("Invalid credentials. Please try again.")
                print("\n")
        self.menu()

    def my_posts(self):
        if self.loggedin == True:
            txt = input("Write your post: ")
            print('your post is: ', txt)

        else:
            print("You need to signin first to write a post.")
            

        self.menu()


    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Write your message: ")
            frnd = input("Enter your friend's email: ")
            print('your message is: ', txt, 'to', frnd)
        else:
            print("You need to signin first to send a message.")
        
        self.menu()




obj = chatbook()