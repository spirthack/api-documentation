all

# Use MD041 instead
exclude_rule 'MD002'

# Allow duplicate titles
exclude_rule 'MD024'

# Allow titles to end in question marks
exclude_rule 'MD026'
 
# Allow any list indentation
exclude_rule 'MD007'

# Require ATX-style headers
rule 'MD003', :style => :atx

# Require dashes for unordered lists
rule 'MD004', :style => :dash

# Allow exactly 2 breaking spaces at the end of a line
rule 'MD009', :br_spaces => 2

# Don't enforce line length in code blocks and tables
rule 'MD013', :line_length => 120, :code_blocks => false, :tables => false

# Don't force ordered lists with 1. 1. 1.
rule 'MD029', :style => :ordered
