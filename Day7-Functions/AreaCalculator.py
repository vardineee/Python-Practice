# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.


def number_of_cans(wall_width,wall_height,can_coverage):
    coverage = round(wall_width*wall_height/can_coverage)

    print(f"You'll need {coverage} cans of paint.")


should_continue =True
while should_continue:
    wall_height = int(input("Enter wall height in meters:\n "))
    wall_width = int(input("Enter wall width in meters:\n "))
    can_coverage = int(input("Square meters 1 can: \n "))

    number_of_cans(wall_width,wall_height,can_coverage)


    result = input("Type 'Yes', if you want calculate again. Otherwise type 'No'. ").lower()
    if result =='no':
        should_continue = False
        print("GoodBye")
