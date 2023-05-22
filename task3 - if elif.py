# Task 4 - Read in individual triathlon times. Display total time. Display award received based on specified criteria.
swimming_time = int(input("What is your swimming time in minutes?"))
cycling_time = int(input("What is your cycling time in minutes?"))
running_time = int(input("What is your running time in minutes?"))

total_time = swimming_time + cycling_time + running_time

print(f"Your total time is {total_time} minutes.")

if total_time <= 100:
    print("Congratulations! Your have been awarded Provincial Colours.")
elif total_time <= 105:
    print("Congratulations! Your have been awarded Provincial Half Colours.")
elif total_time <= 110:
    print("Congratulations! Your have been awarded Provincial Scroll.")
else:
    print("Well done for taking part in the triathlon!")