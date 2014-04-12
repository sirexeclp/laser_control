#include "Calibration.h"
#include "../Config.h"

#include <opencv/highgui.h>
#include <opencv2/calib3d/calib3d.hpp>

#include <vector>
#include <cstdint>
#include <iostream>

using namespace laser;

Calibration::Calibration(EtherdreamWrapperPtr wrapper)
	: m_scale(100),
	  m_yScale(100),
	  m_keystoneFactor(100),
	  m_etherdream(wrapper),
	  m_homography(0, 0, CV_8UC1, nullptr)
{
	;;
}

bool Calibration::alreadyCalibrated()
{
	cv::FileStorage fs("calibration.yml", cv::FileStorage::READ);

	if (!fs.isOpened())
		return false;

	fs["homography"] >> m_homography;
	std::cout << "Found calibration.yml file. Skipping calibration." << std::endl;
	return true;
}

void Calibration::start()
{
	if (!config::forceRecalibration && alreadyCalibrated())
		return;

	void (*callback)(int, void *) = [](int, void *t){static_cast<Calibration *>(t)->repaint();};

	cv::namedWindow("Calibration");
	cv::createTrackbar("Scale", "Calibration", &m_scale, 100, callback, (void*)this);
	cv::createTrackbar("y-Scale", "Calibration", &m_yScale, 100, callback, (void*)this);
	cv::createTrackbar("Keystone", "Calibration", &m_keystoneFactor, 100, callback, (void*)this);

	repaint();
	cv::waitKey();
	cv::destroyWindow("Calibration");

	computeHomography();

	cv::FileStorage fs1("calibration.yml", cv::FileStorage::WRITE);
	fs1 << "homography" << m_homography;

}

void Calibration::repaint()
{
	m_rect.resetTransform();
	m_rect.scale(m_scale / 100.0);
	m_rect.scale(1.0, m_yScale / 100.0);
	m_rect.setKeystoneFactor(m_keystoneFactor / 100.0);

	m_etherdream->setPoints(m_rect.pointsToPaint());
	m_etherdream->writePoints();
}

cv::Mat Calibration::homography()
{
	if (m_homography.empty())
		computeHomography();

	return m_homography;
}

void Calibration::computeHomography()
{
	std::vector<cv::Point2f> dst = m_rect.corners();
	std::vector<cv::Point2f> src;
	for (const auto & p: m_rect.undistoredCorners())
		src.emplace_back(p.x(), p.y());

	m_homography = cv::findHomography(src, dst);
}
