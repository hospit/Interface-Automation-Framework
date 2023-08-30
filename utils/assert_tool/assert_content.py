
"""
Assert 断言方式，或者叫 断言类型
"""


def equal(reality_value, expect_value, messages=''):
    """判断实际是否 相等 预期"""
    assert reality_value == expect_value, messages


def inequality(reality_value, expect_value, messages=''):
    """判断实际是否 不相等 预期"""
    assert reality_value != expect_value, messages


def greater(reality_value, expect_value, messages=''):
    """判断实际是否 大于 预期"""
    assert reality_value > expect_value, messages


def less(reality_value, expect_value, messages=''):
    """判断实际是否 小于 预期"""
    assert reality_value < expect_value, messages


def greater_equal(reality_value, expect_value, messages=''):
    """判断实际是否 大于等于 预期"""
    assert reality_value >= expect_value, messages


def less_equal(reality_value, expect_value, messages=''):
    """判断实际是否 小于等于 预期"""
    assert reality_value <= expect_value, messages


def contains(reality_value, expect_value, messages=''):
    """判断期望结果内容 是否包含 在实际结果中"""
    assert isinstance(
        reality_value, (list, tuple, dict, str, bytes)
    )
    assert expect_value in reality_value, messages


# def contained_by(reality_value, expect_value, message=""):
#     """判断实际结果包含在期望结果中"""
#     assert isinstance(
#         expect_value, (list, tuple, dict, str, bytes)
#     ), "expect_value 需要为  list/tuple/dict/str/bytes  类型"
#
#     assert reality_value in expect_value, message















