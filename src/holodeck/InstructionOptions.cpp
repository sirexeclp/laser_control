#include "InstructionOptions.h"
#include "../objects/CompositeObject.h"
#include "../objects/Line.h"
#include "../objects/GenObject.h"

namespace laser { namespace holodeck { namespace opts {

#define LASER_HOLODECK_OPTS_FULL (3000.0)
#define LASER_HOLODECK_OPTS_HALF (LASER_HOLODECK_OPTS_FULL / 2)
#define LASER_HOLODECK_OPTS_QURT (LASER_HOLODECK_OPTS_FULL / 4)

#define HANDCRAFTED 1

static void moveObjectFromNSpaceToOptsSpace(ObjectPtr & obj)
{
	const double nSpace = 2500.0;
	obj->move(-nSpace * 0.5, -nSpace * 0.5);
	obj->flipVertically();
	obj->scale(1.5 * LASER_HOLODECK_OPTS_FULL / nSpace);
	obj->move(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF);
}

static CompositeObjectPtr getZero()
{
	/*
	 * r-----q
	 * |=====|
	 * |I   I|
	 * |I   I|
	 * |I   I|
	 * |=====|
	 * L-----J
	 */
	CompositeObjectPtr group = CompositeObject::construct();
#if HANDCRAFTED
	ObjectPtr obj(new GenObject{Point(1255, 394), Point(1482, 453), Point(1630, 634), Point(1690, 863),
								Point(1711, 1100), Point(1717, 1337), Point(1702, 1574), Point(1648, 1805),
								Point(1523, 2004), Point(1311, 2102), Point(1078, 2073), Point(905, 1916),
								Point(821, 1695), Point(789, 1460), Point(783, 1222), Point(798, 985),
								Point(843, 753), Point(945, 540), Point(1137, 407), Point(1255, 394)});
	moveObjectFromNSpaceToOptsSpace(obj);
	group->add(obj);
#else
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_FULL), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL), Point(LASER_HOLODECK_OPTS_HALF, 0)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, 0), Point(0, 0)));
	group->add(std::make_shared<Line>(Point(0, 0), Point(0, LASER_HOLODECK_OPTS_FULL)));
#endif
	return group;
}

static CompositeObjectPtr getOne()
{
	/*
	 * r-----q
	 * |    I|
	 * |    I|
	 * |    I|
	 * |    I|
	 * |    I|
	 * L-----J
	 */
	CompositeObjectPtr group = CompositeObject::construct();
#if HANDCRAFTED
	ObjectPtr obj(new GenObject({Point(975, 581), Point(1202, 513), Point(1428, 440), Point(1511, 411),
								 Point(1523, 407), Point(1525, 416), Point(1525, 541), Point(1524, 778),
								 Point(1524, 1016), Point(1524, 1253), Point(1523, 1491), Point(1523, 1728),
								 Point(1522, 1966), Point(1522, 2094)}));
	moveObjectFromNSpaceToOptsSpace(obj);
	group->add(obj);
#else
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, 0), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL)));
#endif
	return group;
}

static CompositeObjectPtr getTwo()
{
	/*
	 * r-----q
	 * |=====|
	 * |    I|
	 * |=====|
	 * |I    |
	 * |=====|
	 * L-----J
	 */
	CompositeObjectPtr group = CompositeObject::construct();
#if HANDCRAFTED
	ObjectPtr obj(new GenObject({Point(1765, 2095), Point(1527, 2094), Point(1290, 2094), Point(1052, 2093),
								 Point(815, 2093), Point(752, 2093), Point(740, 2093), Point(741, 2087),
								 Point(845, 1979), Point(1009, 1807), Point(1168, 1631), Point(1319, 1447),
								 Point(1453, 1252), Point(1553, 1037), Point(1588, 803), Point(1526, 577),
								 Point(1344, 431), Point(1110, 412), Point(887, 492), Point(788, 567)}));
	moveObjectFromNSpaceToOptsSpace(obj);
	group->add(obj);
#else
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_FULL), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF), Point(0, LASER_HOLODECK_OPTS_HALF)));
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_HALF), Point(0, 0)));
	group->add(std::make_shared<Line>(Point(0, 0), Point(LASER_HOLODECK_OPTS_HALF, 0)));
#endif
	return group;
}

