import string

def alphabet_position(letter):
#returns the index of the letter given
    low_let=letter.lower()
    let_ind=string.ascii_lowercase.index(low_let)
    #print (let_ind)
    return let_ind


def rotate_character(char,rot):
    new_letter=""
    if char.lower() not in string.ascii_lowercase:
        new_letter=char
        #print (new_letter)
        return new_letter

    else:
        lowerchar=char.lower()

        rotated_index=string.ascii_lowercase.index(lowerchar)+rot
        #print(rotated_index)

 #finds new letter   
        new_letter=new_letter+string.ascii_lowercase[rotated_index%26]

    if char.islower():
        new_letter=new_letter.lower()
    else:
        new_letter=new_letter.upper()
    #print (new_letter)
    return new_letter