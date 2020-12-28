import sys
from random import randint

import pytest
from src.app.main.model_centric.processes.fl_process import FLProcess

from . import BIG_INT
from .presets.fl_process import (
    AVG_PLANS,
    CLIENT_CONFIGS,
    CYCLES,
    MODELS,
    PROTOCOLS,
    SERVER_CONFIGS,
    TRAINING_PLANS,
    VALIDATION_PLANS,
)

sys.path.append(".")


@pytest.mark.parametrize(
    """model,
                         avg_plan,
                         train_plan,
                         valid_plan,
                         protocol,
                         client_config,
                         server_config,
                         cycle""",
    list(
        zip(
            MODELS,
            AVG_PLANS,
            TRAINING_PLANS,
            VALIDATION_PLANS,
            PROTOCOLS,
            CLIENT_CONFIGS,
            SERVER_CONFIGS,
            CYCLES,
        )
    ),
)
def test_create_fl_process_object(
    model,
    avg_plan,
    train_plan,
    valid_plan,
    protocol,
    client_config,
    server_config,
    cycle,
    database,
):
    new_fl_process = FLProcess(id=randint(0, BIG_INT))

    database.session.add(new_fl_process)

    model.flprocess = new_fl_process
    database.session.add(model)

    avg_plan.avg_flprocess = new_fl_process
    database.session.add(avg_plan)

    train_plan.plan_flprocess = new_fl_process
    database.session.add(train_plan)

    valid_plan.plan_flprocess = new_fl_process
    database.session.add(valid_plan)

    protocol.protocol_flprocess = new_fl_process
    database.session.add(protocol)

    client_config.client_flprocess_config = new_fl_process
    database.session.add(client_config)

    server_config.server_flprocess_config = new_fl_process
    database.session.add(server_config)

    cycle.cycle_flprocess = new_fl_process
    database.session.add(cycle)

    database.session.commit()
