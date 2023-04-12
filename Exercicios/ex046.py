from emoji import emojize
from time import sleep
print('\n\033[1;32mCONTAGEM \033[1;35mREGRESSIVA \033[1;34mPARA \033[1;33mOS \033[1;36mFOGOS \033[1;31mDE \033[1;32mARTIFÍCIO:\033[m\n')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\n')

for e in range(0, 60):
    print(emojize('\033[1;31m:sparkler:\033[m', use_aliases=True) * 100)