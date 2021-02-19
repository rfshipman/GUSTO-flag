###########
# GustoObsFlag
###########
from enum import IntFlag


class GustoSeqFlag(IntFlag):
    """
    Define flags which reflect the quality or processing of an observation (sequence of bbtypes).  Observations refer to a
    calibratable set of integrations (for example a full OTF scan including the HOTs and REFs)

    usage:
    # produce a level_1a processed flag
    level_1a = GustoSeqFlag(level_1a)

    # a processed level flag in header

    processed_flag = processed_level |

    """
    INCOMPLETE = IntFlag(1) #, 'incomplete_obs'
    LEVEL_1A = IntFlag(2)  # 'level_1a_processed'
    LEVEL_1B = IntFlag(4)   # 'level_1b_processed'
    LEVEL_1C = IntFlag(8) #  'level_1c_processed'
    BADBASELINE = IntFlag(16) # 'baseline_issues'


class GustoBbtypeFlag(IntFlag):
    """

    Define Flags which impact an integration or bbtype

    """
    CORRUPT = IntFlag(1) # corrupted data
    FLIPMIRROR = IntFlag(2) # mirror not settled
    IGNORE = IntFlag(4) # don't use itegration in further processing


class GustoMixerFlag(IntFlag):
    """

    Define Flags which impact individual mixers

    """
    UNDERPUMPTED = IntFlag(1)
    PROBLEM = IntFlag(2)


class GustoChannelFlag(IntFlag):
    """

    Define Flags which impact individual spectrometer channels, can appear at any channel of any integration

    """
    SPIKE = IntFlag(1) #, 'spike'
    DATA_OOL = IntFlag(2) #, 'out_of_limit'
    POSSIBLE_LINE = IntFlag(4) #, 'potential_line'
    BAD_CHANNEL = IntFlag(8) #, 'unknown_problem'
