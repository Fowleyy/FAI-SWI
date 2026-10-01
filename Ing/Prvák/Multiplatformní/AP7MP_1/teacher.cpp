#include "teacher.h"
#include <QDebug>

teacher::teacher(QObject *parent)
    : QObject{parent}
{}

void teacher::goToTheClass()
{
    emit classEntered();
}

void teacher::noticeStudent(QString studentName)
{
    qInfo() << "Stand up " << studentName;
}
