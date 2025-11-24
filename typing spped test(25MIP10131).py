import time 
import random 

# Just a bunch of sentences I came up with for the test. 
# They're kinda generic, I guess.
tests_to_use = [ 
    "Python makes programming fun and simple.", 
    "Artificial intelligence is shaping our future.", 
    "Coding regularly improves problem solving skills.", 
    "Practice typing to increase your speed and accuracy.", 
    "Computer science is a blend of creativity and logic." 
] 

# The main function for the typing game
def speed_typing_game(): 
    # Grab a sentence randomly, simple as that.
    # I should probably add more later...
    my_test_sentence = random.choice(tests_to_use) 
    
    print("\n\n--- Typing Speed Test - Time to Type! ---") 
    print("Okay, type this out exactly:") 
    print("\n*** " + my_test_sentence + " ***") # Added some stars for emphasis
    
    # Wait for the user to be ready. 
    # This is important so they don't start early!
    input("\nGot it? Hit Enter when you're ready to start...\n") 

    # Okay, timer starts NOW
    start_time_val = time.time() 
    
    # Prompt user for their input
    user_typed_text = input("Go! Start typing below:\n") 
    
    # And timer ends! Phew.
    end_time_val = time.time() 

    # Calculate how long they took. Need to subtract.
    how_long_it_took = end_time_val - start_time_val 
    
    # Rounding is just cleaner, right? 
    how_long_it_took = round(how_long_it_took, 2) 

    # Figure out the WPM. It's words divided by time, then multiplied by 60.
    # Using a slightly weird way to count words, but it works.
    words_count = len(my_test_sentence.split())
    
    # The actual WPM formula. It's a bit of a mouthful.
    words_per_minute = (words_count / how_long_it_took) * 60 
    words_per_minute = round(words_per_minute, 2) 

    # --- Accuracy Check ---
    # This part is a little tricky. I need to count how many characters match up.
    
    # Let's count correct chars. Start at zero.
    correct_char_counter = 0  
    
    # The minimum length of the two strings is what we care about for the loop
    # Used 'min' just to be safe and avoid errors if one is shorter.
    limit = min(len(my_test_sentence), len(user_typed_text))
    
    # Looping through the strings index by index
    for i in range(limit):  
        # Check if the character at this spot is the same in both strings
        if my_test_sentence[i] == user_typed_text[i]:
            # Found a correct one! Add one to the tally.
            correct_char_counter = correct_char_counter + 1 
        # Don't need an 'else' block, just move to the next character.
  
    # Now, calculate the percentage. Need to use the original sentence's length as the base.
    # Had to do the multiplication by 100 at the end to make it a percentage.
    accuracy_percentage_float = (correct_char_counter / len(my_test_sentence)) * 100 
    
    # Rounding the percentage to two decimal places, looks professional.
    final_accuracy = round(accuracy_percentage_float, 2) 
  
    # --- Print all the results out ---
    print("\n\n*** Your Typing Test Summary ***") 
    print(f"Time: {how_long_it_took} seconds (That was fast!)") 
    print(f"Your Speed (WPM): {words_per_minute}") 
    print(f"Your Accuracy: {final_accuracy}%") 

# Don't forget to call the function so the whole thing runs!
speed_typing_game()
