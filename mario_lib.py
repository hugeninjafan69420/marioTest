my_dir=os.path.dirname(os.path.realpath(__file__))
def read_and_combine(bodies_file, char_file):
    """
    read from the bodies file and the char file
    (CSV) and then iterate thru both of them (nested)
    and to print out all the combinations
    """

    read_csv= csv.reader(bodies_file)

    read_csv2=csv.reader(char_file)
    for row in read_csv:
        body=str(row[0])
        for row in read_csv2:
            character=str(row[0])
            print(body, character)

    pass


def best_speed(bodies_file, char_file):
    """
    read from bodies and char files
    iterate thru them all and get the speed
    sum the speed for the character and the body
    print out the character/body combo that has the highest
    speed.  And print out the highest (total) speed.
    """
    pass

def best_acceleration(bodies_file, char_file):
    """
    """
    pass


# TODO refactor and consider if there's a better way than passing in the
# filename each time
