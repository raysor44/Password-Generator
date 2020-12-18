# Password Generator
Simple password generator created in python, password generator doesn't have any characters amount limit.
Password is generated using letters, numbers and special characters in random positions.

# Required Modules
Password Generator requires some not default installed modules to work, you can install those modules with these commands.
``` python
pip install termcolor
pip install colorama
```

# Arguments
|Short Argument|Full Argument            |Description                                  |
|--------------|-------------------------|---------------------------------------------|
|-h            |--help                   |Shows help message                           |
|-n            |--exclude_numbers        |Excludes Numbers from Password               |
|**-ll**       |**--exclude_lletters**   |Excludes **Lowercase** Letters from Password |
|**-ul**       |**--exclude_uletters**   |Excludes **Uppercase** Letters from Password |
|-sc           |--exclude_scharacters    |Excludes Special Characters from Password    |

# How to run and use
1. Run: 'python PasswordGenerator.py' in terminal
2. Password Generator will now ask you to type length of your password, you can use any value you want.
3. Your password will be displayed alongside with letters, numbers and special characters used in generating password.
