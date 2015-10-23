#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 创建一个新模板的程式

import sys

help_text = '''
You need to pass an argument for the new script you want to create, followed by the script name.  You can use
	-python	: Python Script
	-bash	: Bash Script
	-ksh	: Korn Shell Script
	-sql	: SQL Script
'''

python_tmpl = '''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
if "-h" in sys.argv or '--help' in sys.argv:
    print(help_text)
    sys.exit()

if len(sys.argv) < 3:
    print(help_text)
    sys.exit()

if '-python' == sys.argv[1]:
    file_name = sys.argv[2] + ".py"
    with open(file_name, 'w') as _f:
        _f.writelines(python_tmpl)
else:
    print('unknown options')
    sys.exit()