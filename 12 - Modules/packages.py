#you can import modules from diferent packages or directories
#by using the dot notation:

'''
import pkg.mod1, pkg.mod2
pkg.mod1.foo()

x = pkg.mod2.Bar()
x
'''

'''
>>> from pkg.mod2 import Bar as Qux
>>> x = Qux()
>>> x
<pkg.mod2.Bar object at 0x036DFFD0>
'''

''' import from a subpackage like this:
import pkg.sub_pkg1.mod1
pkg.sub_pkg1.mod1.foo()
'''