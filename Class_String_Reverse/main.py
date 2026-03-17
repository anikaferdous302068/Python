class StringReverse:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]

string_to_reverse = input("Enter a string to reverse: ")
reverse_instance = StringReverse(string_to_reverse)
print("Reversed string:", reverse_instance.reverse())
