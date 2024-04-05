from pytest import CaptureFixture


class Meta(type):
    def __init__(cls, name, bases=None, namespace=None):  # type: ignore
        super().__init__(name, bases, namespace)
        print(f"Creating new class: {cls}")

    def __call__(cls):  # type: ignore
        new_instance = super().__call__()
        print(f"Class {cls} new instance: {new_instance}")
        return new_instance


class MyType(metaclass=Meta):
    pass


def test_MyType__init(capsys: CaptureFixture[str]) -> None:
    # Act
    MyType()

    # Assert
    capture = capsys.readouterr()
    assert capture.out.startswith(
        "Class <class 'test_metaclasses.test_mytype.MyType'> "
        "new instance: <test_metaclasses.test_mytype.MyType object at"
    )
    assert not capture.err
