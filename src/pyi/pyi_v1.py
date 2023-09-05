import no_pyi

# 如果没有实际定义的话会报错
# import only_pyi

# 完整的pyi，不会报错
import full_pyi

import condition_pyi

no_pyi.no_pyi_hello()
# 这里会出现异常，且无法提示
# no_pyi.error_hello()

# only_pyi.only_pyi_hello()

full_pyi.full_pyi_hello()


condition_pyi.all_hold()
condition_pyi.exit_hold()
# 这里会依据条件而不存在
# condition_pyi.no_exit_hold()


