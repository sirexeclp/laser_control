import point
import obj

#max_scale = 6159.
max_scale = 12000
offset = 0 #max_scale / 2

c = lambda v: -int((v - offset) * (2**15 / max_scale))
Point = point.PosPoint

def points(ps, r=0, g=255, b=0):
	return [point.LaserPoint(c(x), c(y), point.col_c(r), point.col_c(g), point.col_c(b), 0, 0, 0) for x, y in ps]

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



"""
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
"""

fairydustb = points([
	Point(1483, 1706), Point(1498, 1658), Point(1512, 1610), Point(1525, 1562), 
	Point(1537, 1514), Point(1549, 1465), Point(1559, 1416), Point(1569, 1367), 
	Point(1578, 1318), Point(1586, 1269), Point(1593, 1219), Point(1599, 1169), 
	Point(1604, 1120), Point(1608, 1070), Point(1611, 1020), Point(1612, 970), 
	Point(1612, 920), Point(1610, 870), Point(1606, 820), Point(1601, 770), 
	Point(1593, 721), Point(1583, 672), Point(1570, 624), Point(1554, 576), 
	Point(1536, 530), Point(1513, 485), Point(1487, 442), Point(1458, 402), 
	Point(1424, 365), Point(1390, 328), Point(1356, 292), Point(1322, 255), 
	Point(1292, 215), Point(1272, 170), Point(1261, 121), Point(1252, 72), 
	Point(1247, 22), Point(1247, 22), Point(1246, 10), Point(1245, 10), 
	Point(1242, 35), Point(1233, 84), Point(1223, 133), Point(1206, 180), 
	Point(1180, 222), Point(1146, 259), Point(1110, 294), Point(1085, 336), 
	Point(1102, 382), Point(1139, 415), Point(1184, 436), Point(1232, 451), 
	Point(1280, 465), Point(1327, 481), Point(1370, 506), Point(1407, 540), 
	Point(1434, 582), Point(1449, 629), Point(1450, 679), Point(1437, 727), 
	Point(1410, 769), Point(1371, 800), Point(1325, 818), Point(1276, 828), 
	Point(1226, 831), Point(1176, 826), Point(1128, 812), Point(1086, 787), 
	Point(1055, 748), Point(1038, 701), Point(1043, 651), Point(1061, 605), 
	Point(1075, 557), Point(1072, 508), Point(1035, 478), Point(990, 496), 
	Point(958, 535), Point(933, 578), Point(914, 624), Point(900, 672), 
	Point(889, 721), Point(880, 770), Point(875, 820), Point(871, 870), 
	Point(869, 920), Point(869, 970), Point(870, 1020), Point(872, 1070), 
	Point(875, 1120), Point(880, 1169), Point(886, 1219), Point(893, 1269), 
	Point(900, 1318), Point(909, 1367), Point(920, 1416), Point(932, 1465), 
	Point(945, 1513), Point(963, 1559), Point(987, 1603), Point(1018, 1643), 
	Point(1054, 1676), Point(1097, 1703), Point(1143, 1721), Point(1192, 1730), 
	Point(1242, 1732), Point(1292, 1724), Point(1338, 1705), Point(1373, 1671), 
	Point(1366, 1624), Point(1323, 1600), Point(1274, 1592), Point(1224, 1594), 
	Point(1175, 1602), Point(1127, 1617), Point(1083, 1640), Point(1043, 1671), 
	Point(1012, 1709), Point(983, 1750), Point(957, 1793), Point(936, 1839), 
	Point(920, 1886), Point(908, 1934), Point(899, 1983), Point(891, 2033), 
	Point(886, 2083), Point(881, 2132), Point(878, 2182), Point(875, 2232), 
	Point(873, 2282), Point(871, 2332), Point(870, 2382), Point(869, 2432), 
	Point(868, 2481), Point(869, 2470), Point(868, 2481), Point(864, 2469), 
	Point(850, 2435), Point(832, 2388), Point(816, 2340), Point(801, 2293), 
	Point(788, 2244), Point(776, 2196), Point(767, 2147), Point(759, 2097), 
	Point(753, 2048), Point(750, 1998), Point(750, 1948), Point(753, 1898), 
	Point(759, 1848), Point(769, 1799), Point(783, 1751), Point(801, 1705), 
	Point(824, 1660), Point(851, 1618), Point(883, 1580), Point(920, 1546), 
	Point(960, 1517), Point(1004, 1492), Point(1050, 1472), Point(1097, 1458), 
	Point(1146, 1448), Point(1196, 1442), Point(1246, 1440), Point(1296, 1442), 
	Point(1345, 1449), Point(1394, 1461), Point(1441, 1477), Point(1486, 1499), 
	Point(1529, 1525), Point(1568, 1556), Point(1604, 1590), Point(1636, 1629), 
	Point(1664, 1670), Point(1688, 1714), Point(1709, 1760), Point(1724, 1807), 
	Point(1736, 1855), Point(1745, 1905), Point(1749, 1955), Point(1750, 2005), 
	Point(1748, 2054), Point(1742, 2104), Point(1733, 2153), Point(1722, 2202), 
	Point(1708, 2250), Point(1691, 2297), Point(1673, 2343), Point(1652, 2389), 
	Point(1628, 2433), Point(1603, 2476), Point(1610, 2466), Point(1603, 2476), 
	Point(1604, 2467), Point(1609, 2430), Point(1614, 2380), Point(1617, 2330), 
	Point(1619, 2280), Point(1620, 2230), Point(1618, 2180), Point(1615, 2130), 
	Point(1609, 2081), Point(1600, 2032), Point(1588, 1983), Point(1571, 1936), 
	Point(1548, 1892), Point(1516, 1853), Point(1476, 1823), Point(1429, 1809), 
	Point(1379, 1809), Point(1337, 1835), Point(1312, 1878), Point(1297, 1925), 
	Point(1286, 1974), Point(1278, 2023), Point(1272, 2073), Point(1267, 2123), 
	Point(1263, 2173), Point(1260, 2223), Point(1257, 2273), Point(1255, 2322), 
	Point(1253, 2372), Point(1250, 2422), Point(1247, 2472), Point(1247, 2472), 
	Point(1247, 2485), Point(1246, 2478), Point(1243, 2453), Point(1239, 2403), 
	Point(1234, 2354), Point(1228, 2304), Point(1221, 2255), Point(1214, 2205), 
	Point(1206, 2156), Point(1197, 2106), Point(1187, 2057), Point(1176, 2009), 
	Point(1163, 1960), Point(1148, 1913), Point(1130, 1866), Point(1105, 1823), 
	Point(1101, 1817)
	],
	0x00, 0x86, 0xf2)

