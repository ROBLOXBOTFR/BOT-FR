import re

# Read the file
with open("cogs/ticket_commands.py", "r") as f:
    content = f.read()

# Find the admin commands section and update it
admin_commands_pattern = r'(name="Admin Commands",\s+value=\(\s+"\/setup.+?"\s+"\/setarchivechannel <channel>.+?"\s+\),)'
replacement = r'\1\n                        '
replacement += r'"\/setpanel <category> <question>" - Set a question for a ticket category\n                    '

content = re.sub(admin_commands_pattern, replacement, content, flags=re.DOTALL)

# Write the file back
with open("cogs/ticket_commands.py", "w") as f:
    f.write(content)

print("Updated help command successfully!")