static CompositeObjectPtr getThree()
{
	/*
	 * r-----q
	 * |=====|
	 * |    I|
	 * |=====|
	 * |    I|
	 * |=====|
	 * L-----J
	 */
	CompositeObjectPtr group = CompositeObject::construct();
#if HANDCRAFTED
	ObjectPtr obj(new GenObject({Point(891, 491), Point(1116, 415), Point(1352, 407), Point(1549, 528),
								 Point(1587, 755), Point(1463, 954), Point(1257, 1068), Point(1110, 1100),
								 Point(1103, 1100), Point(1115, 1099), Point(1178, 1093), Point(1410, 1128),
								 Point(1598, 1269), Point(1684, 1487), Point(1644, 1718), Point(1499, 1904),
								 Point(1295, 2022), Point(1065, 2083), Point(829, 2101), Point(814, 2101)}));
	moveObjectFromNSpaceToOptsSpace(obj);
	group->add(obj);
#else
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_FULL), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL), Point(LASER_HOLODECK_OPTS_HALF, 0)));
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_HALF), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF)));
	group->add(std::make_shared<Line>(Point(0, 0), Point(LASER_HOLODECK_OPTS_HALF, 0)));
#endif
	return group;
}

static CompositeObjectPtr getFour()
{
	/*
	 * r-----q
	 * |I   I|
	 * |I   I|
	 * |=====|
	 * |    I|
	 * |    I|
	 * L-----J
	 */
	CompositeObjectPtr group = CompositeObject::construct();
#if HANDCRAFTED
	ObjectPtr obj(new GenObject({Point(1792, 1555), Point(1554, 1555), Point(1317, 1556), Point(1079, 1556),
								 Point(842, 1557), Point(729, 1557), Point(717, 1557), Point(711, 1553),
								 Point(765, 1469), Point(892, 1269), Point(1021, 1069), Point(1152, 871),
								 Point(1285, 675), Point(1426, 483), Point(1489, 405), Point(1497, 396),
								 Point(1501, 398), Point(1497, 510), Point(1491, 748), Point(1485, 985),
								 Point(1480, 1223), Point(1477, 1460), Point(1475, 1698), Point(1477, 1935),
								 Point(1479, 2109)}));
	moveObjectFromNSpaceToOptsSpace(obj);
	group->add(obj);
#else
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_FULL), Point(0, LASER_HOLODECK_OPTS_HALF)));
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_HALF), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL), Point(LASER_HOLODECK_OPTS_HALF, 0)));
#endif
	return group;
}

static CompositeObjectPtr getFive()
{
	CompositeObjectPtr group = CompositeObject::construct();
#if HANDCRAFTED
	ObjectPtr obj(new GenObject({Point(1713, 408), Point(1476, 415), Point(1238, 421), Point(1001, 427),
								 Point(1013, 427), Point(1001, 427), Point(997, 436), Point(989, 661),
								 Point(981, 898), Point(972, 1136), Point(971, 1173), Point(971, 1185),
								 Point(978, 1185), Point(1136, 1112), Point(1371, 1095), Point(1574, 1210),
								 Point(1671, 1423), Point(1664, 1658), Point(1561, 1870), Point(1377, 2018),
								 Point(1150, 2085), Point(913, 2083), Point(787, 2059)}));
	moveObjectFromNSpaceToOptsSpace(obj);
	group->add(obj);
#else
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL), Point(0, LASER_HOLODECK_OPTS_FULL)));
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_FULL), Point(0, LASER_HOLODECK_OPTS_HALF)));
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_HALF), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF), Point(LASER_HOLODECK_OPTS_HALF, 0)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, 0), Point(0, 0)));
#endif
	return group;
}

static CompositeObjectPtr getSix()
{
	CompositeObjectPtr group = CompositeObject::construct();
#if HANDCRAFTED
	ObjectPtr obj(new GenObject({Point(1598, 397), Point(1363, 428), Point(1154, 539), Point(994, 713),
								 Point(885, 923), Point(820, 1151), Point(792, 1387), Point(795, 1624),
								 Point(845, 1855), Point(989, 2039), Point(1215, 2102), Point(1447, 2062),
								 Point(1624, 1909), Point(1703, 1687), Point(1699, 1450), Point(1589, 1244),
								 Point(1380, 1139), Point(1145, 1152), Point(942, 1271), Point(819, 1472),
								 Point(798, 1564)}));
	moveObjectFromNSpaceToOptsSpace(obj);
	group->add(obj);
#else
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL), Point(0, LASER_HOLODECK_OPTS_FULL)));
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_FULL), Point(0, 0)));
	group->add(std::make_shared<Line>(Point(0, 0), Point(LASER_HOLODECK_OPTS_HALF, 0)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, 0), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF), Point(0, LASER_HOLODECK_OPTS_HALF)));
