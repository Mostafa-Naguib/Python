class ATool:

    @staticmethod
    def string(val):
        if isinstance(val, str):

            if val == " ":
                print("It's an empty string...")

            else:
                word_count = len(val.split())
                print(f"The number of the word is: {word_count}")

        else:
            print("This isn't string")
