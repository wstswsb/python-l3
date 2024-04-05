class SimpleType:
    class_var: int = 0

    def __init__(self, self_var: int) -> None:
        self.self_var = self_var


def SimpleType__init__(self, self_var: int) -> None:  # type: ignore
    self.self_var = self_var


SimpleType_type = type(
    "SimpleType_type",
    (object,),
    {
        "class_var": 0,
        "__init__": SimpleType__init__,
        "__annotations__": {"class_var": int},
    },
)


def test_identical() -> None:
    # Arrange
    simple_type = SimpleType(self_var=15)
    simple_type_type = SimpleType_type(self_var=15)

    # Act
    assert simple_type.self_var == simple_type_type.self_var
    assert simple_type.class_var == simple_type_type.class_var
    assert simple_type.__annotations__ == simple_type_type.__annotations__