fairydust = fairydustb


fairydusty = points([
Point(1785, 1700), Point(1774, 1787), Point(1763, 1874), Point(1752, 1961), 
	Point(1741, 2048), Point(1730, 2134), Point(1720, 2221), Point(1709, 2308), 
	Point(1698, 2395), Point(1687, 2474), Point(1688, 2469), Point(1687, 2474), 
	Point(1684, 2461), Point(1670, 2388), Point(1653, 2302), Point(1636, 2216), 
	Point(1619, 2130), Point(1602, 2044), Point(1632, 1966), Point(1675, 1890), 
	Point(1719, 1815), Point(1763, 1739), Point(1775, 1717), Point(1782, 1706), 
	Point(1407, 1719), Point(1420, 1684), Point(1452, 1603), Point(1484, 1521), 
	Point(1516, 1440), Point(1548, 1360), Point(1543, 1370), Point(1548, 1360), 
	Point(1549, 1372), Point(1554, 1447), Point(1561, 1534), Point(1568, 1621), 
	Point(1574, 1709), Point(1581, 1796), Point(1588, 1883), Point(1594, 1970), 
	Point(1597, 2008), Point(1598, 2020), Point(1594, 2019), Point(1581, 1998), 
	Point(1533, 1924), Point(1486, 1850), Point(1438, 1777), Point(1418, 1745), 
	Point(1411, 1735), Point(1095, 1725), Point(1082, 1746), Point(1034, 1819), 
	Point(987, 1893), Point(939, 1966), Point(912, 2008), Point(905, 2019), 
	Point(902, 2020), Point(903, 2007), Point(910, 1920), Point(916, 1833), 
	Point(923, 1746), Point(930, 1658), Point(936, 1571), Point(943, 1484), 
	Point(950, 1397), Point(951, 1372), Point(952, 1359), Point(957, 1371), 
	Point(971, 1405), Point(1002, 1487), Point(1034, 1568), Point(1066, 1650), 
	Point(1089, 1708), Point(1093, 1720), Point(900, 2032), Point(881, 2117), 
	Point(863, 2203), Point(844, 2288), Point(825, 2374), Point(807, 2459), 
	Point(807, 2459), Point(804, 2471), Point(802, 2472), Point(795, 2410), 
	Point(785, 2323), Point(775, 2236), Point(766, 2149), Point(756, 2062), 
	Point(746, 1975), Point(736, 1888), Point(726, 1801), Point(716, 1714), 
	Point(716, 1714), Point(715, 1702), Point(720, 1710), Point(752, 1764), 
	Point(795, 1840), Point(839, 1916), Point(883, 1992), Point(901, 2024), 
	Point(1247, 2466), Point(1245, 2454), Point(1240, 2429), Point(1222, 2344), 
	Point(1205, 2258), Point(1187, 2172), Point(1169, 2086), Point(1152, 2001), 
	Point(1134, 1915), Point(1117, 1829), Point(1099, 1744), Point(1119, 1661), 
	Point(1150, 1579), Point(1181, 1497), Point(1212, 1415), Point(1243, 1334), 
	Point(1243, 1334), Point(1248, 1322), Point(1248, 1334), Point(1248, 1396), 
	Point(1248, 1484), Point(1248, 1571), Point(1249, 1659), Point(1249, 1746), 
	Point(1249, 1834), Point(1249, 1921), Point(1249, 2009), Point(1249, 2096), 
	Point(1249, 2184), Point(1249, 2271), Point(1250, 2359), Point(1250, 2446), 
	Point(1250, 2459), Point(1250, 2471), Point(1646, 481), Point(1599, 497), 
	Point(1521, 529), Point(1528, 522), Point(1521, 529), Point(1521, 542), 
	Point(1523, 617), Point(1526, 704), Point(1529, 792), Point(1532, 879), 
	Point(1535, 967), Point(1537, 1054), Point(1540, 1142), Point(1543, 1229), 
	Point(1546, 1316), Point(1547, 1341), Point(1547, 1354), Point(1548, 1351), 
	Point(1552, 1314), Point(1563, 1227), Point(1573, 1140), Point(1583, 1053), 
	Point(1594, 966), Point(1604, 879), Point(1614, 793), Point(1624, 706), 
	Point(1635, 619), Point(1645, 532), Point(1649, 495), Point(1651, 482), 
	Point(854, 472), Point(871, 454), Point(928, 388), Point(986, 322), 
	Point(1044, 256), Point(1102, 191), Point(1160, 125), Point(1217, 59), 
	Point(1242, 31), Point(1250, 23), Point(1250, 35), Point(1250, 60), 
	Point(1250, 148), Point(1250, 235), Point(1248, 322), Point(1250, 310), 
	Point(1248, 322), Point(1236, 326), Point(1166, 354), Point(1085, 386), 
	Point(1004, 418), Point(922, 450), Point(864, 473), Point(852, 478), 
	Point(1515, 530), Point(1446, 584), Point(1377, 637), Point(1308, 691), 
	Point(1259, 730), Point(1250, 738), Point(1250, 751), Point(1250, 838), 
	Point(1249, 926), Point(1249, 1013), Point(1249, 1101), Point(1249, 1188), 
	Point(1248, 1276), Point(1248, 1313), Point(1250, 1318), Point(1254, 1306), 
	Point(1262, 1282), Point(1290, 1200), Point(1318, 1117), Point(1347, 1034), 
	Point(1375, 951), Point(1403, 868), Point(1432, 786), Point(1460, 703), 
	Point(1488, 620), Point(1517, 537), Point(1517, 537), Point(1521, 525), 
	Point(1248, 1309), Point(1248, 1247), Point(1248, 1159), Point(1249, 1072), 
	Point(1249, 984), Point(1249, 897), Point(1249, 809), Point(1250, 747), 
	Point(1248, 735), Point(1238, 727), Point(1169, 674), Point(1100, 620), 
	Point(1031, 566), Point(992, 535), Point(982, 528), Point(981, 533), 
	Point(985, 545), Point(1013, 628), Point(1042, 711), Point(1070, 794), 
	Point(1098, 877), Point(1126, 959), Point(1154, 1042), Point(1182, 1125), 
	Point(1210, 1208), Point(1238, 1291), Point(1242, 1303), Point(1246, 1315), 
	Point(849, 484), Point(855, 534), Point(865, 621), Point(875, 708), 
	Point(885, 795), Point(896, 882), Point(906, 969), Point(916, 1055), 
	Point(927, 1142), Point(937, 1229), Point(947, 1316), Point(950, 1341), 
	Point(952, 1353), Point(952, 1353), Point(954, 1315), Point(956, 1228), 
	Point(959, 1140), Point(962, 1053), Point(965, 966), Point(968, 878), 
	Point(970, 791), Point(973, 703), Point(976, 616), Point(979, 528), 
	Point(978, 541), Point(979, 528), Point(970, 522), Point(899, 497), 
	Point(864, 485), Point(852, 480), Point(1250, 31), Point(1250, 56), 
	Point(1250, 143), Point(1250, 231), Point(1250, 318), Point(1250, 306), 
	Point(1250, 318), Point(1259, 324), Point(1329, 352), Point(1410, 384), 
	Point(1491, 416), Point(1573, 449), Point(1650, 478), Point(1642, 476), 
	Point(1650, 478), Point(1641, 468), Point(1592, 412), Point(1534, 346), 
	Point(1476, 280), Point(1419, 215), Point(1361, 149), Point(1303, 83), 
	Point(1262, 36), Point(1254, 27), Point(854, 481), Point(937, 510), 
	Point(972, 523), Point(983, 522), Point(993, 515), Point(1013, 499), 
	Point(1083, 447), Point(1153, 394), Point(1222, 341), Point(1242, 326), 
	Point(1247, 321), Point(1235, 326), Point(1200, 340), Point(1119, 372), 
	Point(1038, 404), Point(956, 436), Point(875, 469), Point(863, 473), 
	Point(852, 478), Point(1643, 482), Point(1596, 498), Point(1537, 519), 
	Point(1525, 523), Point(1514, 520), Point(1445, 467), Point(1375, 415), 
	Point(1305, 362), Point(1265, 332), Point(1255, 324), Point(1255, 322), 
	Point(1267, 327), Point(1348, 359), Point(1429, 391), Point(1511, 423), 
	Point(1592, 456), Point(1638, 474), Point(1650, 479), Point(1537, 1358), 
	Point(1524, 1356), Point(1437, 1345), Point(1351, 1335), Point(1264, 1324), 
	Point(1264, 1324), Point(1251, 1322), Point(1252, 1313), Point(1272, 1253), 
	Point(1300, 1171), Point(1329, 1088), Point(1357, 1005), Point(1385, 922), 
	Point(1414, 839), Point(1442, 757), Point(1470, 674), Point(1499, 591), 
	Point(1515, 544), Point(1519, 532), Point(1521, 530), Point(1522, 543), 
	Point(1525, 630), Point(1527, 718), Point(1530, 805), Point(1533, 892), 
	Point(1536, 980), Point(1538, 1067), Point(1541, 1155), Point(1544, 1242), 
	Point(1547, 1330), Point(1547, 1342), Point(1548, 1355), Point(1240, 1322), 
	Point(1191, 1329), Point(1104, 1340), Point(1017, 1351), Point(967, 1357), 
	Point(955, 1359), Point(952, 1349), Point(953, 1337), Point(956, 1249), 
	Point(958, 1162), Point(961, 1075), Point(964, 987), Point(967, 900), 
	Point(970, 812), Point(972, 725), Point(975, 637), Point(978, 550), 
	Point(978, 537), Point(979, 526), Point(983, 537), Point(999, 585), 
	Point(1027, 668), Point(1055, 751), Point(1083, 833), Point(1111, 916), 
	Point(1139, 999), Point(1167, 1082), Point(1195, 1165), Point(1223, 1248), 
	Point(1252, 2468), Point(1247, 1319), Point(1252, 2468), Point(1254, 2456), 
	Point(1269, 2382), Point(1287, 2297), Point(1304, 2211), Point(1322, 2125), 
	Point(1340, 2040), Point(1357, 1954), Point(1375, 1868), Point(1392, 1782), 
	Point(1394, 1698), Point(1362, 1616), Point(1331, 1535), Point(1299, 1453), 
	Point(1267, 1372), Point(1254, 1337), Point(1249, 1325), Point(1248, 1330), 
	Point(1248, 1355), Point(1248, 1443), Point(1248, 1530), Point(1248, 1618), 
	Point(1249, 1705), Point(1249, 1793), Point(1249, 1880), Point(1249, 1968), 
	Point(1249, 2055), Point(1249, 2143), Point(1249, 2230), Point(1249, 2318), 
	Point(1250, 2405), Point(1250, 2455), Point(1250, 2468), Point(1600, 2023), 
	Point(1606, 2012), Point(1650, 1936), Point(1693, 1860), Point(1737, 1784), 
	Point(1781, 1708), Point(1781, 1708), Point(1784, 1698), Point(1776, 1687), 
	Point(1741, 1636), Point(1691, 1564), Point(1641, 1492), Point(1591, 1420), 
	Point(1555, 1369), Point(1548, 1359), Point(1549, 1371), Point(1556, 1458), 
	Point(1562, 1546), Point(1569, 1633), Point(1575, 1720), Point(1582, 1807), 
	Point(1589, 1895), Point(1595, 1982), Point(1597, 2007), Point(1598, 2019), 
	Point(902, 2018), Point(905, 1980), Point(912, 1893), Point(918, 1806), 
	Point(925, 1719), Point(932, 1631), Point(938, 1544), Point(945, 1457), 
	Point(952, 1370), Point(952, 1370), Point(951, 1360), Point(944, 1370), 
	Point(909, 1422), Point(859, 1494), Point(809, 1565), Point(759, 1637), 
	Point(723, 1689), Point(716, 1699), Point(721, 1710), Point(764, 1786), 
	Point(808, 1861), Point(851, 1937), Point(895, 2013), Point(901, 2025)
	],
	0xff, 0x76, 0x00)

