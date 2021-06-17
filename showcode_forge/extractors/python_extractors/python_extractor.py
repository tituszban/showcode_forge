from abc import ABC, abstractmethod

class PythonExtractorABC(ABC):
    def __init__(self, description):
        self._class_name = description["className"]
        self._class_instance_name = self._class_name[0].lower()
        self._method_name = description["methodName"]
        self._parameters = [p["name"] for p in description["parameters"]]

        self._unit_tests = description["unitTests"]
        self._public_unit_tests = [t for t in self._unit_tests if t["isPublic"]]
        self._private_unit_tests = [t for t in self._unit_tests if not t["isPublic"]]

    def write_source(self):
        with open("solution.py", "w") as f:
            f.write(f"class {self._class_name}:\n")
            f.write(f"    def {self._method_name}(self, {', '.join(self._parameters)}):\n")
            f.write(f"        pass\n")
            f.write("\n\n")
            f.write("if __name__ == \"__main__\":\n")
            f.write(f"    {self._class_instance_name} = {self._class_name}()\n")
            f.write(f"    print({self._class_instance_name}.{self._method_name}())\n")
    
    @abstractmethod
    def write_tests(self):
        pass
