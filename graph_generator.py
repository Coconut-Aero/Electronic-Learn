from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def colors(i):
    switch_dict = {
        0: 'red',
        1: 'blue',
        2: 'purple',
        3: 'orange',
        4: 'yellow',
        5: 'green',
        6: 'aliceblue',
        7: 'antiquewhite',
        8: 'aqua',
        9: 'aquamarine',
        10: 'azure',
        11: 'beige',
        12: 'bisque',
        13: 'black',
        14: 'blanchedalmond',
        15: 'blueviolet',
        16: 'brown',
        17: 'burlywood',
        18: 'cadetblue',
        19: 'chartreuse',
        20: 'chocolate',
        21: 'coral',
        22: 'cornflowerblue',
        23: 'cornsilk',
        24: 'crimson',
        25: 'cyan',
        26: 'darkblue',
        27: 'darkcyan',
        28: 'darkgoldenrod',
        29: 'darkgray',
        30: 'darkgreen',
        31: 'darkgrey',
        32: 'darkkhaki',
        33: 'darkmagenta',
        34: 'darkolivegreen',
        35: 'darkorange',
        36: 'darkorchid',
        37: 'darkred',
        38: 'darksalmon',
        39: 'darkseagreen',
        40: 'darkslateblue',
        41: 'darkslategray',
        42: 'darkslategrey',
        43: 'darkturquoise',
        44: 'darkviolet',
        45: 'deeppink',
        46: 'deepskyblue',
        47: 'dimgray',
        48: 'dimgrey',
        49: 'dodgerblue',
        50: 'firebrick',
        51: 'floralwhite',
        52: 'forestgreen',
        53: 'fuchsia',
        54: 'gainsboro',
        55: 'ghostwhite',
        56: 'gold',
        57: 'goldenrod',
        58: 'gray',
        59: 'greenyellow',
        60: 'grey',
        61: 'honeydew',
        62: 'hotpink',
        63: 'indianred',
        64: 'indigo',
        65: 'ivory',
        66: 'khaki',
        67: 'lavender',
        68: 'lavenderblush',
        69: 'lawngreen',
        70: 'lemonchiffon',
        71: 'lightblue',
        72: 'lightcoral',
        73: 'lightcyan',
        74: 'lightgoldenrodyellow',
        75: 'lightgray',
        76: 'lightgreen',
        77: 'lightgrey',
        78: 'lightpink',
        79: 'lightsalmon',
        80: 'lightseagreen',
        81: 'lightskyblue',
        82: 'lightslategray',
        83: 'lightslategrey',
        84: 'lightsteelblue',
        85: 'lightyellow',
        86: 'lime',
        87: 'limegreen',
        88: 'linen',
        89: 'magenta',
        90: 'maroon',
        91: 'mediumaquamarine',
        92: 'mediumblue',
        93: 'mediumorchid',
        94: 'mediumpurple',
        95: 'mediumseagreen',
        96: 'mediumslateblue',
        97: 'mediumspringgreen',
        98: 'mediumturquoise',
        99: 'mediumvioletred',
        100: 'midnightblue',
        101: 'mintcream',
        102: 'mistyrose',
        103: 'moccasin',
        104: 'navajowhite',
        105: 'navy',
        106: 'oldlace',
        107: 'olive',
        108: 'olivedrab',
        109: 'orangered',
        110: 'orchid',
        111: 'palegoldenrod',
        112: 'palegreen',
        113: 'paleturquoise',
        114: 'palevioletred',
        115: 'papayawhip',
        116: 'peachpuff',
        117: 'peru',
        118: 'plum',
        119: 'powderblue',
        120: 'purple',
        121: 'rebeccapurple',
        122: 'rosybrown',
        123: 'royalblue',
        124: 'saddlebrown',
        125: 'salmon',
        126: 'sandybrown',
        127: 'seagreen',
        128: 'seashell',
        129: 'sienna',
        130: 'silver',
        131: 'skyblue',
        132: 'slateblue',
        133: 'slategray',
        134: 'slategrey',
        135: 'snow',
        136: 'springgreen',
        137: 'steelblue',
        138: 'tan',
        139: 'teal',
        140: 'thistle',
        141: 'tomato',
        142: 'turquoise',
        143: 'violet',
        144: 'wheat',
        145: 'white',
        146: 'whitesmoke',
        147: 'yellowgreen'
    }
    return switch_dict[i]

def main(count: int, steps_extended, lens, suptitle, file_name, *args,):
    fig, axs = plt.subplots(count, 1, figsize=(8, 10))
    for i in range(count):
        if i == count-1:
            extended = args[i]
            label = args[i + count]
            axs[i].step(steps_extended, extended, where='post', label=label, marker='o', color=colors(i))
            axs[i].set_title(label)
            axs[i].set_ylabel('Digital Signal')
            break
        else:
            extended = args[i]
            label = args[i + count]
            axs[i].step(steps_extended, extended, where='post', label=label, marker='o', color=colors(i))
            axs[i].set_title(label)
            axs[i].set_ylabel('Digital Signal')
    for ax in axs:
        ax.set_xticks(np.arange(lens))
        ax.set_xticklabels(np.arange(1, lens + 1))
    plt.suptitle(suptitle, fontsize=16)
    plt.tight_layout()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    plt.annotate(f"Author: XiaoYi Zero\nGenerated on: {current_time}",
                 xy=(0.01, 0.96), xycoords='figure fraction', ha='left', va='top', fontsize=10)
    plt.annotate(f"Software: Python & Matplotlib & KiCAD",
                 xy=(0.99, 0.95), xycoords='figure fraction', ha='right', va='top', fontsize=10)

    plt.savefig(file_name, format="png")
    plt.show()
