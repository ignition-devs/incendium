"""Database module."""

__all__ = [
    "DisposableConnection",
    "InParam",
    "OutParam",
    "Param",
    "check",
    "execute_non_query",
    "get_data",
    "get_output_params",
    "get_return_value",
]

from types import TracebackType
from typing import Any, List, Optional, Type, Union

import system.db
from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import Thread

from incendium.types import DictIntStrAny, SProcResult, String


class DisposableConnection(object):
    """Disposable Connection.

    A disposable connection enables a database connection in Ignition
    and disables it once the operation is completed to release
    resources.
    """

    def __init__(self, database, retries=3):
        # type: (String, int) -> None
        """Disposable Connection initializer.

        Args:
            database: The name of the database connection in
                Ignition.
            retries: The number of additional times to retry
                enabling the connection. Optional.
        """
        self.database = database
        self.retries = retries

    def __enter__(self):
        # type: () -> DisposableConnection
        """Enter the runtime context related to this object.

        Raises:
            IOError: If the connection's status reports as Faulted, or
                ir cannot be enabled.
        """
        system.db.setDatasourceEnabled(self.database, True)

        for _ in range(self.retries):
            Thread.sleep(1000)
            if self.status == "Valid":
                break
            if self.status == "Faulted":
                raise IOError(
                    "The database connection {!r} is {}.".format(
                        self.database, self.status
                    )
                )
        else:
            raise IOError(
                "The database connection {!r} could not be enabled.".format(
                    self.database
                )
            )
        return self

    def __exit__(
        self,
        exc_type,  # type: Optional[Type[BaseException]]
        exc_val,  # type: Optional[BaseException]
        exc_tb,  # type: Optional[TracebackType]
    ):
        # type: (...) -> None
        """Exit the runtime context related to this object."""
        system.db.setDatasourceEnabled(self.database, False)

    @property
    def status(self):
        # type: () -> String
        """Get connection status."""
        connection_info = system.db.getConnectionInfo(self.database)
        return connection_info.getValueAt(0, "Status")


class Param(object):
    """Base class used for defining [In|Out]put parameters."""

    def __init__(
        self,
        name_or_index,  # type: Union[int, str]
        type_code,  # type: int
        value=None,  # type: Optional[Any]
    ):
        # type: (...) -> None
        """Param object initializer.

        Args:
            name_or_index: Parameter name or index.
            type_code: Type code constant.
            value: Value of type type_code.
        """
        self._name_or_index = name_or_index
        self._type_code = type_code
        self._value = value

    @property
    def name_or_index(self):
        # type: () -> Union[int, str]
        """Get value of name_or_index."""
        return self._name_or_index

    @property
    def type_code(self):
        # type: () -> int
        """Get value of type_code."""
        return self._type_code

    @property
    def value(self):
        # type: () -> Optional[Any]
        """Get value of value."""
        return self._value


class InParam(Param):
    """Class used for declaring INPUT parameters."""

    def __init__(self, name_or_index, type_code, value):
        # type: (Union[int, str], int, Any) -> None
        """Create an instance of InParam.

        Args:
            name_or_index: Index (int starting at 1, not 0), or
                name (str).
            type_code: Type code constant from `system.db`.
            value: Value of type type_code.
        """
        super(InParam, self).__init__(
            name_or_index=name_or_index, type_code=type_code, value=value
        )


class OutParam(Param):
    """Class used for declaring OUTPUT parameters."""

    def __init__(self, name_or_index, type_code):
        # type: (Union[int, str], int) -> None
        """Create an instance of OutParam.

        Args:
            name_or_index: Index (int starting at 1, not 0), or name
                (str).
            type_code: Type code constant from `system.db`.
        """
        super(OutParam, self).__init__(
            name_or_index=name_or_index, type_code=type_code
        )


