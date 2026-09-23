#include <iostream>
#include <vector>
#include <string>

class Vehicle {
    std::string type;
    std::string spz;

public:
    Vehicle(const std::string& t, const std::string& s) : type(t), spz(s) {
        std::cout << "[Vehicle] Konstruktor: " << type << " - " << spz << std::endl;
    }

    Vehicle(const std::string& str) {
        size_t delim = str.find(';');
        if (delim != std::string::npos) {
            type = str.substr(0, delim);
            spz = str.substr(delim + 1);
        } else {
            type = "";
            spz = "";
        }
        std::cout << "[Vehicle] Konverzni konstruktor: " << type << " - " << spz << std::endl;
    }

    operator std::string() const {
        return type + " - " + spz;
    }

    const std::string& getType() const { return type; }
    const std::string& getSpz() const { return spz; }

    ~Vehicle() {
        std::cout << "[Vehicle] Destruktor: " << type << " - " << spz << std::endl;
    }
};

class Driver {
    std::string name;
    std::string licence;
public:
    Driver(const std::string& n, const std::string& l) : name(n), licence(l) {
        std::cout << "[Driver] Konstruktor: " << name << " | " << licence << std::endl;
    }

    Driver(const std::string& str) {
        size_t delim = str.find('|');
        if (delim != std::string::npos) {
            name = str.substr(0, delim);
            licence = str.substr(delim + 1);
        } else {
            name = "";
            licence = "";
        }
        std::cout << "[Driver] Konverzni konstruktor: " << name << " | " << licence << std::endl;
    }

    operator std::string() const {
        return name;
    }

    const std::string& getName() const { return name; }
    const std::string& getLicence() const { return licence; }

    ~Driver() {
        std::cout << "[Driver] Destruktor: " << name << " | " << licence << std::endl;
    }
};

class Assignment {
    Driver* driver;
    Vehicle* vehicle;
public:
    Assignment(Driver* d, Vehicle* v) : driver(d), vehicle(v) {
        std::cout << "[Assignment] Vytvoreno: " << d->getName() << " <-> " << v->getType() << " - " << v->getSpz() << std::endl;
    }

    std::string getDescription() const {
        return "Ridic " + driver->getName() + " ridi vozidlo " + vehicle->getType() + " - " + vehicle->getSpz();
    }
};

class Fleet {
    std::vector<Vehicle*> vehicles;
    std::vector<Assignment> assignments;
public:
    Fleet() {
        std::cout << "[Fleet] Konstruktor\n";
    }

    void addVehicle(Vehicle* v) {
        vehicles.push_back(v);
    }

    void assignDriver(Driver* d, Vehicle* v) {
        assignments.emplace_back(d, v);
    }

    void printAssignments() const {
        std::cout << "\n--- Seznam prirazeni ---\n";
        for (const auto& a : assignments) {
            std::cout << a.getDescription() << std::endl;
        }
        std::cout << "------------------------\n";
    }

    ~Fleet() {
        std::cout << "[Fleet] Destruktor\n";
        for (auto v : vehicles) {
            delete v;
        }
        vehicles.clear();
        std::cout << "[Fleet] Vsechna vozidla odstranena\n";
    }
};

// ------- main ----------
int main() {
    Driver d1("Jan Novak", "Skupina B");
    Driver d2("Petra Sykorova", "Skupina C");
    Driver d3("Tomas Maly|Skupina A");
    Driver d4("Alena Hruba|Skupina B+E");

    Vehicle* v1 = new Vehicle("Auto", "4A2 3020");
    Vehicle* v2 = new Vehicle("Motorka", "9T7 5555");
    Vehicle* v3 = new Vehicle("Nakladni vuz;2BC 8876");

    Fleet fl;
    fl.addVehicle(v1);
    fl.addVehicle(v2);
    fl.addVehicle(v3);

    fl.assignDriver(&d1, v1);
    fl.assignDriver(&d2, v3);
    fl.assignDriver(&d3, v2);

    fl.printAssignments();

    fl.assignDriver(&d4, v1);
    std::cout << "\nPo pridani dalsiho prirazeni:\n";
    fl.printAssignments();

    return 0;
}