#yailyn and bianca

#ask the use to enter a list of student scores with input

excellent_count = 0
good_count = 0
pass_count = 0
fail_count = 0

    
# Loop to accept scores from the user
while True:
    # Ask the user to enter a score
    score = int(input("Enter student score (enter a negative number to stop): "))
    
    # Break the loop if the user enters a negative number
    if score < 0:
        break
    
    # MAKE IT SAY SOMETHING FOR EACH SCORE 
    if 90 <= score <= 100:
        print("Excellent")
        excellent_count += 1
    elif 70 <= score <= 89:
        print("Good")
        good_count += 1
    elif 50 <= score <= 69:
        print("Pass")
        pass_count += 1
    else:  # score below 50
        print("Fail")
        fail_count += 1

# Print the final count of each category
print("\nFinal counts:")
print("Excellent:", excellent_count)
print("Good:", good_count)
print("Pass:", pass_count)
print("Fail:", fail_count)

##########################question2##################

# Ask the user for a starting and ending number
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

#  special even and special odd numbers  count
special_even_count = 0
special_odd_count = 0

# Loop from the starting number to the ending number
for num in range(start, end + 1):
    # Check if the number is even and greater than 10
    if num % 2 == 0 and num > 10:
        special_even_count += 1
    # Check if the number is odd and less than 20
    elif num % 2 != 0 and num < 20:
        special_odd_count += 1

# Print the counts for special even and special odd numbers
print("\nCounts:")
print("Special Even:", special_even_count)
print("Special Odd:", special_odd_count)
