# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u024c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u010b")
        buf.write("\n\f\f\f\16\f\u010e\13\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\7\r\u0119\n\r\f\r\16\r\u011c\13\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\7#\u019d\n#\f#\16")
        buf.write("#\u01a0\13#\3$\3$\3$\5$\u01a5\n$\3$\7$\u01a8\n$\f$\16")
        buf.write("$\u01ab\13$\3$\5$\u01ae\n$\3%\3%\5%\u01b2\n%\3&\3&\3&")
        buf.write("\7&\u01b7\n&\f&\16&\u01ba\13&\3&\3&\3&\3\'\3\'\3\'\3(")
        buf.write("\3(\3(\3(\3(\3(\5(\u01c8\n(\3(\3(\3(\3(\3(\3(\5(\u01d0")
        buf.write("\n(\3)\3)\3)\5)\u01d5\n)\3)\7)\u01d8\n)\f)\16)\u01db\13")
        buf.write(")\5)\u01dd\n)\3*\3*\7*\u01e1\n*\f*\16*\u01e4\13*\3+\3")
        buf.write("+\5+\u01e8\n+\3+\6+\u01eb\n+\r+\16+\u01ec\3,\3,\3-\3-")
        buf.write("\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3")
        buf.write("\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:")
        buf.write("\3:\3;\3;\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3")
        buf.write("A\3B\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3E\3F\6F\u022b\nF\r")
        buf.write("F\16F\u022c\3F\3F\3G\3G\3G\7G\u0234\nG\fG\16G\u0237\13")
        buf.write("G\3G\5G\u023a\nG\3G\3G\3H\3H\3H\7H\u0241\nH\fH\16H\u0244")
        buf.write("\13H\3H\3H\3H\3H\3I\3I\3I\3\u010c\2J\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M\2O(Q\2S\2U\2W)Y*[+]")
        buf.write(",_-a.c/e\60g\61i\62k\63m\64o\65q\66s\67u8w9y:{;}<\177")
        buf.write("=\u0081>\u0083?\u0085@\u0087A\u0089B\u008bC\u008dD\u008f")
        buf.write("E\u0091F\3\2\r\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\3\2\63;\3\2\62;\5\2\f\f$$^^\n\2$$))^^ddhhppttvv\4\2")
        buf.write("GGgg\4\2--//\5\2\13\f\17\17\"\"\3\3\f\f\2\u025e\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2O\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u009f\3\2\2\2\7\u00ac")
        buf.write("\3\2\2\2\t\u00b6\3\2\2\2\13\u00c1\3\2\2\2\r\u00cd\3\2")
        buf.write("\2\2\17\u00da\3\2\2\2\21\u00e5\3\2\2\2\23\u00f1\3\2\2")
        buf.write("\2\25\u00f7\3\2\2\2\27\u0106\3\2\2\2\31\u0114\3\2\2\2")
        buf.write("\33\u011f\3\2\2\2\35\u0127\3\2\2\2\37\u012d\3\2\2\2!\u0134")
        buf.write("\3\2\2\2#\u013c\3\2\2\2%\u0141\3\2\2\2\'\u0147\3\2\2\2")
        buf.write(")\u014a\3\2\2\2+\u014f\3\2\2\2-\u0154\3\2\2\2/\u015a\3")
        buf.write("\2\2\2\61\u0163\3\2\2\2\63\u0167\3\2\2\2\65\u016a\3\2")
        buf.write("\2\2\67\u0171\3\2\2\29\u0177\3\2\2\2;\u017c\3\2\2\2=\u0180")
        buf.write("\3\2\2\2?\u0189\3\2\2\2A\u018f\3\2\2\2C\u0197\3\2\2\2")
        buf.write("E\u019a\3\2\2\2G\u01ad\3\2\2\2I\u01b1\3\2\2\2K\u01b3\3")
        buf.write("\2\2\2M\u01be\3\2\2\2O\u01cf\3\2\2\2Q\u01dc\3\2\2\2S\u01de")
        buf.write("\3\2\2\2U\u01e5\3\2\2\2W\u01ee\3\2\2\2Y\u01f0\3\2\2\2")
        buf.write("[\u01f2\3\2\2\2]\u01f4\3\2\2\2_\u01f6\3\2\2\2a\u01f8\3")
        buf.write("\2\2\2c\u01fa\3\2\2\2e\u01fc\3\2\2\2g\u01fe\3\2\2\2i\u0200")
        buf.write("\3\2\2\2k\u0202\3\2\2\2m\u0204\3\2\2\2o\u0206\3\2\2\2")
        buf.write("q\u0208\3\2\2\2s\u020a\3\2\2\2u\u020c\3\2\2\2w\u020e\3")
        buf.write("\2\2\2y\u0210\3\2\2\2{\u0213\3\2\2\2}\u0216\3\2\2\2\177")
        buf.write("\u0218\3\2\2\2\u0081\u021a\3\2\2\2\u0083\u021d\3\2\2\2")
        buf.write("\u0085\u0220\3\2\2\2\u0087\u0223\3\2\2\2\u0089\u0226\3")
        buf.write("\2\2\2\u008b\u022a\3\2\2\2\u008d\u0230\3\2\2\2\u008f\u023d")
        buf.write("\3\2\2\2\u0091\u0249\3\2\2\2\u0093\u0094\7t\2\2\u0094")
        buf.write("\u0095\7g\2\2\u0095\u0096\7c\2\2\u0096\u0097\7f\2\2\u0097")
        buf.write("\u0098\7K\2\2\u0098\u0099\7p\2\2\u0099\u009a\7v\2\2\u009a")
        buf.write("\u009b\7g\2\2\u009b\u009c\7i\2\2\u009c\u009d\7g\2\2\u009d")
        buf.write("\u009e\7t\2\2\u009e\4\3\2\2\2\u009f\u00a0\7r\2\2\u00a0")
        buf.write("\u00a1\7t\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7p\2\2\u00a3")
        buf.write("\u00a4\7v\2\2\u00a4\u00a5\7K\2\2\u00a5\u00a6\7p\2\2\u00a6")
        buf.write("\u00a7\7v\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7i\2\2\u00a9")
        buf.write("\u00aa\7g\2\2\u00aa\u00ab\7t\2\2\u00ab\6\3\2\2\2\u00ac")
        buf.write("\u00ad\7t\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7c\2\2\u00af")
        buf.write("\u00b0\7f\2\2\u00b0\u00b1\7H\2\2\u00b1\u00b2\7n\2\2\u00b2")
        buf.write("\u00b3\7q\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5\7v\2\2\u00b5")
        buf.write("\b\3\2\2\2\u00b6\u00b7\7y\2\2\u00b7\u00b8\7t\2\2\u00b8")
        buf.write("\u00b9\7k\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb\7g\2\2\u00bb")
        buf.write("\u00bc\7H\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7q\2\2\u00be")
        buf.write("\u00bf\7c\2\2\u00bf\u00c0\7v\2\2\u00c0\n\3\2\2\2\u00c1")
        buf.write("\u00c2\7t\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7c\2\2\u00c4")
        buf.write("\u00c5\7f\2\2\u00c5\u00c6\7D\2\2\u00c6\u00c7\7q\2\2\u00c7")
        buf.write("\u00c8\7q\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("\u00cb\7c\2\2\u00cb\u00cc\7p\2\2\u00cc\f\3\2\2\2\u00cd")
        buf.write("\u00ce\7r\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0\7k\2\2\u00d0")
        buf.write("\u00d1\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7D\2\2\u00d3")
        buf.write("\u00d4\7q\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7n\2\2\u00d6")
        buf.write("\u00d7\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7p\2\2\u00d9")
        buf.write("\16\3\2\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7g\2\2\u00dc")
        buf.write("\u00dd\7c\2\2\u00dd\u00de\7f\2\2\u00de\u00df\7U\2\2\u00df")
        buf.write("\u00e0\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7k\2\2\u00e2")
        buf.write("\u00e3\7p\2\2\u00e3\u00e4\7i\2\2\u00e4\20\3\2\2\2\u00e5")
        buf.write("\u00e6\7r\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7k\2\2\u00e8")
        buf.write("\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7U\2\2\u00eb")
        buf.write("\u00ec\7v\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7k\2\2\u00ee")
        buf.write("\u00ef\7p\2\2\u00ef\u00f0\7i\2\2\u00f0\22\3\2\2\2\u00f1")
        buf.write("\u00f2\7u\2\2\u00f2\u00f3\7w\2\2\u00f3\u00f4\7r\2\2\u00f4")
        buf.write("\u00f5\7g\2\2\u00f5\u00f6\7t\2\2\u00f6\24\3\2\2\2\u00f7")
        buf.write("\u00f8\7r\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7g\2\2\u00fa")
        buf.write("\u00fb\7x\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7p\2\2\u00fd")
        buf.write("\u00fe\7v\2\2\u00fe\u00ff\7F\2\2\u00ff\u0100\7g\2\2\u0100")
        buf.write("\u0101\7h\2\2\u0101\u0102\7c\2\2\u0102\u0103\7w\2\2\u0103")
        buf.write("\u0104\7n\2\2\u0104\u0105\7v\2\2\u0105\26\3\2\2\2\u0106")
        buf.write("\u0107\7\61\2\2\u0107\u0108\7,\2\2\u0108\u010c\3\2\2\2")
        buf.write("\u0109\u010b\13\2\2\2\u010a\u0109\3\2\2\2\u010b\u010e")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010c\u010a\3\2\2\2\u010d")
        buf.write("\u010f\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0110\7,\2\2")
        buf.write("\u0110\u0111\7\61\2\2\u0111\u0112\3\2\2\2\u0112\u0113")
        buf.write("\b\f\2\2\u0113\30\3\2\2\2\u0114\u0115\7\61\2\2\u0115\u0116")
        buf.write("\7\61\2\2\u0116\u011a\3\2\2\2\u0117\u0119\n\2\2\2\u0118")
        buf.write("\u0117\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011b\u011d\3\2\2\2\u011c\u011a\3")
        buf.write("\2\2\2\u011d\u011e\b\r\2\2\u011e\32\3\2\2\2\u011f\u0120")
        buf.write("\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122\7v\2\2\u0122\u0123")
        buf.write("\7g\2\2\u0123\u0124\7i\2\2\u0124\u0125\7g\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\34\3\2\2\2\u0127\u0128\7h\2\2\u0128\u0129")
        buf.write("\7n\2\2\u0129\u012a\7q\2\2\u012a\u012b\7c\2\2\u012b\u012c")
        buf.write("\7v\2\2\u012c\36\3\2\2\2\u012d\u012e\7u\2\2\u012e\u012f")
        buf.write("\7v\2\2\u012f\u0130\7t\2\2\u0130\u0131\7k\2\2\u0131\u0132")
        buf.write("\7p\2\2\u0132\u0133\7i\2\2\u0133 \3\2\2\2\u0134\u0135")
        buf.write("\7d\2\2\u0135\u0136\7q\2\2\u0136\u0137\7q\2\2\u0137\u0138")
        buf.write("\7n\2\2\u0138\u0139\7g\2\2\u0139\u013a\7c\2\2\u013a\u013b")
        buf.write("\7p\2\2\u013b\"\3\2\2\2\u013c\u013d\7c\2\2\u013d\u013e")
        buf.write("\7w\2\2\u013e\u013f\7v\2\2\u013f\u0140\7q\2\2\u0140$\3")
        buf.write("\2\2\2\u0141\u0142\7d\2\2\u0142\u0143\7t\2\2\u0143\u0144")
        buf.write("\7g\2\2\u0144\u0145\7c\2\2\u0145\u0146\7m\2\2\u0146&\3")
        buf.write("\2\2\2\u0147\u0148\7f\2\2\u0148\u0149\7q\2\2\u0149(\3")
        buf.write("\2\2\2\u014a\u014b\7g\2\2\u014b\u014c\7n\2\2\u014c\u014d")
        buf.write("\7u\2\2\u014d\u014e\7g\2\2\u014e*\3\2\2\2\u014f\u0150")
        buf.write("\7v\2\2\u0150\u0151\7t\2\2\u0151\u0152\7w\2\2\u0152\u0153")
        buf.write("\7g\2\2\u0153,\3\2\2\2\u0154\u0155\7h\2\2\u0155\u0156")
        buf.write("\7c\2\2\u0156\u0157\7n\2\2\u0157\u0158\7u\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159.\3\2\2\2\u015a\u015b\7h\2\2\u015b\u015c")
        buf.write("\7w\2\2\u015c\u015d\7p\2\2\u015d\u015e\7e\2\2\u015e\u015f")
        buf.write("\7v\2\2\u015f\u0160\7k\2\2\u0160\u0161\7q\2\2\u0161\u0162")
        buf.write("\7p\2\2\u0162\60\3\2\2\2\u0163\u0164\7h\2\2\u0164\u0165")
        buf.write("\7q\2\2\u0165\u0166\7t\2\2\u0166\62\3\2\2\2\u0167\u0168")
        buf.write("\7k\2\2\u0168\u0169\7h\2\2\u0169\64\3\2\2\2\u016a\u016b")
        buf.write("\7t\2\2\u016b\u016c\7g\2\2\u016c\u016d\7v\2\2\u016d\u016e")
        buf.write("\7w\2\2\u016e\u016f\7t\2\2\u016f\u0170\7p\2\2\u0170\66")
        buf.write("\3\2\2\2\u0171\u0172\7y\2\2\u0172\u0173\7j\2\2\u0173\u0174")
        buf.write("\7k\2\2\u0174\u0175\7n\2\2\u0175\u0176\7g\2\2\u01768\3")
        buf.write("\2\2\2\u0177\u0178\7x\2\2\u0178\u0179\7q\2\2\u0179\u017a")
        buf.write("\7k\2\2\u017a\u017b\7f\2\2\u017b:\3\2\2\2\u017c\u017d")
        buf.write("\7q\2\2\u017d\u017e\7w\2\2\u017e\u017f\7v\2\2\u017f<\3")
        buf.write("\2\2\2\u0180\u0181\7e\2\2\u0181\u0182\7q\2\2\u0182\u0183")
        buf.write("\7p\2\2\u0183\u0184\7v\2\2\u0184\u0185\7k\2\2\u0185\u0186")
        buf.write("\7p\2\2\u0186\u0187\7w\2\2\u0187\u0188\7g\2\2\u0188>\3")
        buf.write("\2\2\2\u0189\u018a\7c\2\2\u018a\u018b\7t\2\2\u018b\u018c")
        buf.write("\7t\2\2\u018c\u018d\7c\2\2\u018d\u018e\7{\2\2\u018e@\3")
        buf.write("\2\2\2\u018f\u0190\7k\2\2\u0190\u0191\7p\2\2\u0191\u0192")
        buf.write("\7j\2\2\u0192\u0193\7g\2\2\u0193\u0194\7t\2\2\u0194\u0195")
        buf.write("\7k\2\2\u0195\u0196\7v\2\2\u0196B\3\2\2\2\u0197\u0198")
        buf.write("\7q\2\2\u0198\u0199\7h\2\2\u0199D\3\2\2\2\u019a\u019e")
        buf.write("\t\3\2\2\u019b\u019d\t\4\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019fF\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01ae\7\62\2")
        buf.write("\2\u01a2\u01a9\t\5\2\2\u01a3\u01a5\7a\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01a8\t\6\2\2\u01a7\u01a4\3\2\2\2\u01a8\u01ab\3\2\2\2")
        buf.write("\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ac\3")
        buf.write("\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ae\b$\3\2\u01ad\u01a1")
        buf.write("\3\2\2\2\u01ad\u01a2\3\2\2\2\u01aeH\3\2\2\2\u01af\u01b2")
        buf.write("\5+\26\2\u01b0\u01b2\5-\27\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b2J\3\2\2\2\u01b3\u01b8\7$\2\2\u01b4")
        buf.write("\u01b7\5M\'\2\u01b5\u01b7\n\7\2\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3")
        buf.write("\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01bb\u01bc\7$\2\2\u01bc\u01bd\b&\4\2\u01bdL")
        buf.write("\3\2\2\2\u01be\u01bf\7^\2\2\u01bf\u01c0\t\b\2\2\u01c0")
        buf.write("N\3\2\2\2\u01c1\u01c2\5Q)\2\u01c2\u01c3\5S*\2\u01c3\u01c4")
        buf.write("\b(\5\2\u01c4\u01d0\3\2\2\2\u01c5\u01c7\5Q)\2\u01c6\u01c8")
        buf.write("\5S*\2\u01c7\u01c6\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9")
        buf.write("\3\2\2\2\u01c9\u01ca\5U+\2\u01ca\u01cb\b(\6\2\u01cb\u01d0")
        buf.write("\3\2\2\2\u01cc\u01cd\5S*\2\u01cd\u01ce\5U+\2\u01ce\u01d0")
        buf.write("\3\2\2\2\u01cf\u01c1\3\2\2\2\u01cf\u01c5\3\2\2\2\u01cf")
        buf.write("\u01cc\3\2\2\2\u01d0P\3\2\2\2\u01d1\u01dd\7\62\2\2\u01d2")
        buf.write("\u01d9\t\5\2\2\u01d3\u01d5\7a\2\2\u01d4\u01d3\3\2\2\2")
        buf.write("\u01d4\u01d5\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d8\t")
        buf.write("\6\2\2\u01d7\u01d4\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7")
        buf.write("\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dd\3\2\2\2\u01db")
        buf.write("\u01d9\3\2\2\2\u01dc\u01d1\3\2\2\2\u01dc\u01d2\3\2\2\2")
        buf.write("\u01ddR\3\2\2\2\u01de\u01e2\7\60\2\2\u01df\u01e1\t\6\2")
        buf.write("\2\u01e0\u01df\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0")
        buf.write("\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3T\3\2\2\2\u01e4\u01e2")
        buf.write("\3\2\2\2\u01e5\u01e7\t\t\2\2\u01e6\u01e8\t\n\2\2\u01e7")
        buf.write("\u01e6\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01ea\3\2\2\2")
        buf.write("\u01e9\u01eb\t\6\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec\3")
        buf.write("\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01edV")
        buf.write("\3\2\2\2\u01ee\u01ef\7*\2\2\u01efX\3\2\2\2\u01f0\u01f1")
        buf.write("\7+\2\2\u01f1Z\3\2\2\2\u01f2\u01f3\7\60\2\2\u01f3\\\3")
        buf.write("\2\2\2\u01f4\u01f5\7.\2\2\u01f5^\3\2\2\2\u01f6\u01f7\7")
        buf.write("=\2\2\u01f7`\3\2\2\2\u01f8\u01f9\7<\2\2\u01f9b\3\2\2\2")
        buf.write("\u01fa\u01fb\7}\2\2\u01fbd\3\2\2\2\u01fc\u01fd\7\177\2")
        buf.write("\2\u01fdf\3\2\2\2\u01fe\u01ff\7]\2\2\u01ffh\3\2\2\2\u0200")
        buf.write("\u0201\7_\2\2\u0201j\3\2\2\2\u0202\u0203\7?\2\2\u0203")
        buf.write("l\3\2\2\2\u0204\u0205\7-\2\2\u0205n\3\2\2\2\u0206\u0207")
        buf.write("\7,\2\2\u0207p\3\2\2\2\u0208\u0209\7\61\2\2\u0209r\3\2")
        buf.write("\2\2\u020a\u020b\7\'\2\2\u020bt\3\2\2\2\u020c\u020d\7")
        buf.write("#\2\2\u020dv\3\2\2\2\u020e\u020f\7/\2\2\u020fx\3\2\2\2")
        buf.write("\u0210\u0211\7?\2\2\u0211\u0212\7?\2\2\u0212z\3\2\2\2")
        buf.write("\u0213\u0214\7#\2\2\u0214\u0215\7?\2\2\u0215|\3\2\2\2")
        buf.write("\u0216\u0217\7@\2\2\u0217~\3\2\2\2\u0218\u0219\7>\2\2")
        buf.write("\u0219\u0080\3\2\2\2\u021a\u021b\7@\2\2\u021b\u021c\7")
        buf.write("?\2\2\u021c\u0082\3\2\2\2\u021d\u021e\7>\2\2\u021e\u021f")
        buf.write("\7?\2\2\u021f\u0084\3\2\2\2\u0220\u0221\7(\2\2\u0221\u0222")
        buf.write("\7(\2\2\u0222\u0086\3\2\2\2\u0223\u0224\7~\2\2\u0224\u0225")
        buf.write("\7~\2\2\u0225\u0088\3\2\2\2\u0226\u0227\7<\2\2\u0227\u0228")
        buf.write("\7<\2\2\u0228\u008a\3\2\2\2\u0229\u022b\t\13\2\2\u022a")
        buf.write("\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022a\3\2\2\2")
        buf.write("\u022c\u022d\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u022f\b")
        buf.write("F\2\2\u022f\u008c\3\2\2\2\u0230\u0235\7$\2\2\u0231\u0234")
        buf.write("\n\7\2\2\u0232\u0234\5M\'\2\u0233\u0231\3\2\2\2\u0233")
        buf.write("\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2")
        buf.write("\u0235\u0236\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3")
        buf.write("\2\2\2\u0238\u023a\t\f\2\2\u0239\u0238\3\2\2\2\u023a\u023b")
        buf.write("\3\2\2\2\u023b\u023c\bG\7\2\u023c\u008e\3\2\2\2\u023d")
        buf.write("\u0242\7$\2\2\u023e\u0241\n\7\2\2\u023f\u0241\5M\'\2\u0240")
        buf.write("\u023e\3\2\2\2\u0240\u023f\3\2\2\2\u0241\u0244\3\2\2\2")
        buf.write("\u0242\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0245\3")
        buf.write("\2\2\2\u0244\u0242\3\2\2\2\u0245\u0246\7^\2\2\u0246\u0247")
        buf.write("\n\b\2\2\u0247\u0248\bH\b\2\u0248\u0090\3\2\2\2\u0249")
        buf.write("\u024a\13\2\2\2\u024a\u024b\bI\t\2\u024b\u0092\3\2\2\2")
        buf.write("\32\2\u010c\u011a\u019e\u01a4\u01a9\u01ad\u01b1\u01b6")
        buf.write("\u01b8\u01c7\u01cf\u01d4\u01d9\u01dc\u01e2\u01e7\u01ec")
        buf.write("\u022c\u0233\u0235\u0239\u0240\u0242\n\b\2\2\3$\2\3&\3")
        buf.write("\3(\4\3(\5\3G\6\3H\7\3I\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    Comment = 11
    LineCmt = 12
    Inttype = 13
    Floattype = 14
    Stringtype = 15
    Booleantype = 16
    Autotype = 17
    Breakkey = 18
    Dokey = 19
    Else = 20
    Trueboolean = 21
    Falseboolean = 22
    Functionkey = 23
    Forkey = 24
    Ifkey = 25
    Returnkey = 26
    Whilekey = 27
    Voidtype = 28
    Outkey = 29
    Continuekey = 30
    Arraytype = 31
    Inheritkey = 32
    Ofkey = 33
    Identifiers = 34
    Int = 35
    Boolean = 36
    String = 37
    FLOAT = 38
    LB = 39
    RB = 40
    DOT = 41
    COMMA = 42
    SEMI = 43
    COLON = 44
    LCB = 45
    RCB = 46
    LSB = 47
    RSB = 48
    ASS = 49
    PLUS = 50
    MULT = 51
    DIV = 52
    MOD = 53
    NOT = 54
    MINUS = 55
    EQUAL = 56
    NOT_EQUAL = 57
    GT = 58
    LT = 59
    GTE = 60
    LTE = 61
    LOGICAL_AND = 62
    LOGICAL_OR = 63
    Stringopr = 64
    WS = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67
    ERROR_CHAR = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'integer'", "'float'", "'string'", 
            "'boolean'", "'auto'", "'break'", "'do'", "'else'", "'true'", 
            "'false'", "'function'", "'for'", "'if'", "'return'", "'while'", 
            "'void'", "'out'", "'continue'", "'array'", "'inherit'", "'of'", 
            "'('", "')'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'['", 
            "']'", "'='", "'+'", "'*'", "'/'", "'%'", "'!'", "'-'", "'=='", 
            "'!='", "'>'", "'<'", "'>='", "'<='", "'&&'", "'||'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "Comment", "LineCmt", "Inttype", "Floattype", "Stringtype", 
            "Booleantype", "Autotype", "Breakkey", "Dokey", "Else", "Trueboolean", 
            "Falseboolean", "Functionkey", "Forkey", "Ifkey", "Returnkey", 
            "Whilekey", "Voidtype", "Outkey", "Continuekey", "Arraytype", 
            "Inheritkey", "Ofkey", "Identifiers", "Int", "Boolean", "String", 
            "FLOAT", "LB", "RB", "DOT", "COMMA", "SEMI", "COLON", "LCB", 
            "RCB", "LSB", "RSB", "ASS", "PLUS", "MULT", "DIV", "MOD", "NOT", 
            "MINUS", "EQUAL", "NOT_EQUAL", "GT", "LT", "GTE", "LTE", "LOGICAL_AND", 
            "LOGICAL_OR", "Stringopr", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "Comment", "LineCmt", "Inttype", 
                  "Floattype", "Stringtype", "Booleantype", "Autotype", 
                  "Breakkey", "Dokey", "Else", "Trueboolean", "Falseboolean", 
                  "Functionkey", "Forkey", "Ifkey", "Returnkey", "Whilekey", 
                  "Voidtype", "Outkey", "Continuekey", "Arraytype", "Inheritkey", 
                  "Ofkey", "Identifiers", "Int", "Boolean", "String", "Escape_sequence", 
                  "FLOAT", "INTEGER_PART", "DECIMAL_PART", "EXPONENT_PART", 
                  "LB", "RB", "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", 
                  "LSB", "RSB", "ASS", "PLUS", "MULT", "DIV", "MOD", "NOT", 
                  "MINUS", "EQUAL", "NOT_EQUAL", "GT", "LT", "GTE", "LTE", 
                  "LOGICAL_AND", "LOGICAL_OR", "Stringopr", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[34] = self.Int_action 
            actions[36] = self.String_action 
            actions[38] = self.FLOAT_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[71] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def Int_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def String_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1]
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace("_","")
     

        if actionIndex == 3:
            self.text = self.text.replace("_","")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	text = self.text[1:-1] if self.text[-1] == '\n' else self.text[1:]
            	raise UncloseString(text)


     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	raise IllegalEscape(str(self.text[1:]))

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


