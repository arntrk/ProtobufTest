#include "Person.pb.h"

int main(int argn, char **argv)
{
    Person message;

    message.set_id(0);
    message.set_name("Some NAme");
    message.set_email("soame_name@gmail.com");

    std::cout << message.id() << ", " << message.name() << ", " << message.email() << std::endl;
}
