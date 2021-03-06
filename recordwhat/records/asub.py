from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)


@_register_record_type('aSub')
class AsubRecord(RecordBase):
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    num_elements_in_ovla = Cpt(EpicsSignalRO, '.ONVA')
    num_elements_in_ovlb = Cpt(EpicsSignalRO, '.ONVB')
    num_elements_in_ovlc = Cpt(EpicsSignalRO, '.ONVC')
    num_elements_in_ovld = Cpt(EpicsSignalRO, '.ONVD')
    num_elements_in_ovle = Cpt(EpicsSignalRO, '.ONVE')
    num_elements_in_ovlf = Cpt(EpicsSignalRO, '.ONVF')
    num_elements_in_ovlg = Cpt(EpicsSignalRO, '.ONVG')
    num_elements_in_ovli = Cpt(EpicsSignalRO, '.ONVI')
    num_elements_in_ovlj = Cpt(EpicsSignalRO, '.ONVJ')
    num_elements_in_ovlk = Cpt(EpicsSignalRO, '.ONVK')
    num_elements_in_ovll = Cpt(EpicsSignalRO, '.ONVL')
    num_elements_in_ovlm = Cpt(EpicsSignalRO, '.ONVM')
    num_elements_in_ovln = Cpt(EpicsSignalRO, '.ONVN')
    num_elements_in_ovlo = Cpt(EpicsSignalRO, '.ONVO')
    num_elements_in_ovlp = Cpt(EpicsSignalRO, '.ONVP')
    num_elements_in_ovlq = Cpt(EpicsSignalRO, '.ONVQ')
    num_elements_in_ovlr = Cpt(EpicsSignalRO, '.ONVR')
    num_elements_in_ovls = Cpt(EpicsSignalRO, '.ONVS')
    num_elements_in_ovlt = Cpt(EpicsSignalRO, '.ONVT')
    num_elements_in_ovlu = Cpt(EpicsSignalRO, '.ONVU')
    num_elements_in_vala = Cpt(EpicsSignalRO, '.NEVA')
    num_elements_in_valb = Cpt(EpicsSignalRO, '.NEVB')
    num_elements_in_valc = Cpt(EpicsSignalRO, '.NEVC')
    num_elements_in_vald = Cpt(EpicsSignalRO, '.NEVD')
    num_elements_in_vale = Cpt(EpicsSignalRO, '.NEVE')
    num_elements_in_valf = Cpt(EpicsSignalRO, '.NEVF')
    num_elements_in_valg = Cpt(EpicsSignalRO, '.NEVG')
    num_elements_in_vali = Cpt(EpicsSignalRO, '.NEVI')
    num_elements_in_valj = Cpt(EpicsSignalRO, '.NEVJ')
    num_elements_in_valk = Cpt(EpicsSignalRO, '.NEVK')
    num_elements_in_vall = Cpt(EpicsSignalRO, '.NEVL')
    num_elements_in_valm = Cpt(EpicsSignalRO, '.NEVM')
    num_elements_in_valn = Cpt(EpicsSignalRO, '.NEVN')
    num_elements_in_valo = Cpt(EpicsSignalRO, '.NEVO')
    num_elements_in_valp = Cpt(EpicsSignalRO, '.NEVP')
    num_elements_in_valq = Cpt(EpicsSignalRO, '.NEVQ')
    num_elements_in_valr = Cpt(EpicsSignalRO, '.NEVR')
    num_elements_in_vals = Cpt(EpicsSignalRO, '.NEVS')
    num_elements_in_valt = Cpt(EpicsSignalRO, '.NEVT')
    num_elements_in_valu = Cpt(EpicsSignalRO, '.NEVU')
    num_elements_in_valh = Cpt(EpicsSignalRO, '.NEVH')
    num_elements_in_valh_onvh = Cpt(EpicsSignalRO, '.ONVH')
    old_return_value = Cpt(EpicsSignalRO, '.OVAL')

    # - display
    display_precision = Cpt(EpicsSignal, '.PREC')

    # - inputs
    input_link_a = Cpt(EpicsSignal, '.INPA$')
    input_link_b = Cpt(EpicsSignal, '.INPB$')
    input_link_c = Cpt(EpicsSignal, '.INPC$')
    input_link_d = Cpt(EpicsSignal, '.INPD$')
    input_link_e = Cpt(EpicsSignal, '.INPE$')
    input_link_f = Cpt(EpicsSignal, '.INPF$')
    input_link_g = Cpt(EpicsSignal, '.INPG$')
    input_link_h = Cpt(EpicsSignal, '.INPH$')
    input_link_i = Cpt(EpicsSignal, '.INPI$')
    input_link_j = Cpt(EpicsSignal, '.INPJ$')
    input_link_k = Cpt(EpicsSignal, '.INPK$')
    input_link_l = Cpt(EpicsSignal, '.INPL$')
    input_link_m = Cpt(EpicsSignal, '.INPM$')
    input_link_n = Cpt(EpicsSignal, '.INPN$')
    input_link_o = Cpt(EpicsSignal, '.INPO$')
    input_link_p = Cpt(EpicsSignal, '.INPP$')
    input_link_q = Cpt(EpicsSignal, '.INPQ$')
    input_link_r = Cpt(EpicsSignal, '.INPR$')
    input_link_s = Cpt(EpicsSignal, '.INPS$')
    input_link_t = Cpt(EpicsSignal, '.INPT$')
    input_link_u = Cpt(EpicsSignal, '.INPU$')

    # - output
    output_event_flag = Cpt(EpicsSignal, '.EFLG')
    output_link_a = Cpt(EpicsSignal, '.OUTA$')
    output_link_b = Cpt(EpicsSignal, '.OUTB$')
    output_link_c = Cpt(EpicsSignal, '.OUTC$')
    output_link_d = Cpt(EpicsSignal, '.OUTD$')
    output_link_e = Cpt(EpicsSignal, '.OUTE$')
    output_link_f = Cpt(EpicsSignal, '.OUTF$')
    output_link_g = Cpt(EpicsSignal, '.OUTG$')
    output_link_h = Cpt(EpicsSignal, '.OUTH$')
    output_link_i = Cpt(EpicsSignal, '.OUTI$')
    output_link_j = Cpt(EpicsSignal, '.OUTJ$')
    output_link_k = Cpt(EpicsSignal, '.OUTK$')
    output_link_l = Cpt(EpicsSignal, '.OUTL$')
    output_link_m = Cpt(EpicsSignal, '.OUTM$')
    output_link_n = Cpt(EpicsSignal, '.OUTN$')
    output_link_o = Cpt(EpicsSignal, '.OUTO$')
    output_link_p = Cpt(EpicsSignal, '.OUTP$')
    output_link_q = Cpt(EpicsSignal, '.OUTQ$')
    output_link_r = Cpt(EpicsSignal, '.OUTR$')
    output_link_s = Cpt(EpicsSignal, '.OUTS$')
    output_link_t = Cpt(EpicsSignal, '.OUTT$')
    output_link_u = Cpt(EpicsSignal, '.OUTU$')

    # - sub
    bad_return_severity = Cpt(EpicsSignal, '.BRSV')
    initialize_subr_name = Cpt(EpicsSignalRO, '.INAM$')
    old_subr_name = Cpt(EpicsSignalRO, '.ONAM$')
    process_subr_name = Cpt(EpicsSignal, '.SNAM$')
    subr_input_enable = Cpt(EpicsSignal, '.LFLG')
    subroutine_name_link = Cpt(EpicsSignalRO, '.SUBL$')

    # - wave
    max_elements_in_a = Cpt(EpicsSignalRO, '.NOA')
    max_elements_in_b = Cpt(EpicsSignalRO, '.NOB')
    max_elements_in_c = Cpt(EpicsSignalRO, '.NOC')
    max_elements_in_d = Cpt(EpicsSignalRO, '.NOD')
    max_elements_in_e = Cpt(EpicsSignalRO, '.NOE')
    max_elements_in_f = Cpt(EpicsSignalRO, '.NOF')
    max_elements_in_g = Cpt(EpicsSignalRO, '.NOG')
    max_elements_in_h = Cpt(EpicsSignalRO, '.NOH')
    max_elements_in_i = Cpt(EpicsSignalRO, '.NOI')
    max_elements_in_j = Cpt(EpicsSignalRO, '.NOJ')
    max_elements_in_k = Cpt(EpicsSignalRO, '.NOK')
    max_elements_in_l = Cpt(EpicsSignalRO, '.NOL')
    max_elements_in_m = Cpt(EpicsSignalRO, '.NOM')
    max_elements_in_n = Cpt(EpicsSignalRO, '.NON')
    max_elements_in_o = Cpt(EpicsSignalRO, '.NOO')
    max_elements_in_p = Cpt(EpicsSignalRO, '.NOP')
    max_elements_in_q = Cpt(EpicsSignalRO, '.NOQ')
    max_elements_in_r = Cpt(EpicsSignalRO, '.NOR')
    max_elements_in_s = Cpt(EpicsSignalRO, '.NOS')
    max_elements_in_t = Cpt(EpicsSignalRO, '.NOT')
    max_elements_in_u = Cpt(EpicsSignalRO, '.NOU')
    max_elements_in_vala = Cpt(EpicsSignalRO, '.NOVA')
    max_elements_in_valb = Cpt(EpicsSignalRO, '.NOVB')
    max_elements_in_valc = Cpt(EpicsSignalRO, '.NOVC')
    max_elements_in_vald = Cpt(EpicsSignalRO, '.NOVD')
    max_elements_in_vale = Cpt(EpicsSignalRO, '.NOVE')
    max_elements_in_valf = Cpt(EpicsSignalRO, '.NOVF')
    max_elements_in_valg = Cpt(EpicsSignalRO, '.NOVG')
    max_elements_in_vali = Cpt(EpicsSignalRO, '.NOVI')
    max_elements_in_valj = Cpt(EpicsSignalRO, '.NOVJ')
    max_elements_in_valk = Cpt(EpicsSignalRO, '.NOVK')
    max_elements_in_vall = Cpt(EpicsSignalRO, '.NOVL')
    max_elements_in_valm = Cpt(EpicsSignalRO, '.NOVM')
    max_elements_in_valn = Cpt(EpicsSignalRO, '.NOVN')
    max_elements_in_valo = Cpt(EpicsSignalRO, '.NOVO')
    max_elements_in_valp = Cpt(EpicsSignalRO, '.NOVP')
    max_elements_in_valq = Cpt(EpicsSignalRO, '.NOVQ')
    max_elements_in_valr = Cpt(EpicsSignalRO, '.NOVR')
    max_elements_in_vals = Cpt(EpicsSignalRO, '.NOVS')
    max_elements_in_valt = Cpt(EpicsSignalRO, '.NOVT')
    max_elements_in_valu = Cpt(EpicsSignalRO, '.NOVU')
    max_elements_in_valh = Cpt(EpicsSignalRO, '.NOVH')
    num_elements_in_a = Cpt(EpicsSignalRO, '.NEA')
    num_elements_in_b = Cpt(EpicsSignalRO, '.NEB')
    num_elements_in_c = Cpt(EpicsSignalRO, '.NEC')
    num_elements_in_d = Cpt(EpicsSignalRO, '.NED')
    num_elements_in_e = Cpt(EpicsSignalRO, '.NEE')
    num_elements_in_f = Cpt(EpicsSignalRO, '.NEF')
    num_elements_in_g = Cpt(EpicsSignalRO, '.NEG')
    num_elements_in_h = Cpt(EpicsSignalRO, '.NEH')
    num_elements_in_i = Cpt(EpicsSignalRO, '.NEI')
    num_elements_in_j = Cpt(EpicsSignalRO, '.NEJ')
    num_elements_in_k = Cpt(EpicsSignalRO, '.NEK')
    num_elements_in_l = Cpt(EpicsSignalRO, '.NEL')
    num_elements_in_m = Cpt(EpicsSignalRO, '.NEM')
    num_elements_in_n = Cpt(EpicsSignalRO, '.NEN')
    num_elements_in_o = Cpt(EpicsSignalRO, '.NEO')
    num_elements_in_p = Cpt(EpicsSignalRO, '.NEP')
    num_elements_in_q = Cpt(EpicsSignalRO, '.NEQ')
    num_elements_in_r = Cpt(EpicsSignalRO, '.NER')
    num_elements_in_s = Cpt(EpicsSignalRO, '.NES')
    num_elements_in_t = Cpt(EpicsSignalRO, '.NET')
    num_elements_in_u = Cpt(EpicsSignalRO, '.NEU')
    type_of_a = Cpt(EpicsSignalRO, '.FTA')
    type_of_b = Cpt(EpicsSignalRO, '.FTB')
    type_of_c = Cpt(EpicsSignalRO, '.FTC')
    type_of_d = Cpt(EpicsSignalRO, '.FTD')
    type_of_e = Cpt(EpicsSignalRO, '.FTE')
    type_of_f = Cpt(EpicsSignalRO, '.FTF')
    type_of_g = Cpt(EpicsSignalRO, '.FTG')
    type_of_h = Cpt(EpicsSignalRO, '.FTH')
    type_of_i = Cpt(EpicsSignalRO, '.FTI')
    type_of_j = Cpt(EpicsSignalRO, '.FTJ')
    type_of_k = Cpt(EpicsSignalRO, '.FTK')
    type_of_l = Cpt(EpicsSignalRO, '.FTL')
    type_of_m = Cpt(EpicsSignalRO, '.FTM')
    type_of_n = Cpt(EpicsSignalRO, '.FTN')
    type_of_o = Cpt(EpicsSignalRO, '.FTO')
    type_of_p = Cpt(EpicsSignalRO, '.FTP')
    type_of_q = Cpt(EpicsSignalRO, '.FTQ')
    type_of_r = Cpt(EpicsSignalRO, '.FTR')
    type_of_s = Cpt(EpicsSignalRO, '.FTS')
    type_of_t = Cpt(EpicsSignalRO, '.FTT')
    type_of_u = Cpt(EpicsSignalRO, '.FTU')
    type_of_vala = Cpt(EpicsSignalRO, '.FTVA')
    type_of_valb = Cpt(EpicsSignalRO, '.FTVB')
    type_of_valc = Cpt(EpicsSignalRO, '.FTVC')
    type_of_vald = Cpt(EpicsSignalRO, '.FTVD')
    type_of_vale = Cpt(EpicsSignalRO, '.FTVE')
    type_of_valf = Cpt(EpicsSignalRO, '.FTVF')
    type_of_valg = Cpt(EpicsSignalRO, '.FTVG')
    type_of_valh = Cpt(EpicsSignalRO, '.FTVH')
    type_of_vali = Cpt(EpicsSignalRO, '.FTVI')
    type_of_valj = Cpt(EpicsSignalRO, '.FTVJ')
    type_of_valk = Cpt(EpicsSignalRO, '.FTVK')
    type_of_vall = Cpt(EpicsSignalRO, '.FTVL')
    type_of_valm = Cpt(EpicsSignalRO, '.FTVM')
    type_of_valn = Cpt(EpicsSignalRO, '.FTVN')
    type_of_valo = Cpt(EpicsSignalRO, '.FTVO')
    type_of_valp = Cpt(EpicsSignalRO, '.FTVP')
    type_of_valq = Cpt(EpicsSignalRO, '.FTVQ')
    type_of_valr = Cpt(EpicsSignalRO, '.FTVR')
    type_of_vals = Cpt(EpicsSignalRO, '.FTVS')
    type_of_valt = Cpt(EpicsSignalRO, '.FTVT')
    type_of_valu = Cpt(EpicsSignalRO, '.FTVU')
