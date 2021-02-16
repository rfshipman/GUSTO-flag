###########
# GustoObsFlag
###########
import numpy as np
from flags import Flags


class GustoSeqFlag(Flags):
    """
    Define flags which reflect the quality or processing of an observation.  Observations refer to a
    calibratable set of integrations (for example a full OTF scan including the HOTs and REFs)

    usage:
    # produce a level_1a processed flag
    level_1a = GustoSeqFlag(level_1a)

    # a processed level flag in header

    processed_flag = processed_level |

    """
    incomplete = 1, 'incomplete_obs'
    lavel_1a = 4, 'level_1a_processed'
    level_1b = 8, 'level_1b_processed'
    level_1c = 16, 'level_1c_processed'
    badbaselines = 32, 'baseline_issues'



class GustoBbFlag(Flags):
    """
    Define flags reflecting the quality of an individual integration of a building block type .  This could
    be for example the quality of a "HOT" integration.
    """
    corrupt = 1, 'corrupt_data'
    problem = 2, 'unknown_problem'
    ignore = 4, 'ígnore_bb'


class GustoMixerFlag(Flags):
    """
    Define Flags which impact an individual mixer in the array.
    """
    underpumped   = 1, 'mixer_underpumped'
    flag2         = 2, 'TBD'

class GustoChannelFlag(Flags):
    """
    Define Flags which impact individual spectrometer channels, can appear at any channel of any integration
    """
    spike         = 1, 'spike'
    data_ool      = 2, 'out_of_limit'
    possible_line = 4, 'potential_line'
    bad_channel   = 8, 'unknown_problem'
