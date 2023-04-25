import keyboard

def write(text):
    aliases = ['write',]
    keyboard.write(text.replace('/write ', ''))
    
