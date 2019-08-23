max_scale = 6159.
offset = 0 #max_scale / 2

c = lambda v: -int((v - offset) * (2**15 / max_scale))
#c = lambda v: v
Point = lambda x, y: (x, y)

UINT16_MAX = 2**16 - 1
col_c = lambda col: int((col / 255.) * UINT16_MAX)

def points(ps, r=0, g=255, b=0):
	return [(c(x), c(y), col_c(r), col_c(g), col_c(b), 0, 0, 0) for x, y in ps]

rakete_cccp = points([(2035, 394), (1948, 398), (1861, 406), (1774, 418), 
(1688, 433), (1602, 451), (1519, 479), (1436, 507), 
(1354, 535), (1271, 563), (1188, 591), (1105, 619), 
(1022, 648), (939, 676), (856, 704), (856, 704), 
(846, 703), (837, 694), (795, 648), (769, 621), 
(761, 611), (765, 602), (781, 583), (837, 515), 
(845, 506), (853, 496), (851, 492), (801, 500), 
(717, 523), (638, 559), (565, 607), (499, 665), 
(466, 703), (462, 714), (467, 725), (478, 729), 
(564, 716), (552, 715), (564, 716), (570, 727), 
(597, 796), (602, 808), (607, 819), (595, 824), 
(549, 843), (490, 854), (484, 849), (492, 840), 
(519, 814), (527, 805), (515, 799), (492, 791), 
(405, 794), (324, 826), (248, 869), (177, 920), 
(110, 977), (110, 977), (101, 985), (111, 984), 
(173, 975), (259, 961), (344, 970), (344, 970), 
(356, 973), (357, 984), (351, 1046), (373, 1129), 
(433, 1192), (476, 1218), (487, 1223), (499, 1220), 
(512, 1218), (596, 1201), (585, 1202), (596, 1201), 
(593, 1213), (580, 1287), (565, 1373), (565, 1373), 
(562, 1385), (551, 1392), (498, 1424), (455, 1450), 
(445, 1457), (444, 1461), (457, 1463), (544, 1473), 
(631, 1477), (718, 1473), (804, 1454), (880, 1413), 
(889, 1404), (898, 1395), (897, 1383), (850, 1369), 
(763, 1365), (763, 1365), (750, 1365), (752, 1357), 
(783, 1303), (827, 1227), (909, 1205), (995, 1187), 
(1076, 1157), (1111, 1122), (1111, 1110), (1105, 1100), 
(1093, 1096), (1030, 1098), (1018, 1099), (1019, 1098), 
(1103, 1076), (1188, 1054), (1273, 1032), (1357, 1010), 
(1442, 988), (1527, 966), (1611, 944), (1696, 922), 
(1781, 900), (1862, 867), (1943, 836), (2021, 796), 
(2094, 747), (2162, 692), (2226, 633), (2288, 571), 
(2349, 508), (2391, 462), (2399, 452), (2389, 449), 
(2304, 428), (2219, 409), (2132, 397), (2045, 394), 
(2058, 394), (2045, 394), (2037, 415), (2112, 417), 
(2199, 427), (2285, 445), (2345, 461), (2357, 464), 
(2350, 473), (2290, 537), (2229, 599), (2165, 659), 
(2099, 715), (2027, 766), (1951, 808), (1870, 841), 
(1789, 875), (1704, 897), (1620, 919), (1535, 941), 
(1450, 963), (1366, 985), (1281, 1007), (1196, 1029), 
(1112, 1051), (1027, 1073), (1003, 1079), (991, 1082), 
(986, 1092), (984, 1104), (983, 1116), (989, 1122), 
(1076, 1118), (1076, 1118), (1088, 1118), (1080, 1127), 
(1025, 1158), (940, 1176), (854, 1194), (830, 1199), 
(817, 1201), (811, 1211), (792, 1244), (748, 1319), 
(717, 1373), (710, 1384), (721, 1386), (808, 1388), 
(846, 1390), (858, 1392), (863, 1396), (843, 1410), 
(762, 1443), (676, 1455), (588, 1454), (507, 1444), 
(513, 1447), (507, 1444), (518, 1438), (582, 1399), 
(571, 1405), (582, 1399), (585, 1387), (598, 1313), 
(613, 1227), (620, 1190), (622, 1178), (617, 1173), 
(593, 1178), (507, 1196), (431, 1163), (380, 1093), 
(374, 1006), (381, 969), (381, 959), (369, 955), 
(346, 947), (261, 939), (174, 952), (187, 950), 
(174, 952), (183, 945), (243, 900), (318, 854), 
(398, 820), (485, 813), (472, 811), (485, 813), 
(480, 821), (445, 856), (441, 864), (453, 867), 
(502, 879), (514, 881), (525, 876), (537, 872), 
(618, 839), (618, 839), (630, 834), (633, 826), 
(609, 768), (568, 694), (507, 702), (495, 704), 
(503, 695), (567, 635), (639, 585), (718, 548), 
(801, 524), (790, 527), (801, 524), (793, 534), 
(745, 591), (737, 601), (731, 611), (739, 620), 
(773, 657), (832, 721), (832, 721), (841, 730), 
(852, 728), (911, 708), (994, 680), (1077, 652), 
(1160, 624), (1243, 596), (1325, 568), (1408, 540), 
(1491, 512), (1574, 484), (1658, 460), (1744, 445), 
(1831, 432), (1918, 422), (2005, 416), (2018, 416), 
(2030, 415), (583, 1555), (533, 1561), (452, 1593), 
(389, 1653), (350, 1731), (336, 1817), (342, 1904), 
(372, 1986), (428, 2053), (504, 2094), (590, 2106), 
(676, 2089), (748, 2040), (756, 2031), (764, 2021), 
(759, 2012), (725, 1975), (700, 1947), (691, 1938), 
(683, 1940), (665, 1957), (584, 1985), (509, 1945), 
(478, 1865), (481, 1778), (522, 1702), (604, 1677), 
(680, 1717), (670, 1708), (680, 1717), (688, 1709), 
(738, 1653), (746, 1644), (754, 1635), (754, 1626), 
(715, 1594), (635, 1559), (610, 1556), (598, 1555), 
(1055, 1555), (1018, 1558), (935, 1586), (868, 1641), 
(825, 1717), (807, 1802), (809, 1889), (835, 1973), 
(886, 2043), (959, 2090), (1045, 2106), (1131, 2094), 
(1206, 2051), (1224, 2033), (1232, 2024), (1230, 2014), 
(1205, 1986), (1171, 1949), (1163, 1940), (1154, 1938), 
(1146, 1947), (1070, 1985), (989, 1956), (950, 1880), 
(948, 1793), (981, 1713), (1058, 1676), (1138, 1706), 
(1138, 1706), (1147, 1715), (1156, 1712), (1197, 1665), 
(1222, 1637), (1225, 1628), (1216, 1619), (1197, 1603), 
(1120, 1563), (1083, 1556), (1071, 1555), (1528, 1555), 
(1503, 1556), (1419, 1579), (1348, 1629), (1301, 1702), 
(1278, 1787), (1277, 1874), (1298, 1959), (1345, 2032), 
(1415, 2083), (1499, 2105), (1586, 2099), (1664, 2061), 
(1692, 2035), (1700, 2026), (1702, 2016), (1685, 1998), 
(1626, 1935), (1635, 1942), (1626, 1935), (1618, 1944), 
(1555, 1983), (1471, 1966), (1423, 1895), (1416, 1808), 
(1442, 1725), (1512, 1678), (1595, 1697), (1605, 1705), 
(1615, 1713), (1624, 1714), (1657, 1676), (1690, 1639), 
(1697, 1630), (1688, 1621), (1679, 1613), (1604, 1568), 
(1543, 1555), (1531, 1555), (1761, 1576), (1761, 1663), 
(1761, 1751), (1761, 1838), (1761, 1926), (1761, 2013), 
(1765, 2097), (1761, 2088), (1765, 2097), (1778, 2097), 
(1853, 2097), (1890, 2097), (1899, 2093), (1899, 2080), 
(1899, 2055), (1899, 1968), (1899, 1943), (1899, 1930), 
(1905, 1924), (1942, 1924), (2029, 1914), (2106, 1875), 
(2154, 1803), (2163, 1717), (2134, 1635), (2066, 1583), 
(1980, 1565), (1893, 1564), (1805, 1564), (1768, 1564), 
(597, 1577), (609, 1577), (634, 1581), (712, 1620), 
(712, 1620), (721, 1628), (723, 1636), (682, 1683), 
(690, 1674), (682, 1683), (673, 1684), (605, 1655), 
(522, 1675), (469, 1743), (454, 1829), (468, 1915), 
(519, 1984), (602, 2007), (680, 1971), (680, 1971), 
(689, 1968), (697, 1977), (722, 2005), (731, 2014), 
(727, 2023), (655, 2072), (569, 2084), (485, 2063), 
(416, 2011), (373, 1935), (358, 1849), (365, 1762), 
(397, 1681), (456, 1617), (535, 1583), (1092, 1579), 
(1172, 1613), (1182, 1620), (1192, 1628), (1193, 1637), 
(1159, 1674), (1159, 1674), (1151, 1684), (1142, 1683), 
(1086, 1657), (1001, 1669), (943, 1733), (924, 1817), 
(934, 1904), (979, 1977), (1060, 2007), (1141, 1979), 
(1141, 1979), (1150, 1971), (1159, 1969), (1201, 2015), 
(1193, 2006), (1201, 2015), (1197, 2024), (1136, 2067), 
(1051, 2084), (965, 2068), (893, 2019), (847, 1946), 
(828, 1861), (832, 1774), (861, 1691), (916, 1624), 
(994, 1585), (1550, 1578), (1632, 1607), (1652, 1621), 
(1662, 1629), (1662, 1638), (1637, 1666), (1629, 1675), 
(1620, 1684), (1611, 1683), (1567, 1659), (1481, 1664), 
(1418, 1722), (1395, 1806), (1400, 1893), (1441, 1969), 
(1518, 2006), (1601, 1986), (1611, 1978), (1620, 1970), 
(1629, 1969), (1663, 2006), (1663, 2006), (1671, 2015), 
(1666, 2025), (1616, 2062), (1532, 2084), (1446, 2072), 
(1371, 2028), (1321, 1957), (1299, 1872), (1300, 1785), 
(1325, 1702), (1377, 1632), (1452, 1589), (1792, 1586), 
(1880, 1586), (1967, 1586), (2053, 1601), (2121, 1654), 
(2142, 1738), (2122, 1822), (2059, 1880), (1974, 1901), 
(1887, 1902), (1887, 1902), (1877, 1904), (1877, 1917), 
(1877, 1979), (1877, 2067), (1877, 2054), (1877, 2067), 
(1872, 2075), (1797, 2075), (1797, 2075), (1785, 2075), 
(1783, 2064), (1783, 2001), (1783, 1914), (1783, 1826), 
(1783, 1739), (1783, 1651), (1783, 1601), (1783, 1589), 
(1877, 1666), (1877, 1678), (1877, 1766), (1877, 1816), 
(1877, 1828), (1885, 1832), (1898, 1832), (1985, 1828), 
(2047, 1773), (2037, 1688), (1958, 1656), (1896, 1656), 
(1883, 1656), (1904, 1678), (1991, 1684), (2029, 1753), 
(1971, 1808), (1909, 1810), (1899, 1808), (1899, 1795), 
(1899, 1708), (1899, 1678)])




