#include "CalibrationRectangle.h"

#include <iostream>
#include <cstdint>

using namespace laser;

CalibrationRectangle::CalibrationRectangle(cv::Point2f topLeft, cv::Point2f bottomLeft, cv::Point2f bottomRight, cv::Point2f topRight)
    : m_topLeft(topLeft), m_bottomLeft(bottomLeft), m_bottomRight(bottomRight), m_topRight(topRight)
{
}

std::vector<etherdream_point> CalibrationRectangle::points()
{
    std::vector<etherdream_point> points;

    float pointsPerLine = 50;

    // topLeft - bottomLeft
    cv::Point2f fromTo(m_bottomLeft.x - m_topLeft.x, m_bottomLeft.y - m_topLeft.y);
    for (int i = 0; i < pointsPerLine; ++i)
    {
        cv::Point2f newPoint(m_topLeft.x + (i/pointsPerLine) * fromTo.x, m_topLeft.y + (i/pointsPerLine) * fromTo.y);
        points.push_back(etherdream_point { newPoint.x, newPoint.y, 0, UINT16_MAX, 0 } );
    }

    // bottomLeft - bottomRight
    fromTo = cv::Point2f(m_bottomRight.x - m_bottomLeft.x, m_bottomRight.y - m_bottomLeft.y);
    for (int i = 0; i < pointsPerLine; ++i)
    {
        cv::Point2f newPoint(m_bottomLeft.x + (i/pointsPerLine) * fromTo.x, m_bottomLeft.y + (i/pointsPerLine) * fromTo.y);
        points.push_back(etherdream_point { newPoint.x, newPoint.y, 0, UINT16_MAX, 0 } );
    }

    // bottomRight - topRight
    fromTo = cv::Point2f(m_topRight.x - m_bottomRight.x, m_topRight.y - m_bottomRight.y);
    for (int i = 0; i < pointsPerLine; ++i)
    {
        cv::Point2f newPoint(m_bottomRight.x + (i/pointsPerLine) * fromTo.x, m_bottomRight.y + (i/pointsPerLine) * fromTo.y);
        points.push_back(etherdream_point { newPoint.x, newPoint.y, 0, UINT16_MAX, 0 } );
    }

    // topRight - topLeft
    fromTo = cv::Point2f(m_topLeft.x - m_topRight.x, m_topLeft.y - m_topRight.y);
    for (int i = 0; i < pointsPerLine; ++i)
    {
        cv::Point2f newPoint(m_topRight.x + (i/pointsPerLine) * fromTo.x, m_topRight.y + (i/pointsPerLine) * fromTo.y);
        points.push_back(etherdream_point { newPoint.x, newPoint.y, 0, UINT16_MAX, 0 } );
    }

    return points;
}

std::vector<cv::Point2f> CalibrationRectangle::corners()
{
    std::vector<cv::Point2f> corners;
    corners.push_back(m_topLeft);
    corners.push_back(m_bottomLeft);
    corners.push_back(m_bottomRight);
    corners.push_back(m_topRight);

    return corners;
}

void CalibrationRectangle::print()
{
    std::cout << "(" << m_topLeft.x << "|" << m_topLeft.y << ") \t" <<
                 "(" << m_topRight.x << "|" << m_topRight.y << ")" << std::endl <<
                 "(" << m_bottomLeft.x << "|" << m_bottomLeft.y << ") \t" <<
                 "(" << m_bottomRight.x << "|" << m_bottomRight.y << ")" << std::endl;
}
