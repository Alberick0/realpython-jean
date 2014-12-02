from easygui import *

msgbox("Hello", "Message", "hi!")
options = "yes", "no"
var_btn_box = buttonbox("Do you like python?", "Choose!", options)
var_idx_box = indexbox("Index Do you like python?", "Choose!", options)
choices = "list", "tuple", "set", "dictionary"
var_choicebox = choicebox("Choose something", "do it now!", choices)
var_mul_choice_box = multchoicebox("What do you like more?", "Choose!", choices)
var_enterbox = enterbox("Say something about Python", "Type!")
var_pass = passwordbox("What's your password?")

print var_pass, var_enterbox, var_mul_choice_box, var_choicebox, var_idx_box, var_btn_box