head = points([Point(-2972, 6096), Point(-3007, 6159), Point(-3075, 6148), Point(-3093, 6078), 
	Point(-3045, 6027), Point(-2982, 6059), Point(-2972, 6096)],
	0xe9, 0xe1, 0xd9)

body = points([Point(-3031, 5899), Point(-3036, 5974), Point(-3036, 5974), Point(-3038, 5987), 
	Point(-3050, 5989), Point(-3050, 5989), Point(-3061, 5993), Point(-3055, 5999), 
	Point(-3055, 5977), Point(-3050, 5903), Point(-3056, 5892), Point(-3067, 5886), 
	Point(-3079, 5888), Point(-3103, 5916), Point(-3125, 5987), Point(-3117, 6061), 
	Point(-3061, 6109), Point(-2990, 6132), Point(-2916, 6129), Point(-2856, 6086), 
	Point(-2823, 6020), Point(-2817, 5996), Point(-2818, 5983), Point(-2828, 5980), 
	Point(-2850, 5993), Point(-2869, 6009), Point(-2879, 6016), Point(-2879, 6008), 
	Point(-2868, 5986), Point(-2832, 5920), Point(-2825, 5846), Point(-2831, 5821), 
	Point(-2838, 5811), Point(-2850, 5809), Point(-2868, 5826), Point(-2896, 5895), 
	Point(-2942, 5954), Point(-2942, 5954), Point(-2952, 5960), Point(-2960, 5954), 
	Point(-2957, 5904), Point(-2957, 5829), Point(-2964, 5805), Point(-2972, 5796), 
	Point(-2984, 5799), Point(-3002, 5816), Point(-3029, 5885), Point(-3031, 5899)],
	0xf9, 0xbe, 0x00)


