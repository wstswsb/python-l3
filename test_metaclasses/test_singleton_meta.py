class SingletonMeta(type):
    def __init__(cls, name, bases, namespace):  # type: ignore
        super().__init__(name, bases, namespace)
        cls.instance = None

    def __call__(cls, *args, **kwargs):  # type: ignore
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)

        return cls.instance


class SingletonBaseMeta(metaclass=SingletonMeta):
    pass


class A(SingletonBaseMeta):
    pass


class B(A):
    pass


def test_singleton() -> None:
    # Act
    a1 = A()
    a2 = A()
    b1 = B()
    b2 = B()

    # Assert
    assert a1 is a2
    assert b1 is b2
    assert a1 is not b1
