colors = input("Enter a list of colors separated by commas: ").split(',')
colors = [color.strip() for color in colors]
if colors:
    print("First color:", colors[0])
    print("Last color:", colors[-1])
else:
    print("No colors were entered.")
