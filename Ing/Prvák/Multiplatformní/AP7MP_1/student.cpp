#include "student.h"
#include <Qdebug>

Student::Student(QString name, QObject *parent)
    : QObject{parent}
{
    m_name = name;
}
void Student::riseMyHand()
{
    emit riseHand(m_name);
}
void Student::Student::seyHello()
{
    qInfo() << "Hello Ms./Mrs. teacher.";
}
