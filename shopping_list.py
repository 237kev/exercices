
"""In this project, you’ll create a simple program that organizes a shopping list.

You can start by placing this list in the first line of your Python script:

shopping_list = ["apples", "bananas", "oranges", "milk", "bananas", "bread", "apples"]
Your program should do the following:

Sort the items of the list alphabetically

Remove duplicates

Print out the items neatly in the command line, one item in each line."""


"""How This Project Matters in the Real-World
This beginner example teaches you how to work with lists, remove duplicates, and organize data—essential skills in real-world applications. In real-world scenarios, you might not be cleaning up grocery lists but rather handling CSV or SQL datasets, automating the removal of duplicate customer emails from hundreds of Excel files, sorting file directories, or structuring inventory lists. The ability to process and organize lists efficiently is a valuable skill in many fields, including e-commerce, data analytics, and automation.

Prerequisites
Required Libraries: No libraries are needed.
Required Files: No files are needed for this project.
IDE: You can use any IDE on your computer to code the project.

Danger Zone
We provide two solutions for this problem. Find them both in the button below:"""

shopping_list = ["apples", "bananas", "oranges", "milk", "bananas", "bread", "apples"]
shopping_list_unique = set(shopping_list)
shopping_list_new = (list(shopping_list_unique))
shopping_list_new.sort()
print('Organised Shopping List:')
for item in shopping_list_new:
    print(f"- {item}" )


