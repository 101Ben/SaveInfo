
import pickle 


def menu(info, user_name_file) :
    print('____MENU____')
    print('1 : look up email addresses')
    print('2 : Add addresses')
    print('3 : Change addresses')
    print('4 : Delete name and addresses')
    print('5 : Change the Password')
    print('6 : Quit')
    print('CHOOSE NUMBER FROM 1 TO 5')

    choice = int(input('\nWhat do you want to do: '))

    while choice != 6 :

        if choice == 1 :
            look_up(info)
        elif choice == 2 :
            add_up(info)
        elif choice == 3 :
            change_name(info)
        elif choice == 4 :
            delete_name(info)
        elif choice  == 5 :
            change_password(user_name_file)
        else :
            print('\n\n__THE FUNCTION YOU CHOSE DOES NOT EXIST__')
            

        print('\n____MENU____')
        print('1 : look up email addresses')
        print('2 : Add addresses')
        print('3 : Change addresses')
        print('4 : Delete name and addresses')
        print('5 : Change the Password')
        print('6 : Quit')
        print('CHOOSE NUMBER FROM 1 TO 5')

        choice = int(input('\nwhat do you want to do now? '))

    print('__YOU HAVE EXITTED__')
        
    
    
    #print(info)

    return info

def add_up (_dict) :
    answer = 'y'
    while answer.lower() == 'y' :
        name = input('Enter a Name: ')
        name = name.capitalize()
        if name not in _dict :
            address = input('Enter the address Email: ')
            _dict[name] = address
        else :
            print('Name already existing')
##            upd_name == 'y'
##            while upd_name.lower() == 'y' :
##                
##            upd_name = input('Do you want to change it (y/n)? ')

        answer = input('Do you want to add another name (y/n): ')

def look_up (_dict) :
    answer = 'y'
    while answer.lower() == 'y' :
        name = input('Enter the name you are searching: ')
        name = name.capitalize()
        if name in _dict :
            print('The email of', name, 'is:', _dict[name])
        else :
            print('__there is no such name store in the memory__')

        answer = input('Do you want to look for another (y/n): ')

def change_name(_dict) :
    answer = 'y'
    while answer.lower() == 'y' :
        name = input('Enter the name whose email you want to change: ')
        name = name.capitalize()
        if name in _dict :
            address = input('Enter the new Email address: ')
            _dict[name] = address
            print('The email of', name, 'has been changed to:', address)
        else :
            print('__there is no such name store in the memory__')

        answer = input('Do you want to look for another (y/n): ')
        
def delete_name(_dict) :
    answer = 'y'
    while answer.lower() == 'y' :
        name = input('Enter the name you want delete: ')
        name = name.capitalize()
        if name in _dict :
            del _dict[name]
            print('The email of', name, 'has been deleted')
        else :
            print('__there is no such name store in the memory__')

        answer = input('Do you want to try with another name (y/n): ')



def change_password(user_name_file) :
    user_file_info_change = open('user_file_info.dat', 'rb')
    old_pass = pickle.load(user_file_info_change)
    old_pass = dict(old_pass)
    user_file_info_change.close()
    ancient = input('Enter the old Password: ')
    n = 0
    print('you have 5 TRIES')
    while old_pass[user_name_file] != ancient and n < 5:
        ancient = input('___Wrong Password___\nTry Again : ')
        n += 1
        if n == 4 :
            print('This is your last try')
    if old_pass[user_name_file] != ancient :
        print ('__SORRY YOU DID NOT PROVIDE THE RIGHT PASSWORD__')
    else :
        new_one = input('Enter your new password: ')
        old_pass[user_name_file] = new_one
        
        user_file_info_save = open('user_file_info.dat', 'wb')
        pickle.dump(old_pass , user_file_info_save)
        user_file_info_save.close()
        print('Your passcode has been updated')
    


        
def main():
##    SETTING THE PASSWORD
##    try : 
##        password_file_show = open('password_file.dat', 'rb')
##        oup = pickle.load(password_file_show)
##        password_file_show.close()
##        password_list = oup
##    except :
##        password_file = open('password_file.dat', 'wb')
##        pickle.dump(['tchamba@101'], password_file)
##        password_file.close()
##        
##        password_file_show = open('password_file.dat', 'rb')
##        oup = pickle.load(password_file_show)
##        password_file_show.close()
##        password_list = oup
##
##    print(password_list)

##    SETTING THE USER INFORMATION

    
    answer = input('have you been using this programme before (yes/no): ')

    if answer.lower() == 'yes' :
        user_file_info_take = open('user_file_info.dat', 'rb')
        nam = pickle.load(user_file_info_take)
        nam = dict(nam)
        user_file_info_take.close()
        #print(nam)
        name_file = input('Enter the name of your file: ')
        
        if not name_file.endswith('.dat')  :
            name_file = name_file + '.dat'

        while str(name_file) not in nam :
            print('__INCORRECT FILE NAME__')
            name_file = input('Enter the name of your file: ')
            if not name_file.endswith('.dat')  :
                name_file = name_file + '.dat'
            
        if str(name_file) in nam :
            pwrd = input('Please enter your password\n')
        if nam[name_file] == pwrd:
##        if pwrd in password_list :   ######
            try:
                in_file = open(name_file, 'rb')
                saved_info = pickle.load(in_file)
                saved_info = dict(saved_info)
                in_file.close()

                the_info = menu(saved_info, name_file)
                
            except FileNotFoundError and EOFError :
                out_file = open(name_file, 'wb')
                pickle.dump('', out_file)
                out_file.close()
                
                in_file = open(name_file, 'rb')
                saved_info = pickle.load(in_file)
                saved_info = dict(saved_info)
                in_file.close()

                the_info = menu(saved_info, name_file)
                
        

            out_file = open(name_file, 'wb')
            pickle.dump(the_info, out_file)
            out_file.close()

        else :
            print('__SORRY, WRONG INFORMATION__ GET OUT ')


    else :
        file_name = input('Enter the name of your external data file: ')
        if not file_name.endswith('.dat')  :
            file_name = file_name + '.dat'
        password = input('create your own Password: ')

        try : 
            user_file_info = open('user_file_info.dat', 'rb')
            bridge = pickle.load(user_file_info)
            bridge = dict(bridge)
            user_file_info.close()
        except :
            user_file_info = open('user_file_info.dat', 'wb')
            pickle.dump({}, user_file_info)
##            bridge = dict(bridge)
            user_file_info.close()
            user_file_info = open('user_file_info.dat', 'wb')
            bridge = pickle.load(user_file_info)
            bridge = dict(bridge)
            user_file_info.close()

            
        bridge[file_name] = password
        user_file_info = open('user_file_info.dat', 'wb')        
        pickle.dump(bridge, user_file_info)
        user_file_info.close()
        
        # create your password
        try :
            infile1 = open(file_name, 'rb')
            saved_info = pickle.load(infile1)
            saved_info = dict(saved_info)
            infile1.close()
            the_info = menu(saved_info, name_file)
            
        except :
            outfile = open(file_name, 'wb')
            pickle.dump('', outfile)
            outfile.close()
            
            infile = open(file_name, 'rb')
            saved_info = pickle.load(infile)
            saved_info = dict(saved_info)
            infile.close()

            the_info = menu(saved_info, file_name)
    

        outfile = open(file_name, 'wb')
        pickle.dump(the_info, outfile)
        outfile.close()

            


main()
