from typing import Any

try:
    import datetime
    import os
    import sys
    import logging
except Exception as e:
    print("Some Modules are Missing {}".format(e))

class Meta(type):
    """Meta Class"""
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        instance = super(Meta, cls).__call__(*args, **kwds)
        return instance

    def __init__(cls, name, base, attr):
        super(Meta, cls).__init__(name, base, attr)

class log(object):
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Wrapper function"""

        start = datetime.datetime.now()  # start time.
        Tem = self.func(*args, **kwds)  # call function
        FunName = self.func.__name__  # get function name
        end = datetime.datetime.now()  # end time

        message = """
        Function: {}
        Execution Time: {}
        Address: {}
        Memory: {}
        Date: {}
        """.format(FunName,
                   end,start,
                   sys.getsizeof(self.func),
                   start)

        cwd = os.getcwd()
        folder = 'Logs'
        new_path = os.path.join(cwd, folder)

        try:
            os.mkdir(new_path)
        except FileExistsError:
            pass  # Directory already exists

        logging.basicConfig(filename='{}/log.log'.format(new_path), level=logging.DEBUG)
        logging.debug(message)

        return Tem

class Test(object):
    def __init__(self) -> None:
        pass

    @log
    def methodA():
        print("Method A")
        return "1111"

if __name__ == "__main__":
    obj = Test()
    obj.methodA()
    print(obj)
