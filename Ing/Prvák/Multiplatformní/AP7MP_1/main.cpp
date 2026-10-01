#include <QCoreApplication>
#include <Qdebug>
#include "student.h"
#include "teacher.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    qInfo() << "Hello world";

    teacher te1;
    Student st1("Franta");
    Student st2("Pepa");
    Student st3("Anežka");

    QObject::connect(&te1, &teacher::classEntered, &st1, &Student::seyHello);
    QObject::connect(&te1, &teacher::classEntered, &st2, &Student::seyHello);
    QObject::connect(&te1, &teacher::classEntered, &st3, &Student::seyHello);
    QObject::connect(&st1, &Student::riseHand, &te1, &teacher::noticeStudent);
    QObject::connect(&st2, &Student::riseHand, &te1, &teacher::noticeStudent);
    QObject::connect(&st3, &Student::riseHand, &te1, &teacher::noticeStudent);

    te1.goToTheClass();
    st3.riseMyHand();

    return QCoreApplication::exec();
}
