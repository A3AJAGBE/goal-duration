"""
An application that calculates the time constraints in achieving a goal
"""

print('Welcome User, You are using this application because you have a long time goal')
print('This application will help you calculate the time needed to achieve that goal\n')

current_age = int(input('Your current age: '))
goal_age = int(input('Hope to achieve the goal by what age: '))

if current_age > 1 and (goal_age > current_age):
    time_to_achieve = goal_age - current_age

    if time_to_achieve > 1:
        months = time_to_achieve * 12
        weeks = time_to_achieve * 52
        days = time_to_achieve * 365

        print(f"You have {days} days, {weeks} weeks, {months} months and {time_to_achieve} "
              f"years to achieve your goal. Good-luck 🤞🏾💪🏽.")
    else:
        print('This application calculates long-term goals.\n'
              'Although, a one year goal will give you 365 days, 52 weeks, and 12 months to achieve it.')
else:
    print('Invalid inputs.')


