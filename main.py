"""
An application that calculates how long a goal will be achieved using age.
"""
print('\nHow long to achieve that goal?')


def duration_app():

    try:
        current_age = int(input('Your current age: '))
    except ValueError:
        print('Integers Only\n')
        duration_app()

    try:
        goal_age = int(input('Hope to achieve the goal by what age: '))
    except ValueError:
        print('Integers Only\n')
        duration_app()
    else:

        if current_age > 5:
            if goal_age > current_age:
                time_to_achieve = goal_age - current_age

                if time_to_achieve > 1:
                    months = time_to_achieve * 12
                    weeks = time_to_achieve * 52
                    days = time_to_achieve * 365

                    print(f"\nYou have {days} days, {weeks} weeks, {months} months and {time_to_achieve} "
                          f"years to achieve your goal. Good-luck 🤞🏾💪🏽.")
                else:
                    print('\nThis application calculates long-term goals.\n'
                          'Although, a one year goal will give you 365 days, 52 weeks, and 12 months to achieve it.')
            else:
                print('The age you hope to achieve your goal must be greater than your current age.\n')
                duration_app()
        else:
            print('You must be older than 5 years before you can use this application.')


duration_app()

