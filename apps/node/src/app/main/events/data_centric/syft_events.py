# Standard Python imports
import json

# External imports
import syft as sy
from flask_login import current_user
from syft.exceptions import EmptyCryptoPrimitiveStoreError
from syft.exceptions import GetNotPermittedError
from syft.exceptions import ResponseSignatureError

# Local imports
from ... import hook, local_worker
from ...data_centric.auth import UserSession, authenticated_only
from ...data_centric.persistence.object_storage import recover_objects


@authenticated_only
def forward_binary_message(message: bin) -> bin:
    """Forward binary syft messages to user's workers.

    Args:
        message (bin) : PySyft binary message.
    Returns:
        response (bin) : PySyft binary response.
    """
    try:
        ## If worker is empty, load previous database tensors.
        if not current_user.worker._objects:
            recover_objects(current_user.worker)

        # Process message
        decoded_response = current_user.worker._recv_msg(message)

    except (
        EmptyCryptoPrimitiveStoreError,
        GetNotPermittedError,
        ResponseSignatureError,
    ) as e:
        # Register this request into tensor owner account.
        if hasattr(current_user, "save_tensor_request"):
            message = sy.serde.deserialize(message, worker=current_user.worker)
            current_user.save_request(message._contents)

        decoded_response = sy.serde.serialize(e)
    return decoded_response


@authenticated_only
def syft_command(message: dict) -> str:
    """Forward JSON syft messages to user's workers.

    Args:
        message (dict) : Dictionary data structure containing PySyft message.
    Returns:
        response (str) : Node response.
    """
    response = local_worker._message_router[message["msg_type"]](message["content"])
    payload = sy.serde.serialize(response, force_no_serialization=True)
    return json.dumps({"type": "command-response", "response": payload})
