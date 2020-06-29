# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:26 PM", "2:00", "sunDay"))


# Run unit tests automatically
main(module='test_module', exit=False)
