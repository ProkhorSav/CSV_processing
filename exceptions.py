class CsvProcessorError(Exception):
    pass

class ColumnNotFoundError(CsvProcessorError):
    pass

class InvalidOperationError(CsvProcessorError):
    pass