#endif
	return group;
}

static CompositeObjectPtr getSeven()
{
	CompositeObjectPtr group = CompositeObject::construct();
#if HANDCRAFTED
	ObjectPtr obj(new GenObject({Point(802, 395), Point(1038, 419), Point(1275, 425), Point(1513, 419),
								 Point(1687, 406), Point(1698, 406), Point(1692, 418), Point(1675, 451),
								 Point(1567, 662), Point(1457, 873), Point(1347, 1083), Point(1239, 1295),
								 Point(1137, 1509), Point(1044, 1728), Point(967, 1953), Point(931, 2105)}));
	moveObjectFromNSpaceToOptsSpace(obj);
	group->add(obj);
#else
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_FULL), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL), Point(LASER_HOLODECK_OPTS_HALF, 0)));
#endif
	return group;
}

static CompositeObjectPtr getEight()
{
	CompositeObjectPtr group = CompositeObject::construct();
#if HANDCRAFTED
	ObjectPtr obj(new GenObject({Point(1248, 1191), Point(1469, 1111), Point(1618, 931), Point(1638, 698),
								 Point(1520, 497), Point(1302, 411), Point(1071, 452), Point(901, 612),
								 Point(859, 842), Point(950, 1058), Point(1150, 1178), Point(1385, 1212),
								 Point(1594, 1318), Point(1699, 1526), Point(1688, 1762), Point(1574, 1968),
								 Point(1368, 2079), Point(1133, 2078), Point(922, 1974), Point(809, 1770),
								 Point(803, 1534), Point(912, 1327), Point(1118, 1213), Point(1248, 1191)}));

	moveObjectFromNSpaceToOptsSpace(obj);
	group->add(obj);
#else
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_HALF), Point(0, LASER_HOLODECK_OPTS_FULL)));
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_FULL), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF), Point(0, LASER_HOLODECK_OPTS_HALF)));
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_HALF), Point(0, 0)));
	group->add(std::make_shared<Line>(Point(0, 0), Point(LASER_HOLODECK_OPTS_HALF, 0)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, 0), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF)));
#endif
	return group;
}

static CompositeObjectPtr getNine()
{
	CompositeObjectPtr group = CompositeObject::construct();
#if HANDCRAFTED
	ObjectPtr obj(new GenObject({Point(891, 2102), Point(1125, 2072), Point(1336, 1964), Point(1503, 1797),
								 Point(1618, 1590), Point(1683, 1362), Point(1710, 1126), Point(1708, 889),
								 Point(1667, 656), Point(1526, 470), Point(1301, 399), Point(1068, 428),
								 Point(887, 576), Point(798, 794), Point(801, 1030), Point(905, 1240),
								 Point(1109, 1352), Point(1345, 1350), Point(1552, 1238), Point(1680, 1041),
								 Point(1708, 893)}));
	moveObjectFromNSpaceToOptsSpace(obj);
	group->add(obj);
#else
	group->add(std::make_shared<Line>(Point(0, 0), Point(LASER_HOLODECK_OPTS_HALF, 0)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, 0), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL)));
	group->add(std::make_shared<Line>(Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_FULL), Point(0, LASER_HOLODECK_OPTS_FULL)));
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_FULL), Point(0, LASER_HOLODECK_OPTS_HALF)));
	group->add(std::make_shared<Line>(Point(0, LASER_HOLODECK_OPTS_HALF), Point(LASER_HOLODECK_OPTS_HALF, LASER_HOLODECK_OPTS_HALF)));
#endif
	return group;
}

CompositeObjectPtr getDigit(int digit)
{
	switch (digit) {
	case 0:
		return getZero();
		break;
	case 1:
		return getOne();
		break;
	case 2:
		return getTwo();
		break;
	case 3:
		return getThree();
		break;
	case 4:
		return getFour();
		break;
	case 5:
		return getFive();
		break;
	case 6:
		return getSix();
		break;
	case 7:
		return getSeven();
		break;
	case 8:
		return getEight();
		break;
	case 9:
		return getNine();
		break;
	default:
		return CompositeObject::construct();
		break;
	}
}

}}}