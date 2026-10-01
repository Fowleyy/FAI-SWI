#ifndef TEACHER_H
#define TEACHER_H

#include <QObject>

class teacher : public QObject
{
    Q_OBJECT
public:
    explicit teacher(QObject *parent = nullptr);
    void goToTheClass();

signals:
    void classEntered(void);

public slots:
    void noticeStudent(QString studentName);
};

#endif // TEACHER_H