def _execute_sp(
    stored_procedure,  # type: String
    database="",  # type: String
    transaction=None,  # type: Optional[String]
    skip_audit=False,  # type: bool
    in_params=None,  # type: Optional[List[InParam]]
    out_params=None,  # type: Optional[List[OutParam]]
    get_out_params=False,  # type: bool
    get_result_set=False,  # type: bool
    get_ret_val=False,  # type: bool
    get_update_count=False,  # type: bool
    return_type_code=system.db.INTEGER,  # type: int
):
    # type: (...) -> SProcResult
    """Execute a stored procedure against the connection.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        transaction: A transaction identifier. If omitted, the call will
            be executed in its own transaction. Optional.
        skip_audit: A flag which, if set to True, will cause the
            procedure call to skip the audit system. Useful for some
            queries that have fields which won't fit into the audit log.
            Optional.
        in_params: A Dictionary containing INPUT parameters. Optional.
        out_params: A Dictionary containing OUTPUT parameters. Optional.
        get_out_params: A flag indicating whether to return OUTPUT
            parameters after execution. Optional.
        get_result_set: A flag indicating whether to return a dataset
            that is the resulting data of the stored procedure, if any.
            Optional.
        get_ret_val: A flag indicating whether to get the return value
            of the stored procedure Call. Optional.
        get_update_count: A flag indicating whether to return the number
            of rows modified by the stored procedure, or -1 if not
            applicable. Optional.
        return_type_code: The return value Type Code. Optional.

    Returns:
        Result dictionary.
    """
    call = system.db.createSProcCall(
        procedureName=stored_procedure,
        database=database,
        tx=transaction,
        skipAudit=skip_audit,
    )

    if in_params is not None:
        for i_param in in_params:
            call.registerInParam(
                i_param.name_or_index, i_param.type_code, i_param.value
            )

    if out_params is not None:
        for o_param in out_params:
            call.registerOutParam(o_param.name_or_index, o_param.type_code)

    if get_ret_val:
        call.registerReturnParam(return_type_code)

    system.db.execSProcCall(call)

    _out_params = {}
    if out_params is not None and get_out_params:
        for o_param in out_params:
            _out_params[o_param.name_or_index] = call.getOutParamValue(
                o_param.name_or_index
            )

    return {
        "output_params": _out_params,
        "result_set": call.getResultSet() if get_result_set else None,
        "return_value": call.getReturnValue() if get_ret_val else None,
        "update_count": call.getUpdateCount() if get_update_count else None,
    }


def check(stored_procedure, database="", params=None):
    # type: (String, String, Optional[List[InParam]]) -> Optional[bool]
    """Execute a stored procedure against the connection.

    This will return a flag set to TRUE or FALSE.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        params: A Dictionary containing all parameters. Optional.

    Returns:
        The flag.
    """
    output = OutParam("flag", system.db.BIT)
    output_params = get_output_params(
        stored_procedure, output=[output], database=database, params=params
    )

    return (
        output_params["flag"] if "flag" in output_params.iterkeys() else None
    )


def execute_non_query(
    stored_procedure,  # type: String
    database="",  # type: String
    transaction=None,  # type: Optional[String]
    params=None,  # type: Optional[List[InParam]]
):
    # type: (...) -> Optional[int]
    """Execute a stored procedure against the connection.

    Used for UPDATE, INSERT, and DELETE statements.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        transaction: A transaction identifier. If omitted, the call will
            be executed in its own transaction. Optional.
        params: A Dictionary containing all parameters. Optional.

    Returns:
        The number of rows modified by the stored procedure, or -1 if
        not applicable.
    """
    result = _execute_sp(
        stored_procedure,
        database=database,
        transaction=transaction,
        in_params=params,
        get_update_count=True,
    )

    return result["update_count"]


def get_data(
    stored_procedure,  # type: String
    database="",  # type: String
    params=None,  # type: Optional[List[InParam]]
):
    # type: (...) -> Optional[BasicDataset]
    """Get data by executing a stored procedure.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        params: A Dictionary containing all parameters. Optional.

    Returns:
        A Dataset that is the resulting data of the stored procedure
        call, if any.
    """
    result = _execute_sp(
        stored_procedure,
        database=database,
        in_params=params,
        get_result_set=True,
    )

    return result["result_set"]


def get_output_params(
    stored_procedure,  # type: String
    output,  # type: List[OutParam]
    database="",  # type: String
    transaction=None,  # type: Optional[String]
    params=None,  # type: Optional[List[InParam]]
):
    # type: (...) -> DictIntStrAny
    """Get the Output parameters from the Stored Procedure.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        output: A Dictionary containing all output parameters.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        transaction: A transaction identifier. If omitted, the call will
            be executed in its own transaction. Optional.
        params: A Dictionary containing all parameters. Optional.

    Returns:
        Result's output_params.
    """
    result = _execute_sp(
        stored_procedure,
        database=database,
        transaction=transaction,
        in_params=params,
        out_params=output,
        get_out_params=True,
    )

    return result["output_params"]


def get_return_value(
    stored_procedure,  # type: String
    return_type_code,  # type: int
    database="",  # type: String
    transaction=None,  # type: Optional[String]
    params=None,  # type: Optional[List[InParam]]
):
    # type: (...) -> Optional[int]
    """Get the Return Value from the Stored Procedure.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        return_type_code: The Type Code of the Return Value.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        transaction: A transaction identifier. If omitted, the call will
            be executed in its own transaction. Optional.
        params: A Dictionary containing all parameters. Optional.

    Returns:
        The return value.
    """
    result = _execute_sp(
        stored_procedure,
        database=database,
        transaction=transaction,
        in_params=params,
        get_ret_val=True,
        return_type_code=return_type_code,
    )

    return result["return_value"]
