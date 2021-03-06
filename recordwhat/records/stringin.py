from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('stringin')
class StringinRecord(RecordBase):
    value = Cpt(EpicsSignal, '.VAL$')

    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    previous_value = Cpt(EpicsSignalRO, '.OVAL$')
    simulation_mode = Cpt(EpicsSignal, '.SIMM')
    simulation_value = Cpt(EpicsSignal, '.SVAL$')

    # - display
    post_archive_monitors = Cpt(EpicsSignal, '.APST')
    post_value_monitors = Cpt(EpicsSignal, '.MPST')

    # - inputs
    input_specification = Cpt(EpicsSignal, '.INP$')
    sim_input_specifctn = Cpt(EpicsSignal, '.SIOL$')
    sim_mode_location = Cpt(EpicsSignal, '.SIML$')
    sim_mode_alarm_svrty = Cpt(EpicsSignal, '.SIMS')
