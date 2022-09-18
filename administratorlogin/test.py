# Python3 program for the above approach
 
# Function to calculate time
# taken to type the given word
def timeTakenToType(keyboardLayout, word):
     
    # Stores position of characters
    pos = [0]*(26)
 
    # Iterate over the range [0, 26]
    for i in range(26):
       
      # Set position of each character
        ch = keyboardLayout[i]
        pos[ord(ch) - ord('a')] = i
 
    # Store the last index
    last = 0
 
    # Stores the total time taken
    result = 0
 
    # Iterate over the characters of word
    for i in range(len(word)):
        ch = word[i]
 
        # Stores index of the next character
        destination = pos[ord(ch) - ord('a')]
 
        # Stores the distance of current
        # character from the next character
        distance = abs(destination - last)
 
        # Update the result
        result += distance
 
        # Update last position
        last = destination
 
    # Print result
    print (result)
 
# Driver Code
if __name__ == '__main__':
   
    # Given keyboard layout
    keyboardLayout = "acdbefghijlkmnopqrtsuwvxyz"
 
    # Given word
    word = "dog"
 
    # Function call to find the minimum
    # time required to type the word
    timeTakenToType(keyboardLayout, word)
 
    # This code is contributed by mohit kumar 29.