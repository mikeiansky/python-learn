"""
标准库json模块
"""

import json
result = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(result)