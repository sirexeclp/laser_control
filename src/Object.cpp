#include "Object.h"
#include "Transform.h"
#include "CompositeObject.h"

#include <boost/date_time.hpp>

#include <opencv2/imgproc/imgproc.hpp>
#include <assert.h>

laser::Object::Object()
	: m_started(boost::date_time::microsec_clock<boost::posix_time::ptime>::universal_time()),
	  m_isUpdating(false),
	  m_isVisible(true)
{
	resetTransform();
}

/**** For scene graph structure with CompositeObject ****/

laser::Object::parent_t laser::Object::parent() const
{
	return m_parent.lock();
}

void laser::Object::setParent(const parent_t & newParent)
{
	if (parent_t oldParent = parent()) {
		oldParent->removeChild(this);
	}
	m_parent = newParent;
}

void laser::Object::rebuildCache()
{
	if (m_isUpdating)
		return;

	m_isUpdating = true;

	m_cache.clear();

	appendToVector(m_cache, startPoints());
	appendToVector(m_cache, points());
	appendToVector(m_cache, endPoints());

	Transform::applyInPlace(m_cache, cv::transform, m_transform(cv::Rect(0, 0, 3, 2)));

	// Now I'm rebuild and I prevent my parent from calling
	// this function
	m_dirty = false;
	if (parent_t myParent = parent()) {
		myParent->rebuildCache();
	}
	m_isUpdating = false;
}

laser::EtherdreamPoints laser::Object::pointsToPaint()
{
	if (!m_isVisible)
		return EtherdreamPoints();

	if (m_dirty)
		rebuildCache();

	return m_cache;
}

/**** Transform ***/

void laser::Object::rotate(double rad)
{
	// Counter clockwise rotation about rad
	double s = std::sin(rad);
	double c = std::cos(rad);
	double m[3][3] = {{c, -s, 0}, {s, c, 0}, {0, 0, 1}};
	m_transform = cv::Mat(3, 3, CV_64FC1, m) * m_transform;
	nowDirty();
}

void laser::Object::rotate(double rad, int centerX, int centerY, double scale)
{
	// TODO: Look up right matrix
	move(-centerX, -centerY);
	rotate(rad);
	move(centerX, centerY);
	if (scale != 1) this->scale(scale);
}

void laser::Object::move(int x, int y)
{
	double m[3][3] = {{1, 0, (double) x}, {0, 1, (double) y}, {0, 0, 1}};
	m_transform = cv::Mat(3, 3, CV_64FC1, m) * m_transform;
	nowDirty();
}

void laser::Object::scale(double factorX, double factorY)
{
	double m[3][3] = {{factorX, 0, 0}, {0, factorY, 0}, {0, 0, 1}};
	m_transform = cv::Mat(3, 3, CV_64FC1, m) * m_transform;
	nowDirty();
}

void laser::Object::scale(double factor)
{
	scale(factor, factor);
}

void laser::Object::resetTransform()
{
	m_transform = cv::Mat::eye(3, 3, CV_64FC1);
	nowDirty();
}

void laser::Object::setAnimation(Animation animation)
{
	m_animation = animation;
}

void laser::Object::setVisible(bool visible)
{
	m_isVisible = visible;
}

bool laser::Object::visible()
{
	return m_isVisible;
}

void laser::Object::tick()
{
	if (m_animation)
		m_animation();
}

/**** Other ****/

boost::posix_time::ptime laser::Object::started() const
{
	return m_started;
}

void laser::Object::setPermanent(bool permanent)
{
	m_permanent = permanent;
}

bool laser::Object::permanent() const
{
	return m_permanent;
}
