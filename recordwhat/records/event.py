from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('event')
class EventRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')
    simulation_value = Cpt(EpicsSignal, '.SVAL')

    # - inputs
    input_specification = Cpt(EpicsSignal, '.INP$')
    sim_input_specifctn = Cpt(EpicsSignal, '.SIOL$')
    sim_mode_location = Cpt(EpicsSignal, '.SIML$')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')
