class TestClassDemoInstance:
    value = 0

    def test_one(self, top):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1
