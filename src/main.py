# This command instructs the search tool to crawl the web-
# site, build the index, and save the resulting index into the file system.
# For simplicity, you can save the entire index to a single file.
def build():
    print("Building index...")

# This command loads the index from the file system. Ob-
# viously, this command will only work if the index has been created
# previously with the ’build’ command.
def load():
    print("Loading index...")

# This command prints the inverted index for a particular
# word. The following example will print the inverted index for the word
# ’nonsense’.
def printIndex(word):
    print("Finding '" + word + "' in index...")

# This command is used to find a given query phrase in the
# inverted index and returns a list of all pages that contain it. The first
# example will return a list of all pages containing the word ’indifference’.
# The second example will return all pages containing the words ’good’
# and ’friends’.
def find(phrase):
    print("Finding pages containing '" + phrase + "' in index...")


# Main function
while True:

    # Parse User Input
    content = ""
    userInput = input()
    command = userInput.split(' ', 1)[0]
    try:
        content = userInput.split(' ', 1)[1]
    except:
        pass

    # Process input command
    match command:
        case "build":
            if content != "":
                print("Too many arguments for statement 'build'")
                continue
            build()
        case "load":
            if content != "":
                print("Too many arguments for statement 'load'")
                continue
            load()
        case "print":
            if content == "":
                print("Argument expected: print <arg>")
                continue
            printIndex(content)
        case "find":
            if content == "":
                print("Argument expected: find <arg>")
                continue
            find(content)
        case "exit":
            if content != "":
                print("Too many arguments for statement 'exit'")
                continue
            break
        case _:
            print("Invalid command!")