fairydustg = points([
	Point(1400, 2052), Point(1426, 2095), Point(1452, 2138), Point(1480, 2180), 
	Point(1508, 2221), Point(1538, 2261), Point(1568, 2300), Point(1600, 2339), 
	Point(1633, 2376), Point(1668, 2412), Point(1704, 2447), Point(1743, 2479), 
	Point(1743, 2479), Point(1752, 2487), Point(1756, 2477), Point(1760, 2453), 
	Point(1767, 2403), Point(1773, 2353), Point(1776, 2304), Point(1778, 2254), 
	Point(1777, 2204), Point(1774, 2154), Point(1770, 2104), Point(1763, 2054), 
	Point(1753, 2005), Point(1742, 1957), Point(1728, 1908), Point(1713, 1861), 
	Point(1695, 1814), Point(1675, 1768), Point(1654, 1723), Point(1630, 1679), 
	Point(1605, 1636), Point(1578, 1594), Point(1550, 1552), Point(1557, 1562), 
	Point(1550, 1552), Point(1093, 2094), Point(1074, 2126), Point(1047, 2168), 
	Point(1018, 2210), Point(989, 2250), Point(957, 2289), Point(925, 2327), 
	Point(891, 2363), Point(855, 2398), Point(818, 2432), Point(780, 2464), 
	Point(760, 2480), Point(750, 2487), Point(747, 2477), Point(739, 2428), 
	Point(732, 2378), Point(727, 2329), Point(724, 2279), Point(722, 2229), 
	Point(723, 2179), Point(726, 2129), Point(730, 2079), Point(737, 2030), 
	Point(746, 1980), Point(758, 1932), Point(771, 1884), Point(787, 1836), 
	Point(805, 1790), Point(825, 1744), Point(847, 1699), Point(871, 1655), 
	Point(897, 1612), Point(924, 1570), Point(939, 1550), Point(1250, 298), 
	Point(1240, 305), Point(1199, 334), Point(1160, 365), Point(1123, 399), 
	Point(1089, 436), Point(1058, 475), Point(1029, 516), Point(1004, 559), 
	Point(981, 603), Point(961, 649), Point(944, 696), Point(930, 744), 
	Point(918, 793), Point(908, 842), Point(901, 891), Point(895, 941), 
	Point(892, 991), Point(890, 1041), Point(889, 1091), Point(891, 1141), 
	Point(893, 1191), Point(897, 1241), Point(902, 1290), Point(907, 1340), 
	Point(914, 1390), Point(922, 1439), Point(931, 1488), Point(940, 1537), 
	Point(951, 1586), Point(962, 1635), Point(973, 1684), Point(986, 1732), 
	Point(999, 1780), Point(1012, 1828), Point(1026, 1877), Point(1040, 1924), 
	Point(1055, 1972), Point(1071, 2020), Point(1087, 2067), Point(1103, 2114), 
	Point(1120, 2161), Point(1137, 2208), Point(1154, 2255), Point(1172, 2302), 
	Point(1190, 2349), Point(1208, 2395), Point(1227, 2442), Point(1246, 2488), 
	Point(1241, 2476), Point(1246, 2488), Point(1250, 2476), Point(1263, 2441), 
	Point(1280, 2394), Point(1297, 2347), Point(1314, 2300), Point(1331, 2253), 
	Point(1348, 2206), Point(1364, 2158), Point(1380, 2111), Point(1396, 2064), 
	Point(1412, 2016), Point(1428, 1969), Point(1443, 1921), Point(1458, 1873), 
	Point(1472, 1825), Point(1486, 1777), Point(1499, 1729), Point(1512, 1681), 
	Point(1525, 1633), Point(1536, 1584), Point(1547, 1535), Point(1557, 1486), 
	Point(1567, 1437), Point(1575, 1388), Point(1583, 1338), Point(1589, 1289), 
	Point(1594, 1239), Point(1598, 1189), Point(1601, 1139), Point(1602, 1089), 
	Point(1602, 1039), Point(1599, 989), Point(1595, 939), Point(1589, 890), 
	Point(1581, 841), Point(1570, 792), Point(1558, 743), Point(1542, 696), 
	Point(1524, 649), Point(1504, 603), Point(1481, 559), Point(1455, 516), 
	Point(1427, 475), Point(1397, 435), Point(1364, 397), Point(1330, 361), 
	Point(1293, 327), Point(1275, 310), Point(1265, 302), Point(1170, 13), 
	Point(1191, 58), Point(1210, 104), Point(1225, 152), Point(1239, 200), 
	Point(1250, 249), Point(1258, 298), Point(1264, 348), Point(1268, 398), 
	Point(1270, 448), Point(1269, 498), Point(1267, 548), Point(1264, 597), 
	Point(1258, 647), Point(1251, 697), Point(1243, 746), Point(1233, 795), 
	Point(1223, 844), Point(1210, 892), Point(1199, 941), Point(1190, 990), 
	Point(1183, 1040), Point(1179, 1089), Point(1177, 1139), Point(1177, 1189), 
	Point(1179, 1239), Point(1183, 1289), Point(1189, 1339), Point(1197, 1388), 
	Point(1207, 1437), Point(1218, 1486), Point(1231, 1534), Point(1245, 1582), 
	Point(1262, 1629), Point(1281, 1676), Point(1284, 1684)
	],
	0x99, 0xba, 0x00)