rocket = points([Point(-2882, 5625), Point(-2953, 5649), Point(-3009, 5698), Point(-3048, 5762), 
	Point(-3047, 5835), Point(-2996, 5889), Point(-2944, 5943), Point(-2896, 6001), 
	Point(-2841, 6050), Point(-2768, 6044), Point(-2704, 6005), Point(-2658, 5947), 
	Point(-2635, 5876), Point(-2657, 5808), Point(-2705, 5749), Point(-2756, 5695), 
	Point(-2814, 5647), Point(-2882, 5625)],
	0xe9, 0xe1, 0xd9)

hatch = points([Point(-3031, 5484), Point(-3102, 5507), Point(-3166, 5546), Point(-3220, 5598), 
	Point(-3226, 5670), Point(-3174, 5721), Point(-3138, 5728), Point(-3125, 5728), 
	Point(-3119, 5737), Point(-3114, 5748), Point(-3056, 5791), Point(-2983, 5782), 
	Point(-2924, 5736), Point(-2893, 5669), Point(-2905, 5596), Point(-2965, 5557), 
	Point(-2965, 5557), Point(-2975, 5553), Point(-2978, 5540), Point(-3004, 5499), 
	Point(-3031, 5484)],
	0x5d, 0x31, 0x20)

logo = head + body + rocket + hatch