from IPython.core.magic import Magics, magics_class, cell_magic


class ExceptionExpected(Exception):
    pass


@magics_class
class ExceptionMagics(Magics):

    # Note: This gets made into an instance method on the IPython shell
    @staticmethod
    def custom_handler(self, etype, value, tb, tb_offset=None):
        stb = self.InteractiveTB.structured_traceback(etype, value, tb, tb_offset)
        for line in stb:
            print line
        return stb

    @cell_magic
    def expect_exception(self, line, cell):
        if not line:
            line = "Exception"
        try:
            exception = self.shell.ev(line)
        except (SyntaxError, NameError):
            raise NameError("Could not evaluate name of expected exception")
        if not (isinstance(exception, type) and issubclass(exception, Exception)):
            raise TypeError("Argument to expect_exception must be an Exception")

        old_CustomTB = self.shell.CustomTB
        old_custom_exceptions = self.shell.custom_exceptions
        try:
            self.shell.set_custom_exc((exception,), self.custom_handler)
            result = self.shell.run_cell(cell)
            if not (result.error_in_exec and isinstance(result.error_in_exec, exception)):
                raise ExceptionExpected("This cell did not raise the expected %s." % line)
        finally:
            self.shell.CustomTB = old_CustomTB
            self.shell.custom_exceptions = old_custom_exceptions
