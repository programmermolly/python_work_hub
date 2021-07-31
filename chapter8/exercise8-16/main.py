# 导入整个模块
import function
function.display_message()

# 只导入其中的函数
from function import display_message
display_message()

# 给模块起别名
import function as f
f.display_message()

# 导入模块中的所有函数
from function import *
display_message()
