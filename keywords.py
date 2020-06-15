import sys
from input import getch

# The list of 60 C++ keywords
# http://www.eng.fsu.edu/~haik/met.dir/hcpp.dir/notes.dir/cppnotes/node29.html
keywords = [ 'Asm', 'auto', 'bool', 'break', 'case',
             'catch', 'char', 'class', 'const_cast', 'continue',
             'default', 'delete', 'do', 'double', 'dynamic_cast',
             'else', 'enum', 'extern', 'false', 'float',
             'for', 'friend', 'goto', 'if', 'inline',
             'int', 'long', 'mutable', 'namespace', 'new',
             'operator', 'private', 'protected', 'public', 'reinterpret_cast',
             'register', 'return', 'short', 'signed', 'sizeof',
             'static', 'static_cast', 'struct', 'switch', 'template',
             'this', 'throw', 'true', 'try', 'typedef',
             'typeid', 'union', 'unsigned', 'unsigned', 'using',
             'virtual', 'void', 'volatile', 'wchar_t', 'while' ]

# Dictionary of states. Each initial state is a key with possible next states as a set of values
# Example for 'bool' and 'break' (simular for other ):
# states = { ''      : ('b')       ,    <-- both words start with 'b', no other letters/numbers/symbols are allowed
#            'b'     : ('bo', 'br'),    <-- allowed options are 'o' and 'r'
#            'bo'    : ('boo')     ,    <-- only 1 allowed option is 'o'
#            'boo'   : ('bool')    ,    <-- only 1 allowed option is 'l'
#            'bool'  : ('')        ,    <-- empty next state means 'bool' is a final state
#            'br'    : ('bre')     ,
#            'bre'   : ('brea')    ,
#            'brea'  : ('break')   ,
#            'break' : ('')         }   <-- empty next state means 'break' is a final state
states = { '': set() }

# Checks if a entered user symbol leads to a correct new state
def is_acceptable_input(word, char):
    if word in states.keys():
        new_word = word + char
        if new_word in states[word]:
            return True
    return False

# checks if a provided word is a final state
def is_keyword(word):
    if word in states.keys() and "" in states[word]:
        return True
    return False

# Updates a current state with a new next state. Evoked from create_states()
def add_state(current_state, next_state):
    if current_state not in states.keys():
        states[current_state] = set()
    states[current_state].add(next_state)

# Goes through the provided list of words and generates states
# as in example for 'bool' and 'break'
def create_states():    
    for word in keywords:
        add_state("", word[0])
        add_state(word, "")
        for i in range(1, len(word)):
            token = word[:i]
            add_state(token, word[:i+1])

def print_menu():
    print "The program allowes you to enter only C++ keywords"
    print "To start a new word hit Enter/Return"
    print "Hit Escape to exit"
    print
    print "C++ keywords are: "

    for row in range(len(keywords) / 5):
        print "{0:11}{1:15}{2:12}{3:13}{4}".format(*keywords[row*5:row*5+5])
        #print "'{0}', '{1}', '{2}', '{3}', '{4}',".format(*keywords[row*5:row*5+5])
    print
    print "Start entering a word:"

# Interact with a user letting him enter only C++ keywords
def start():
    create_states()
    print_menu()

    word = ""
    while True:
        # Gets new symbol from user
        char = getch()
        # Exits on Esc/Escape
        if char == b'\x1B':
            break
        # Restart the cycle on Enter/Return or whitespace
        elif char == b'\x0D' or char == " ":
            word = ""
            print
        else:
            if is_acceptable_input(word, char):
                word += char
                # prints the user entered symbol if it's allowed
                sys.stdout.write(char)

# Executes the whole program
start()