
import weaponClass as w
import csv


'''
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''


# create a file object to open the file in read mode
infile= open('weapons.csv','r')



# create a csv object from the file object

text = csv.reader(infile, delimiter= ',')

#skip the header row

next(infile)


#create an empty dictionary named 'weapons_dict'

weapons_dict = {}


#use a for loop to iterate through every row of the csv file
for record in text:


    #use variables for name,speed and range (optional)
    name = record[0]
    s = record[1]
    r = record[2]    

    # create an instance of the weapon object using the 
    # specs from the csv file (name,speed and range) 
    gun = w.Weapon(name, s, r)

    # append the name and bullet count to 'weapons_dict'
    gun.set_bullets()
    weapons_dict[name]= gun.get_bullets()

    # print out the name of the weapon using the appropriate method of the object 
    gun.set_name(name)
    print("The name of the gun is ", gun.get_name())
    # print out the speed of the weapon using the appropriate method of the object
    gun.set_speed(s)
    print("The speed of the gun is ", gun.get_speed())
    # print out the range of the weapon using the appropriate method of the object
    gun.set_range(r)
    print("The range of the gun is ", gun.get_range())
    # print out the number of bullets of the weapon using the appropriate method of the object
    #gun.set_bullets()
    print("The number of bullets is ", gun.get_bullets())

    #use an input statement to halt the program and wait for the user - 
    input("Press any key to fire the weapon")
    

    # use an appropriate loop to keep firing the weapon until all bullets run out

    for i in range(0,gun.get_bullets()):
        gun.set_status()
        if gun.get_status() == 'Active':


        # call the appropriate method to fire a bullet
                gun.fire_bullet()

       
        # print out the bullet count every time the weapon is 
                print("Bullet Count: ", gun.get_bullets())
        #fired


    


#using a loop print out the name and number of bullets from the dictionary


for key,value in weapons_dict.items():
    print('Name:',key)
    print("Number of Bullets:",value) 
    print('\n')


