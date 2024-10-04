def main():
    slow = input("Input your sentence here: ")
    output = replace(slow)
    print(output)

def replace(text):
  outputtext = text.replace(" ", "...")
  return outputtext


main()
