from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('sseq')
class SseqRecord(RecordBase):
    ix1 = Cpt(EpicsSignalRO, '.IX1')
    ix2 = Cpt(EpicsSignalRO, '.IX2')
    ix3 = Cpt(EpicsSignalRO, '.IX3')
    ix4 = Cpt(EpicsSignalRO, '.IX4')
    ix5 = Cpt(EpicsSignalRO, '.IX5')
    ix6 = Cpt(EpicsSignalRO, '.IX6')
    ix7 = Cpt(EpicsSignalRO, '.IX7')
    ix8 = Cpt(EpicsSignalRO, '.IX8')
    ix9 = Cpt(EpicsSignalRO, '.IX9')
    ixa = Cpt(EpicsSignal, '.IXA')
    werr1 = Cpt(EpicsSignalRO, '.WERR1')
    werr2 = Cpt(EpicsSignalRO, '.WERR2')
    werr3 = Cpt(EpicsSignalRO, '.WERR3')
    werr4 = Cpt(EpicsSignalRO, '.WERR4')
    werr5 = Cpt(EpicsSignalRO, '.WERR5')
    werr6 = Cpt(EpicsSignalRO, '.WERR6')
    werr7 = Cpt(EpicsSignalRO, '.WERR7')
    werr8 = Cpt(EpicsSignalRO, '.WERR8')
    werr9 = Cpt(EpicsSignalRO, '.WERR9')
    werra = Cpt(EpicsSignalRO, '.WERRA')
    wtg1 = Cpt(EpicsSignalRO, '.WTG1')
    wtg2 = Cpt(EpicsSignalRO, '.WTG2')
    wtg3 = Cpt(EpicsSignalRO, '.WTG3')
    wtg4 = Cpt(EpicsSignalRO, '.WTG4')
    wtg5 = Cpt(EpicsSignalRO, '.WTG5')
    wtg6 = Cpt(EpicsSignalRO, '.WTG6')
    wtg7 = Cpt(EpicsSignalRO, '.WTG7')
    wtg8 = Cpt(EpicsSignalRO, '.WTG8')
    wtg9 = Cpt(EpicsSignalRO, '.WTG9')
    wtga = Cpt(EpicsSignal, '.WTGA')
    abort_sequence = Cpt(EpicsSignal, '.ABORT')
    aborting = Cpt(EpicsSignal, '.ABORTING')
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    dol_link_status = Cpt(EpicsSignalRO, '.DOL1V')
    dol_link_status_dol2v = Cpt(EpicsSignalRO, '.DOL2V')
    dol_link_status_dol3v = Cpt(EpicsSignalRO, '.DOL3V')
    dol_link_status_dol4v = Cpt(EpicsSignalRO, '.DOL4V')
    dol_link_status_dol5v = Cpt(EpicsSignalRO, '.DOL5V')
    dol_link_status_dol6v = Cpt(EpicsSignalRO, '.DOL6V')
    dol_link_status_dol7v = Cpt(EpicsSignalRO, '.DOL7V')
    dol_link_status_dol8v = Cpt(EpicsSignalRO, '.DOL8V')
    dol_link_status_dol9v = Cpt(EpicsSignalRO, '.DOL9V')
    dol_link_status_dolav = Cpt(EpicsSignalRO, '.DOLAV')
    dol_link_type = Cpt(EpicsSignalRO, '.DT1')
    dol_link_type_dt2 = Cpt(EpicsSignalRO, '.DT2')
    dol_link_type_dt3 = Cpt(EpicsSignalRO, '.DT3')
    dol_link_type_dt4 = Cpt(EpicsSignalRO, '.DT4')
    dol_link_type_dt5 = Cpt(EpicsSignalRO, '.DT5')
    dol_link_type_dt6 = Cpt(EpicsSignalRO, '.DT6')
    dol_link_type_dt7 = Cpt(EpicsSignalRO, '.DT7')
    dol_link_type_dt8 = Cpt(EpicsSignalRO, '.DT8')
    dol_link_type_dt9 = Cpt(EpicsSignalRO, '.DT9')
    dol_link_type_dta = Cpt(EpicsSignalRO, '.DTA')
    lnk_link_status = Cpt(EpicsSignalRO, '.LNK1V')
    lnk_link_status_lnk2v = Cpt(EpicsSignalRO, '.LNK2V')
    lnk_link_status_lnk3v = Cpt(EpicsSignalRO, '.LNK3V')
    lnk_link_status_lnk4v = Cpt(EpicsSignalRO, '.LNK4V')
    lnk_link_status_lnk5v = Cpt(EpicsSignalRO, '.LNK5V')
    lnk_link_status_lnk6v = Cpt(EpicsSignalRO, '.LNK6V')
    lnk_link_status_lnk7v = Cpt(EpicsSignalRO, '.LNK7V')
    lnk_link_status_lnk8v = Cpt(EpicsSignalRO, '.LNK8V')
    lnk_link_status_lnk9v = Cpt(EpicsSignalRO, '.LNK9V')
    lnk_link_status_lnkav = Cpt(EpicsSignalRO, '.LNKAV')
    lnk_link_type = Cpt(EpicsSignalRO, '.LT1')
    lnk_link_type_lt2 = Cpt(EpicsSignalRO, '.LT2')
    lnk_link_type_lt3 = Cpt(EpicsSignalRO, '.LT3')
    lnk_link_type_lt4 = Cpt(EpicsSignalRO, '.LT4')
    lnk_link_type_lt5 = Cpt(EpicsSignalRO, '.LT5')
    lnk_link_type_lt6 = Cpt(EpicsSignalRO, '.LT6')
    lnk_link_type_lt7 = Cpt(EpicsSignalRO, '.LT7')
    lnk_link_type_lt8 = Cpt(EpicsSignalRO, '.LT8')
    lnk_link_type_lt9 = Cpt(EpicsSignalRO, '.LT9')
    lnk_link_type_lta = Cpt(EpicsSignalRO, '.LTA')
    link_selection = Cpt(EpicsSignal, '.SELN')
    sequence_active = Cpt(EpicsSignalRO, '.BUSY')

    # - display
    display_precision = Cpt(EpicsSignal, '.PREC')

    # - inputs
    link_selection_loc = Cpt(EpicsSignal, '.SELL$')
    select_mechanism = Cpt(EpicsSignal, '.SELM')

    # - seq1
    constant_input_1 = Cpt(EpicsSignal, '.DO1')
    constant_input_10 = Cpt(EpicsSignal, '.DOA')
    constant_input_2 = Cpt(EpicsSignal, '.DO2')
    constant_input_3 = Cpt(EpicsSignal, '.DO3')
    constant_input_4 = Cpt(EpicsSignal, '.DO4')
    constant_input_5 = Cpt(EpicsSignal, '.DO5')
    constant_input_6 = Cpt(EpicsSignal, '.DO6')
    constant_input_7 = Cpt(EpicsSignal, '.DO7')
    constant_input_8 = Cpt(EpicsSignal, '.DO8')
    constant_input_9 = Cpt(EpicsSignal, '.DO9')
    delay_1 = Cpt(EpicsSignal, '.DLY1')
    delay_2 = Cpt(EpicsSignal, '.DLY2')
    delay_3 = Cpt(EpicsSignal, '.DLY3')
    input_link_2 = Cpt(EpicsSignal, '.DOL2$')
    input_link_3 = Cpt(EpicsSignal, '.DOL3$')
    input_link1 = Cpt(EpicsSignal, '.DOL1$')
    output_link_1 = Cpt(EpicsSignal, '.LNK1$')
    output_link_2 = Cpt(EpicsSignal, '.LNK2$')
    output_link_3 = Cpt(EpicsSignal, '.LNK3$')
    string_value_1 = Cpt(EpicsSignal, '.STR1$')
    string_value_2 = Cpt(EpicsSignal, '.STR2$')
    string_value_3 = Cpt(EpicsSignal, '.STR3$')
    string_value_4 = Cpt(EpicsSignal, '.STR4$')
    string_value_5 = Cpt(EpicsSignal, '.STR5$')
    string_value_6 = Cpt(EpicsSignal, '.STR6$')
    string_value_7 = Cpt(EpicsSignal, '.STR7$')
    string_value_8 = Cpt(EpicsSignal, '.STR8$')
    string_value_9 = Cpt(EpicsSignal, '.STR9$')
    string_value_a = Cpt(EpicsSignal, '.STRA$')
    wait_for_completion = Cpt(EpicsSignal, '.WAIT1')
    wait_for_completion_wait2 = Cpt(EpicsSignal, '.WAIT2')
    wait_for_completion_wait3 = Cpt(EpicsSignal, '.WAIT3')
    wait_for_completion_wait4 = Cpt(EpicsSignal, '.WAIT4')
    wait_for_completion_wait5 = Cpt(EpicsSignal, '.WAIT5')
    wait_for_completion_wait6 = Cpt(EpicsSignal, '.WAIT6')
    wait_for_completion_wait7 = Cpt(EpicsSignal, '.WAIT7')
    wait_for_completion_wait8 = Cpt(EpicsSignal, '.WAIT8')
    wait_for_completion_wait9 = Cpt(EpicsSignal, '.WAIT9')
    wait_for_completion_waita = Cpt(EpicsSignal, '.WAITA')

    # - seq2
    delay_4 = Cpt(EpicsSignal, '.DLY4')
    delay_5 = Cpt(EpicsSignal, '.DLY5')
    delay_6 = Cpt(EpicsSignal, '.DLY6')
    input_link_4 = Cpt(EpicsSignal, '.DOL4$')
    input_link_5 = Cpt(EpicsSignal, '.DOL5$')
    input_link_6 = Cpt(EpicsSignal, '.DOL6$')
    output_link_4 = Cpt(EpicsSignal, '.LNK4$')
    output_link_5 = Cpt(EpicsSignal, '.LNK5$')
    output_link_6 = Cpt(EpicsSignal, '.LNK6$')

    # - seq3
    delay_10 = Cpt(EpicsSignal, '.DLYA')
    delay_7 = Cpt(EpicsSignal, '.DLY7')
    delay_8 = Cpt(EpicsSignal, '.DLY8')
    delay_9 = Cpt(EpicsSignal, '.DLY9')
    input_link_10 = Cpt(EpicsSignal, '.DOLA$')
    input_link_7 = Cpt(EpicsSignal, '.DOL7$')
    input_link_8 = Cpt(EpicsSignal, '.DOL8$')
    input_link_9 = Cpt(EpicsSignal, '.DOL9$')
    output_link_10 = Cpt(EpicsSignal, '.LNKA$')
    output_link_7 = Cpt(EpicsSignal, '.LNK7$')
    output_link_8 = Cpt(EpicsSignal, '.LNK8$')
    output_link_9 = Cpt(EpicsSignal, '.LNK9$')
