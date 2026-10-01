#include <QApplication>
#include <QPushButton>
#include <QDebug>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    QPushButton pb("Click me!");
    pb.setGeometry(100,100,200,300);
    pb.show();

    QObject::connect(&pb, &QPushButton::clicked, [](){
        qInfo() << "Good bye!";
    });

    QObject::connect(&pb, &QPushButton::clicked, &a,&QApplication::quit);

    return QApplication::exec();
}
