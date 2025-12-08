"""Database module."""

__all__ = [
    "DisposableConnection",
    "InParam",
    "OutParam",
    "TransactionManager",
    "check",
    "execute_non_query",
    "get_data",
    "get_output_params",
    "get_return_value",
    "o_execute_non_query",
    "o_get_data",
]

from types import TracebackType
from typing import Any, List, Optional, Tuple, Type, TypedDict, Union

import system.db
import system.util
from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import Thread

from incendium.helper.types import AnyStr, DictIntStringAny

_SProcResult = TypedDict(
    "_SProcResult",
    {
        "output_params": DictIntStringAny,
        "result_set": BasicDataset,
        "return_value": Optional[int],
        "update_count": int,
    },
)


class DisposableConnection(object):
    """Disposable Connection.

    A disposable connection enables a database connection in Ignition
    and disables it once the operation is completed to release
    resources.
    """

    def __init__(self, database, retries=3):
        # type: (AnyStr, int) -> None
        """Disposable Connection initializer.

        Args:
            database: The name of the database connection in Ignition.
            retries: The number of additional times to retry enabling
                the connection. Optional.
        """
        super(DisposableConnection, self).__init__()
        self._database = database
        self._retries = retries
        self._global_conn = "incendium_db_{}".format(database)

    @property
    def database(self):
        # type: () -> AnyStr
        """Get the name of the disposable connection."""
        return self._database

    @property
    def status(self):
        # type: () -> AnyStr
        """Get connection status."""
        connection_info = system.db.getConnectionInfo(self._database)
        return str(connection_info.getValueAt(0, "Status"))

    def __enter__(self):
        # type: () -> DisposableConnection
        """Enter the runtime context related to this object.

        Raises:
            IOError: If the connection's status reports as Faulted, or
                it cannot be enabled.

        Returns:
            DisposableConnection: The current instance.
        """
        system.db.setDatasourceEnabled(self._database, True)

        for _ in range(self._retries):
            Thread.sleep(1000)
            if self.status == "Valid":
                if self._global_conn not in system.util.globals:
                    system.util.globals[self._global_conn] = 0
                system.util.globals[self._global_conn] += 1
                break
            if self.status == "Faulted":
                raise IOError(
                    "The database connection {!r} is {}.".format(
                        self._database, self.status
                    )
                )
        else:
            raise IOError(
                "The database connection {!r} could not be enabled.".format(
                    self._database
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
        system.util.globals[self._global_conn] -= 1
        if system.util.globals[self._global_conn] == 0:
            system.db.setDatasourceEnabled(self._database, False)


class InParam(object):
    """Class used for declaring INPUT parameters."""

    def __init__(self, name_or_index, type_code, value):
        # type: (Union[int, AnyStr], int, Any) -> None
        """Create an instance of InParam.

        Args:
            name_or_index: Index (int starting at 1, not 0), or name
                (str).
            type_code: Type code constant from `system.db`.
            value: Value of type type_code.
        """
        super(InParam, self).__init__()
        self._name_or_index = name_or_index
        self._type_code = type_code
        self._value = value

    @property
    def name_or_index(self):
        # type: () -> Union[int, AnyStr]
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

    def __repr__(self):  # type: ignore[no-untyped-def]
        """Compute the "official" string representation."""
        return "InParam(name_or_index={!r}, type_code={}, value={})".format(
            self.name_or_index,
            self.type_code,
            self.value,
        )

    def __str__(self):  # type: ignore[no-untyped-def]
        """Compute the "informal" string representation."""
        return "{!r}, {}, {}".format(self.name_or_index, self.type_code, self.value)


class OutParam(object):
    """Class used for declaring OUTPUT parameters."""

    def __init__(self, name_or_index, type_code):
        # type: (Union[int, AnyStr], int) -> None
        """Create an instance of OutParam.

        Args:
            name_or_index: Index (int starting at 1, not 0), or name
                (str).
            type_code: Type code constant from `system.db`.
        """
        super(OutParam, self).__init__()
        self._name_or_index = name_or_index
        self._type_code = type_code

    @property
    def name_or_index(self):
        # type: () -> Union[int, AnyStr]
        """Get value of name_or_index."""
        return self._name_or_index

    @property
    def type_code(self):
        # type: () -> int
        """Get value of type_code."""
        return self._type_code

    def __repr__(self):  # type: ignore[no-untyped-def]
        """Compute the "official" string representation."""
        return "OutParam(name_or_index={!r}, type_code={})".format(
            self.name_or_index,
            self.type_code,
        )

    def __str__(self):  # type: ignore[no-untyped-def]
        """Compute the "informal" string representation."""
        return "{!r}, {}".format(self.name_or_index, self.type_code)


class TransactionManager(object):
    """Database transaction context manager."""

    def __init__(
        self,
        database="",  # type: Union[str, unicode]
        isolation_level=None,  # type: Optional[int]
        timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        """Transaction Manager initializer.

        Args:
            database: The name of the database connection to use. If not
                specified, the project's default database is used.
                Optional.
            isolation_level: The isolation level for the transaction. If
                not specified, the default isolation level is used.
                Optional.
            timeout: The timeout for the transaction in seconds. If not
                specified, the default timeout is used. Optional.
        """
        self._database = database
        self._isolation_level = isolation_level
        self._timeout = timeout
        self.transaction_id = ""  # type: AnyStr

    def __enter__(self):
        # type: () -> TransactionManager
        """Enter the runtime context related to this object."""
        self.transaction_id = system.db.beginTransaction(
            database=self._database,
            isolationLevel=self._isolation_level,
            timeout=self._timeout,
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
        if exc_type is None:
            system.db.commitTransaction(self.transaction_id)
        else:
            system.db.rollbackTransaction(self.transaction_id)

        system.db.closeTransaction(self.transaction_id)


def _execute_sp(
    stored_procedure,  # type: AnyStr
    database="",  # type: AnyStr
    transaction_id=None,  # type: Optional[AnyStr]
    skip_audit=False,  # type: bool
    in_params=None,  # type: Optional[List[InParam]]
    out_params=None,  # type: Optional[List[OutParam]]
    get_out_params=False,  # type: bool
    get_result_set=False,  # type: bool
    get_ret_val=False,  # type: bool
    get_update_count=False,  # type: bool
    return_type_code=system.db.INTEGER,  # type: int
):
    # type: (...) -> _SProcResult
    """Execute a stored procedure against the connection.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        transaction_id: A transaction identifier. If omitted, the call
            will be executed in its own transaction. Optional.
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
        tx=transaction_id,
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
        "result_set": call.getResultSet() if get_result_set else BasicDataset(),
        "return_value": call.getReturnValue() if get_ret_val else None,
        "update_count": call.getUpdateCount() if get_update_count else -1,
    }


def check(
    stored_procedure,  # type: AnyStr
    database="",  # type: AnyStr
    transaction_id=None,  # type: Optional[AnyStr]
    params=None,  # type: Optional[List[InParam]]
):
    # type: (...) -> Optional[bool]
    """Execute a stored procedure against the connection.

    This will return a flag set to TRUE or FALSE.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        transaction_id: A transaction identifier. If omitted, the call
            will be executed in its own transaction. Optional.
        params: A Dictionary containing all INPUT parameters. Optional.

    Returns:
        The flag.
    """
    result = _execute_sp(
        stored_procedure,
        database=database,
        transaction_id=transaction_id,
        in_params=params,
        out_params=[OutParam("flag", system.db.BIT)],
        get_out_params=True,
    )

    return (
        result["output_params"]["flag"]
        if "flag" in result["output_params"].iterkeys()
        else None
    )


def execute_non_query(
    stored_procedure,  # type: AnyStr
    database="",  # type: AnyStr
    transaction_id=None,  # type: Optional[AnyStr]
    params=None,  # type: Optional[List[InParam]]
):
    # type: (...) -> int
    """Execute a stored procedure against the connection.

    Used for UPDATE, INSERT, and DELETE statements.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        transaction_id: A transaction identifier. If omitted, the call
            will be executed in its own transaction. Optional.
        params: A list containing all INPUT parameters as InParam
            objects. Optional.

    Returns:
        The number of rows modified by the stored procedure, or -1 if
        not applicable.
    """
    result = _execute_sp(
        stored_procedure,
        database=database,
        transaction_id=transaction_id,
        in_params=params,
        get_update_count=True,
    )

    return result["update_count"]


def get_data(
    stored_procedure,  # type: AnyStr
    database="",  # type: AnyStr
    transaction_id=None,  # type: Optional[AnyStr]
    params=None,  # type: Optional[List[InParam]]
):
    # type: (...) -> BasicDataset
    """Get data by executing a stored procedure.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        transaction_id: A transaction identifier. If omitted, the call
            will be executed in its own transaction. Optional.
        params: A list containing all INPUT parameters as InParam
            objects. Optional.

    Returns:
        A Dataset that is the resulting data of the stored procedure
        call.
    """
    result = _execute_sp(
        stored_procedure,
        database=database,
        transaction_id=transaction_id,
        in_params=params,
        get_result_set=True,
    )

    return result["result_set"]


def get_output_params(
    stored_procedure,  # type: AnyStr
    output,  # type: List[OutParam]
    database="",  # type: AnyStr
    transaction_id=None,  # type: Optional[AnyStr]
    params=None,  # type: Optional[List[InParam]]
):
    # type: (...) -> DictIntStringAny
    """Get the Output parameters from the Stored Procedure.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        output: A list containing all OUTPUT parameters as OutParam
            objects.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        transaction_id: A transaction identifier. If omitted, the call
            will be executed in its own transaction. Optional.
        params: A list containing all INPUT parameters as InParam
            objects. Optional.

    Returns:
        A Python dictionary of OUTPUT parameters.
    """
    result = _execute_sp(
        stored_procedure,
        database=database,
        transaction_id=transaction_id,
        in_params=params,
        out_params=output,
        get_out_params=True,
    )

    return result["output_params"]


def get_return_value(
    stored_procedure,  # type: AnyStr
    return_type_code,  # type: int
    database="",  # type: AnyStr
    transaction_id=None,  # type: Optional[AnyStr]
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
        transaction_id: A transaction identifier. If omitted, the call
            will be executed in its own transaction. Optional.
        params: A list containing all INPUT parameters as InParam
            objects. Optional.

    Returns:
        The return value.
    """
    result = _execute_sp(
        stored_procedure,
        database=database,
        transaction_id=transaction_id,
        in_params=params,
        get_ret_val=True,
        return_type_code=return_type_code,
    )

    return result["return_value"]


def o_execute_non_query(
    stored_procedure,  # type: AnyStr
    out_params,  # type: List[OutParam]
    database="",  # type: AnyStr
    transaction_id=None,  # type: Optional[AnyStr]
    in_params=None,  # type: Optional[List[InParam]]
):
    # type: (...) -> Tuple[int, DictIntStringAny]
    """Execute a stored procedure against the connection.

    Used for UPDATE, INSERT, and DELETE statements which return OUTPUT
    parameters.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        out_params: A list containing all OUTPUT parameters as OutParam
            objects.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        transaction_id: A transaction identifier. If omitted, the call
            will be executed in its own transaction. Optional.
        in_params: A list containing all INPUT parameters as InParam
            objects. Optional.

    Returns:
        A tuple containing the number of rows modified by the stored
        procedure, or -1 if not applicable, and the OUTPUT parameters.
    """
    result = _execute_sp(
        stored_procedure,
        database=database,
        transaction_id=transaction_id,
        in_params=in_params,
        out_params=out_params,
        get_out_params=True,
        get_update_count=True,
    )

    return result["update_count"], result["output_params"]


def o_get_data(
    stored_procedure,  # type: AnyStr
    out_params,  # type: List[OutParam]
    database="",  # type: AnyStr
    transaction_id=None,  # type: Optional[AnyStr]
    in_params=None,  # type: Optional[List[InParam]]
):
    # type: (...) -> Tuple[BasicDataset, DictIntStringAny]
    """Get data by executing a stored procedure and OUTPUT parameters.

    Args:
        stored_procedure: The name of the stored procedure to execute.
        out_params: A list containing all OUTPUT parameters as OutParam
            objects.
        database: The name of the database connection to execute
            against. If omitted or "", the project's default database
            connection will be used. Optional.
        transaction_id: A transaction identifier. If omitted, the call
            will be executed in its own transaction. Optional.
        in_params: A list containing all INPUT parameters as InParam
            objects. Optional.

    Returns:
        A tuple containing a Dataset that is the resulting data of the
        stored procedure call, and the OUTPUT parameters.
    """
    result = _execute_sp(
        stored_procedure,
        database=database,
        transaction_id=transaction_id,
        in_params=in_params,
        out_params=out_params,
        get_out_params=True,
        get_result_set=True,
    )

    return result["result_set"], result["output_params"]
