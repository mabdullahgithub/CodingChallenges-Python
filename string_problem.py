# The variable sentence stores a string. Write code to determine how many words in sentence start 
# and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.

# Hard-coded answers will receive no credit.

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
sentence = sentence.split(" ")
same_letter_count = 0
for i in sentence:
    if i[0].lower() == i[-1].lower():
        same_letter_count += 1
print(same_letter_count)